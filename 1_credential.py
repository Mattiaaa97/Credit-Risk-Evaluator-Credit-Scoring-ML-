import numpy as np
import pandas as pd
from random import choice

def genera_dati_credenziali(n_righe: int = 100) -> pd.DataFrame:
    utente: dict = {
        "ID_UTENTE": [],
        "CONTO_CORRENTE": [],
        "ENTRATE": [],
        "USCITE": [],
        "DEBITO": [],
        "TIPOLOGIA_LAVORO": [],
        "PUNTEGGIO_CREDITO": [],
        "ESITO": []
    }

    for _ in range(n_righe):
        id_utente: int = int(np.random.randint(1, 10))
        conto_corrente: int = int(np.random.randint(-1000, 50000))
        entrate: int = int(np.random.randint(800, 5000))
        uscite: int = int(np.random.randint(300, 10000))
        lavoro: str = choice(["Indeterminato", "Determinato", "Partita_IVA", "Disoccupato"])
        punteggio_credito: int = int(np.random.randint(1, 10))
        debito_credito: int = int(np.random.randint(-1000, 5000))

        if entrate > uscite and punteggio_credito > 6 and (lavoro == "Indeterminato" or lavoro == "Partita_IVA"):
            print("CONCESSO ✅")
            esito = 1
        else:
            print("NEGATO!!! ❌")
            esito = 0

        utente["ID_UTENTE"].append(id_utente)
        utente["CONTO_CORRENTE"].append(conto_corrente)
        utente["ENTRATE"].append(entrate)
        utente["USCITE"].append(uscite)
        utente["DEBITO"].append(debito_credito)
        utente["TIPOLOGIA_LAVORO"].append(lavoro)
        utente["PUNTEGGIO_CREDITO"].append(punteggio_credito)
        utente["ESITO"].append(esito)

    return pd.DataFrame(utente)

def salva_dataset_grezzo(df: pd.DataFrame, percorso_file: str) -> None:
    df.to_csv(percorso_file, index=False)
    print("Credenziali salvate con successo ✅!!! ")

if __name__ == '__main__':
    dataset_credenziali = genera_dati_credenziali(100)
    salva_dataset_grezzo(dataset_credenziali, "credenziali.csv")
