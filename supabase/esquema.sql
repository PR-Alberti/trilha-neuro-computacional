-- Esquema do banco no Supabase: progresso de cada aluno.
-- Rodar uma vez em: painel do Supabase → SQL Editor → colar tudo → Run.
-- Pode rodar de novo sem medo: nada aqui apaga dados.

-- Uma linha = "este usuário marcou este tema como estudado".
-- Desmarcar um tema apaga a linha.
create table if not exists public.progresso (
  -- quem marcou; preenchido sozinho com o usuário logado.
  -- "on delete cascade": apagar a conta apaga o progresso junto.
  user_id    uuid        not null default auth.uid()
                         references auth.users (id) on delete cascade,
  -- ex.: '3-2' = módulo 3, tema 2 (mesmo formato usado na página)
  tema       text        not null check (tema ~ '^[0-9]{1,2}-[0-9]{1,2}$'),
  marcado_em timestamptz not null default now(),
  primary key (user_id, tema)
);

-- Row Level Security: sem uma regra (policy) que permita, ninguém lê nem
-- escreve nada. As regras abaixo liberam só as linhas do próprio usuário.
alter table public.progresso enable row level security;

drop policy if exists "ler o proprio progresso" on public.progresso;
create policy "ler o proprio progresso" on public.progresso
  for select to authenticated
  using ((select auth.uid()) = user_id);

drop policy if exists "marcar para si mesmo" on public.progresso;
create policy "marcar para si mesmo" on public.progresso
  for insert to authenticated
  with check ((select auth.uid()) = user_id);

drop policy if exists "desmarcar o proprio progresso" on public.progresso;
create policy "desmarcar o proprio progresso" on public.progresso
  for delete to authenticated
  using ((select auth.uid()) = user_id);

-- Apagar a própria conta (botão "Apagar minha conta" da página).
-- A tabela de usuários (auth.users) não é acessível pela página, então isto
-- é uma função que roda com o poder de quem a criou ("security definer").
-- Ela é segura porque não recebe nenhum parâmetro: só consegue apagar o
-- usuário que a chamou. O progresso dele vai junto (on delete cascade).
create or replace function public.apagar_minha_conta()
returns void
language sql
security definer
set search_path = ''
as $$
  delete from auth.users where id = (select auth.uid());
$$;

revoke all on function public.apagar_minha_conta() from public, anon;
grant execute on function public.apagar_minha_conta() to authenticated;

-- Permissões da API: só quem está logado ("authenticated") e só o
-- necessário. Visitante sem login ("anon") não recebe nada.
revoke all on public.progresso from anon, authenticated;
grant select, insert, delete on public.progresso to authenticated;

-- =====================================================================
-- Exercícios gerados por IA
-- Quem chama o Gemini é a função gerar-exercicios
-- (supabase/functions/gerar-exercicios). A página só lê o histórico.
-- =====================================================================

-- Cada linha = uma geração: os exercícios que a IA criou de uma vez para um
-- aluno, num tema, com as orientações que ele escreveu.
create table if not exists public.exercicios (
  id          bigint      generated always as identity primary key,
  user_id     uuid        not null references auth.users (id) on delete cascade,
  tema        text        not null check (tema ~ '^[0-9]{1,2}-[0-9]{1,2}$'),
  orientacoes text        not null default '' check (char_length(orientacoes) <= 300),
  -- lista de {enunciado, dica, resolucao}
  itens       jsonb       not null check (jsonb_typeof(itens) = 'array'),
  modelo      text        not null,
  criado_em   timestamptz not null default now()
);
create index if not exists exercicios_aluno_tema
  on public.exercicios (user_id, tema, criado_em desc);

alter table public.exercicios enable row level security;

drop policy if exists "ler os proprios exercicios" on public.exercicios;
create policy "ler os proprios exercicios" on public.exercicios
  for select to authenticated
  using ((select auth.uid()) = user_id);

drop policy if exists "apagar os proprios exercicios" on public.exercicios;
create policy "apagar os proprios exercicios" on public.exercicios
  for delete to authenticated
  using ((select auth.uid()) = user_id);

-- O aluno lê e apaga os seus; só a função (service_role) grava. Assim
-- ninguém consegue inserir exercícios sem passar pelo limite diário.
revoke all on public.exercicios from anon, authenticated;
grant select, delete on public.exercicios to authenticated;
grant select, insert on public.exercicios to service_role;

-- Quantas gerações cada aluno fez em cada dia (horário de Brasília).
create table if not exists public.uso_ia (
  user_id  uuid    not null references auth.users (id) on delete cascade,
  dia      date    not null,
  geracoes integer not null default 0 check (geracoes >= 0),
  primary key (user_id, dia)
);

alter table public.uso_ia enable row level security;
-- ninguém lê nem altera a tabela direto: só pelas funções abaixo
revoke all on public.uso_ia from anon, authenticated;

-- O limite diário mora aqui, num lugar só. Para mudar, troque o número e
-- rode o script de novo.
create or replace function public.limite_diario_ia()
returns integer
language sql
immutable
as $$ select 10 $$;

-- "Hoje" no horário de Brasília, para o limite virar à meia-noite daqui.
create or replace function public.hoje_brasilia()
returns date
language sql
stable
as $$ select (now() at time zone 'America/Sao_Paulo')::date $$;

-- Para a página mostrar "restam N gerações hoje".
create or replace function public.geracoes_restantes_hoje()
returns integer
language sql
stable
security definer
set search_path = ''
as $$
  select public.limite_diario_ia() - coalesce((
    select geracoes from public.uso_ia
    where user_id = (select auth.uid()) and dia = public.hoje_brasilia()
  ), 0);
$$;

-- Gasta uma geração do aluno, se ainda houver. Devolve quantas restam
-- depois disso, ou -1 se o limite do dia já acabou. É uma operação só no
-- banco, então dois cliques simultâneos não passam do limite.
create or replace function public.consumir_geracao_ia(p_user uuid)
returns integer
language plpgsql
security definer
set search_path = ''
as $$
declare
  usadas integer;
begin
  insert into public.uso_ia as u (user_id, dia, geracoes)
  values (p_user, public.hoje_brasilia(), 1)
  on conflict (user_id, dia) do update
    set geracoes = u.geracoes + 1
    where u.geracoes < public.limite_diario_ia()
  returning geracoes into usadas;

  if usadas is null then
    return -1;
  end if;
  return public.limite_diario_ia() - usadas;
end;
$$;

-- Devolve a geração quando a IA falha, para o aluno não perder a vez.
create or replace function public.devolver_geracao_ia(p_user uuid)
returns void
language sql
security definer
set search_path = ''
as $$
  update public.uso_ia set geracoes = geracoes - 1
  where user_id = p_user and dia = public.hoje_brasilia() and geracoes > 0;
$$;

-- Quem pode chamar o quê: o aluno só consulta o próprio saldo. Gastar e
-- devolver gerações recebem o id do usuário como parâmetro, então ficam
-- só com a função do servidor (service_role) — senão um aluno poderia
-- devolver gerações para si mesmo sem parar.
revoke all on function public.geracoes_restantes_hoje() from public, anon;
grant execute on function public.geracoes_restantes_hoje() to authenticated;

revoke all on function public.consumir_geracao_ia(uuid) from public, anon, authenticated;
revoke all on function public.devolver_geracao_ia(uuid) from public, anon, authenticated;
grant execute on function public.consumir_geracao_ia(uuid) to service_role;
grant execute on function public.devolver_geracao_ia(uuid) to service_role;
