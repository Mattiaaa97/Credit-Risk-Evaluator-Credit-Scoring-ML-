import pandas as pd

new = pd.read_csv("credenziali.csv")

df: pd.DataFrame = pd.get_dummies(new, columns=["TIPOLOGIA_LAVORO"])
print(df.head())

df = df.drop(columns=["ID_UTENTE"])

df.to_csv("credenziali_pulite.csv", index=False)

print("File puliti con successo")

