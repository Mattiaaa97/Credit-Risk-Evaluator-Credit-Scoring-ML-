import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

def carica_features_e_target(percorso_file: str) -> tuple[pd.DataFrame, pd.Series]:
    df = pd.read_csv(percorso_file)
    X = df.drop(columns=["ESITO"])
    y = df["ESITO"]
    return X, y

def normalizza_features(X: pd.DataFrame) -> tuple[np.ndarray, StandardScaler]:
    print("----------------------------------------------- STANDARD SCALER ------------------------------------------------")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    print("Lo standard scaler è -> ", X_scaled)
    return X_scaled, scaler

def addestra_e_valuta_modello(X_scaled: np.ndarray, y: pd.Series) -> tuple[RandomForestClassifier, np.ndarray, float]:
    print("----------------------------------------------- RANDOM FORREST CLASSIFIER ------------------------------------------------")
    forest = RandomForestClassifier()
    forest.fit(X_scaled, y)
    predizioni = forest.predict(X_scaled)
    forest.score(X_scaled, y)
    accuratezza = accuracy_score(y, predizioni)
    print("Il model del Forrest -> ", predizioni)
    print("Il accuracy del Forrest -> ", accuratezza)
    return forest, predizioni, accuratezza

def salva_modelli(modello: RandomForestClassifier, scaler: StandardScaler) -> None:
    joblib.dump(modello, 'credenziali_forrest.pkl')
    joblib.dump(scaler, 'credenziali_scaler.pkl')
    print("Dati caricati correttamente!!!!")

if __name__ == '__main__':
    features, target = carica_features_e_target("credenziali_pulite.csv")
    features_scalate, scaler = normalizza_features(features)
    modello_forest, predizioni, acc = addestra_e_valuta_modello(features_scalate, target)
    salva_modelli(modello_forest, scaler)



