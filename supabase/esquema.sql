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

-- Permissões da API: só quem está logado ("authenticated") e só o
-- necessário. Visitante sem login ("anon") não recebe nada.
revoke all on public.progresso from anon, authenticated;
grant select, insert, delete on public.progresso to authenticated;
