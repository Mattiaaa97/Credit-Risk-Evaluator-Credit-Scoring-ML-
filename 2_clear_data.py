import pandas as pd

def carica_dati(percorso_file: str) -> pd.DataFrame:
    return pd.read_csv(percorso_file)

def elabora_e_pulisci_credenziali(df: pd.DataFrame) -> pd.DataFrame:
    df_trasformato: pd.DataFrame = pd.get_dummies(df, columns=["TIPOLOGIA_LAVORO"])
    print(df_trasformato.head())
    df_pulito = df_trasformato.drop(columns=["ID_UTENTE"])
    return df_pulito

def salva_dati_puliti(df: pd.DataFrame, percorso_file: str) -> None:
    df.to_csv(percorso_file, index=False)
    print("File puliti con successo")

if __name__ == '__main__':
    df_iniziale = carica_dati("credenziali.csv")
    df_elaborato = elabora_e_pulisci_credenziali(df_iniziale)
    salva_dati_puliti(df_elaborato, "credenziali_pulite.csv")

