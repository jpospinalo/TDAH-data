"""
Reconstruye de punta a punta el modelo y la interfaz "Perfil TDAH".

Uso (desde la raíz del repositorio):
    python app/construir_modelo_y_app.py
    python app/construir_modelo_y_app.py [ruta a processed_data.csv] [ruta del html de salida]

Por defecto lee data/processed/processed_data.csv y escribe docs/index.html, que es la
página que publica GitHub Pages. El modelo entrenado (.joblib) y los datos de la página
(payload.json) quedan en app/salida/, que no se sube al repositorio.

Pasos:
  1. Entrena el Random Forest del repo (mismos hiperparámetros y 14 variables
     de notebooks/model_13clases.ipynb), ahora con los 875 casos.
  2. Calcula las métricas de validación cruzada (10 particiones) que muestra la interfaz.
  3. Exporta los árboles a JSON y verifica que la reimplementación de la
     inferencia da las mismas probabilidades que scikit-learn.
  4. Genera los casos ilustrativos, estadísticas de la muestra y datos auxiliares.
  5. Inserta todo en template.html y escribe docs/index.html (archivo autónomo).

Datos de origen: https://github.com/jpospinalo/TDAH-data  (data/processed/processed_data.csv)
"""
import json
import sys
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import sklearn
from sklearn.base import clone
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from sklearn.preprocessing import OrdinalEncoder

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
CSV = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "data" / "processed" / "processed_data.csv"
HTML_OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "docs" / "index.html"
OUT = HERE / "salida"          # modelo .joblib y payload.json (no se versionan)
OUT.mkdir(parents=True, exist_ok=True)
HTML_OUT.parent.mkdir(parents=True, exist_ok=True)

FEATURES = ["edad", "sexo", "escolaridad", "lateralidad", "antecedentes_familiares",
            "antecedentes_obstetricos", "retrasos_desarrollo", "cit", "agresividad_basc3",
            "hiperactividad_basc3", "problemas_conducta_basc3", "problemas_atencion_basc3",
            "atipicidad_basc3", "fluidez_fonologica"]
CAT = ["sexo", "lateralidad", "antecedentes_familiares", "antecedentes_obstetricos", "retrasos_desarrollo"]
NUM = [f for f in FEATURES if f not in CAT]
ZVARS = ["problemas_atencion_basc3", "hiperactividad_basc3", "agresividad_basc3",
         "problemas_conducta_basc3", "atipicidad_basc3", "cit", "fluidez_fonologica", "edad"]

df = pd.read_csv(CSV, encoding="utf-8-sig")
classes = sorted(df.etiqueta.unique())
y = df.etiqueta.map({c: i for i, c in enumerate(classes)}).values
enc = OrdinalEncoder()
X = df[FEATURES].copy()
X[CAT] = enc.fit_transform(X[CAT])

rf = RandomForestClassifier(n_estimators=300, min_samples_leaf=2, class_weight="balanced",
                            random_state=42, n_jobs=-1)

# ---- 2. Validación cruzada (10 particiones) ----
P = cross_val_predict(clone(rf), X.values, y, cv=StratifiedKFold(10, shuffle=True, random_state=42),
                      method="predict_proba")
pred = P.argmax(1)
C = np.array(classes)
sub = lambda l: l.split(" + ")[0]
com = lambda l: l.split(" + ")[1] if " + " in l else "ninguna"
top2 = np.argsort(-P, 1)[:, :2]
conf = P.max(1)
ok = pred == y
print("== Validación cruzada (10 particiones) ==")
print(f"Exactitud 13 clases : {accuracy_score(y, pred):.3f}")
print(f"F1-macro            : {f1_score(y, pred, average='macro'):.3f}")
print(f"Correcta en top-2   : {np.mean([y[i] in top2[i] for i in range(len(y))]):.3f}")
print(f"Acierto subtipo     : {np.mean([sub(a) == sub(b) for a, b in zip(C[y], C[pred])]):.3f}")
print(f"Acierto comorbilidad: {np.mean([com(a) == com(b) for a, b in zip(C[y], C[pred])]):.3f}")
shown = np.floor(conf * 100 + 0.5)  # mismo redondeo que la interfaz (Math.round)
hi = shown >= 60
print(f"Puntaje mostrado >= 60: cobertura {hi.mean():.3f}, acierto {ok[hi].mean():.3f}")

# ---- 1. Modelo final con los 875 casos ----
rf.fit(X.values, y)
joblib.dump({"encoder": enc, "model": rf, "features": FEATURES, "classes": classes,
             "sklearn": sklearn.__version__}, OUT / "modelo_rf_tdah.joblib")

# ---- 3. Exportar árboles y verificar paridad ----
trees = []
for t in rf.estimators_:
    tr = t.tree_
    v = tr.value[:, 0, :]
    v = v / v.sum(1, keepdims=True)
    trees.append({"f": tr.feature.tolist(), "t": [round(float(a), 4) for a in tr.threshold],
                  "l": tr.children_left.tolist(), "r": tr.children_right.tolist(),
                  "v": [[round(float(a), 4) for a in row] for row in v]})


def proba_json(x):
    acc = np.zeros(len(classes))
    for tr in trees:
        n = 0
        while tr["l"][n] != -1:
            n = tr["l"][n] if x[tr["f"][n]] <= tr["t"][n] else tr["r"][n]
        acc += tr["v"][n]
    return acc / len(trees)


Pj = np.array([proba_json(x) for x in X.values])
Ps = rf.predict_proba(X.values)
print(f"\n== Paridad JSON vs scikit-learn (875 casos) ==\nDiferencia máxima: {np.abs(Pj - Ps).max():.2e} · "
      f"misma clase: {(Pj.argmax(1) == Ps.argmax(1)).mean():.3f}")

# ---- 4. Datos auxiliares de la interfaz ----
prof = df.groupby("etiqueta").agg({**{c: "median" for c in NUM}, **{c: (lambda s: s.mode()[0]) for c in CAT}})[FEATURES]


def predict_row(row):
    r = pd.DataFrame([row])[FEATURES].copy()
    r[CAT] = enc.transform(r[CAT])
    return rf.predict_proba(r.values.astype(float))[0]


# Caso ambiguo: mezcla de perfiles típicos de pares que el modelo suele confundir; se elige la de menor confianza
best = None
for a, b in [("TDAH combinado", "TDAH inatento + TND"), ("TDAH combinado + TEAZ", "TDAH combinado"),
             ("TDAH inatento + TEAZ", "TDAH inatento"), ("TDAH combinado", "TDAH hiperactivo/impulsivo")]:
    for w in np.linspace(0.2, 0.8, 25):
        row = prof.loc[a].copy()
        for c in NUM:
            row[c] = int(round(w * prof.loc[a, c] + (1 - w) * prof.loc[b, c]))
        p1 = predict_row(row).max()
        if best is None or p1 < best[0]:
            best = (p1, row.to_dict())
ambiguous = {k: (int(v) if k in NUM else v) for k, v in best[1].items()}

f1c = f1_score(y, pred, average=None)
bins = [(0, 50, "Puntaje < 50"), (50, 60, "Puntaje 50–59"), (60, 70, "Puntaje 60–69"), (70, 101, "Puntaje ≥ 70")]
payload = {
    "features": FEATURES,
    "categorical": {c: list(map(str, cats)) for c, cats in zip(CAT, enc.categories_)},
    "classes": classes, "trees": trees, "sklearn": sklearn.__version__, "n_train": len(df),
    "profiles": {c: {k: (int(v) if k in NUM else v) for k, v in prof.loc[c].items()} for c in classes},
    "global": {**{c: int(df[c].median()) for c in NUM}, **{c: df[c].mode()[0] for c in CAT}},
    "ranges": {c: [int(df[c].min()), int(df[c].max())] for c in NUM},
    "classStats": {c: {"n": int((df.etiqueta == c).sum()), "f1": round(float(f1c[i]), 3)} for i, c in enumerate(classes)},
    "ambiguous": ambiguous,
    "confBins": [{"label": l, "n": int(((shown >= lo) & (shown < h)).sum()),
                  "acc": round(float(ok[(shown >= lo) & (shown < h)].mean()), 3)} for lo, h, l in bins],
    "zvars": ZVARS,
    "stats": {v: [round(float(df[v].mean()), 3), round(float(df[v].std()), 3)] for v in ZVARS},
    "sample": [[int(r[v]) for v in ZVARS] + [classes.index(r["etiqueta"])] for _, r in df.iterrows()],
}

# Casos ilustrativos A–C: parten de un caso real del grupo, acercado un 40 % a la mediana del grupo
# (no reproduce a ningún paciente) y con un puntaje alto pero no perfecto.
def neighbours_ok(row, target):
    V = ZVARS[:7]; st = payload["stats"]
    zc = np.array([(row[v] - st[v][0]) / st[v][1] for v in V])
    Sm = np.array([[(r[i] - st[V[i]][0]) / st[V[i]][1] for i in range(7)] for r in payload["sample"]])
    idx = np.argsort(((Sm - zc) ** 2).sum(1), kind="stable")[:15]
    return sum(payload["sample"][i][-1] == classes.index(target) for i in idx)

demo = {}
for target, lo_, hi_ in [("Desarrollo típico", .75, .92), ("TDAH inatento + TEA", .70, .88), ("TDAH combinado + TND", .70, .88)]:
    med = payload["profiles"][target]; sub_df = df[df.etiqueta == target]; best_d = None
    if target == "Desarrollo típico":
        sub_df = sub_df[sub_df.sexo == "Mujer"]
    for _, r in sub_df.iterrows():
        row = {**med}
        for c in NUM: row[c] = int(round(med[c] + 0.6 * (r[c] - med[c])))
        for c in CAT: row[c] = r[c]
        if abs(row["escolaridad"] - (row["edad"] - 5)) > 2:
            row["escolaridad"] = int(min(7, max(1, row["edad"] - 5 + (0 if row["edad"] < 10 else -1))))
        p = predict_row(row); k = int(p.argmax()); p1 = p.max()
        if classes[k] != target or not (lo_ <= p1 <= hi_): continue
        diff = sum(row[c] != med[c] for c in NUM)
        sc = diff * 0.1 + min(p1, .85) - abs(p1 - .82)
        if best_d is None or sc > best_d[0]: best_d = (sc, row)
    demo[target] = best_d[1]
payload["demoCases"] = demo
(OUT / "payload.json").write_text(json.dumps(payload, separators=(",", ":"), ensure_ascii=False), encoding="utf-8")

# ---- 5. Construir la página autónoma ----
tpl = (HERE / "template.html").read_text(encoding="utf-8")
body = tpl.replace("/*__MODEL__*/null", json.dumps(payload, separators=(",", ":"), ensure_ascii=False))
html = ('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="robots" content="noindex, nofollow">\n'
        '<meta name="description" content="Prototipo de investigación: apoyo a la decisión clínica para perfiles de TDAH en niñas y niños de 6 a 12 años.">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '</head>\n<body>\n' + body + '\n</body>\n</html>\n')
HTML_OUT.write_text(html, encoding="utf-8")
print(f"\nListo: {HTML_OUT}")
