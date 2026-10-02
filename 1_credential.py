from typing import Any

import pandas as pd
import numpy as np
from random import randint, choice, random

def crea_credenziali() -> pd.DataFrame:
    utente: dict = {"ID_UTENTE" : [],
                    "CONTO_CORRENTE" : [],
                    "ENTRATE" : [],
                    "USCITE" : [],
                    "DEBITO" : [],
                    "TIPOLOGIA_LAVORO" : [],
                    "PUNTEGGIO_CREDITO" : [],
                    "ESITO" : []
                    }

    for i in range(100):
        id : int = np.random.randint(1, 10)
        conto_corrente: int = np.random.randint(-1000, 50000)
        entrate: int = np.random.randint(800, 5000)
        uscite: int = np.random.randint(300, 10000)
        lavoro: str = choice(["Indeterminato", "Determinato", "Partita_IVA", "Disoccupato"])
        punteggio_credito : int = np.random.randint(1, 10)
        debito_credito: int = np.random.randint(-1000, 5000)

        esito: int = 0
        if entrate > uscite and punteggio_credito > 6 and lavoro == "Indeterminato" or lavoro == "Partita_IVA":
            print("CONCESSO ✅")
            esito += 1
        else:
            esito = 0
            print("NEGATO!!! ❌")

        utente["ID_UTENTE"].append(id)
        utente["CONTO_CORRENTE"].append(conto_corrente)
        utente["ENTRATE"].append(entrate)
        utente["USCITE"].append(uscite)
        utente["DEBITO"].append(debito_credito)
        utente["TIPOLOGIA_LAVORO"].append(lavoro)
        utente["PUNTEGGIO_CREDITO"].append(punteggio_credito)
        utente["ESITO"].append(esito)

    return pd.DataFrame(utente)

new_id = crea_credenziali()
new_id.to_csv("credenziali.csv", index=False)
print("Credenziali salvate con successo ✅!!! ")












