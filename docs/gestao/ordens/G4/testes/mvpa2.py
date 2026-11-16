import sys
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

def rodar(n_neuronios, janela_s, r_basal, amplitude, largura, n_por_classe=60, orient=(0,45,90,135)):
    rng = np.random.default_rng(0)
    orientacoes = np.array(orient)
    pref = np.linspace(0, 180, n_neuronios, endpoint=False)
    y = np.repeat(np.arange(len(orientacoes)), n_por_classe)
    thetas = orientacoes[y][:, None]
    diff = np.abs(thetas - pref[None, :])
    diff_circ = np.minimum(diff, 180.0 - diff)
    taxas_esperadas = r_basal + amplitude * np.exp(-0.5 * (diff_circ / largura) ** 2)
    contagens = rng.poisson(taxas_esperadas * janela_s)
    taxas = contagens / janela_s
    X_treino, X_teste, y_treino, y_teste = train_test_split(taxas, y, test_size=0.25, stratify=y, random_state=0)
    dec = [("log", make_pipeline(StandardScaler(), LogisticRegression(C=1.0, max_iter=1000, random_state=0))),
           ("knn", make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=7))),
           ("lda", LinearDiscriminantAnalysis())]
    out = []
    for nome, clf in dec:
        clf.fit(X_treino, y_treino)
        out.append(accuracy_score(y_teste, clf.predict(X_teste)))
    return out


for n, T, orient in [(40,0.3,(0,10,20,30)),(40,0.3,(0,5,10,15)),(40,0.2,(0,10,20,30)),(40,0.1,(0,10,20,30)),(30,0.2,(0,10,20,30)),(40,0.3,(80,85,90,95)),(40,0.3,(0,6,12,18)),(40,0.2,(0,6,12,18))]:
    print(n, T, orient, ["%.3f" % a for a in rodar(n, T, 5, 45, 25, orient=orient)])
