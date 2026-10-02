from typing import final

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

new_2 = pd.read_csv("credenziali_pulite.csv")

X = new_2.drop(columns = ["ESITO"])
y = new_2["ESITO"]

print("----------------------------------------------- STANDARD SCALER ------------------------------------------------")
scaler = StandardScaler()
X = scaler.fit_transform(X)

print("Lo standard scaler è -> ", X)

print("----------------------------------------------- RANDOM FORREST CLASSIFIER ------------------------------------------------")
forest = RandomForestClassifier()
forest.fit(X, y)

model = forest.predict(X)
forest.score(X, y)

accuracy = accuracy_score(y, model)

print("Il model del Forrest -> ", model)
print("Il accuracy del Forrest -> ", accuracy)

joblib.dump(forest, 'credenziali_forrest.pkl')
joblib.dump(scaler, 'credenziali_scaler.pkl')

print("Dati caricati correttamente!!!!")


