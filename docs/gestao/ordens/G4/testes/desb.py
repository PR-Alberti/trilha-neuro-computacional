from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, balanced_accuracy_score, precision_score, recall_score, roc_auc_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
for w, flip, sep in [((0.95,0.05),0.02,1.0),((0.95,0.05),0.02,1.5),((0.95,0.05),0.02,2.0),((0.95,0.05),0.0,1.0),((0.95,0.05),0.0,1.5)]:
    X, y = make_classification(n_samples=2000, n_features=12, n_informative=4, n_redundant=2, weights=list(w), flip_y=flip, class_sep=sep, random_state=0)
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, stratify=y, random_state=0)
    res=[]
    for cw in (None, "balanced"):
        m = make_pipeline(StandardScaler(), LogisticRegression(C=1.0, class_weight=cw, max_iter=1000, random_state=0)).fit(Xtr, ytr)
        p = m.predict(Xte); s = m.predict_proba(Xte)[:,1]
        res.append(f"acc={accuracy_score(yte,p):.3f} bal={balanced_accuracy_score(yte,p):.3f} rec={recall_score(yte,p,zero_division=0):.3f} prec={precision_score(yte,p,zero_division=0):.3f} auc={roc_auc_score(yte,s):.3f}")
    print(w, flip, sep, "prev_teste=%.3f" % yte.mean()); print("   ", res[0]); print("   ", res[1])
    if flip == 0.0 or True:
        s = make_pipeline(StandardScaler(), LogisticRegression(C=1.0, max_iter=1000, random_state=0)).fit(Xtr,ytr).predict_proba(Xte)[:,1]
        for tau in (0.5,0.3,0.15):
            p=(s>=tau).astype(int)
            print(f"      tau={tau} acc={accuracy_score(yte,p):.3f} bal={balanced_accuracy_score(yte,p):.3f} rec={recall_score(yte,p,zero_division=0):.3f} prec={precision_score(yte,p,zero_division=0):.3f} f1={f1_score(yte,p,zero_division=0):.3f}")
