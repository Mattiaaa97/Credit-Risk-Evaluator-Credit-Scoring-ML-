# 💳 Valutazione Credito e Prestiti (Credit Scoring)

Progetto in Python per simulare l'assegnazione di prestiti, preparare i dati dei richiedenti e addestrare un modello di Machine Learning capace di approvare o rifiutare la richiesta.

---

## 📌 Cosa fa il progetto

- Genera un elenco di 100 clienti con entrate, uscite, debiti, tipo di lavoro e punteggio di credito
- Assegna l'esito del prestito (approvato o rifiutato) in base a regole di reddito e stabilità lavorativa
- Converte i tipi di contratto in formato numerico ed elimina le colonne non necessarie
- Uniforma la scala dei numeri per non sbilanciare i calcoli
- Addestra un algoritmo Random Forest per imparare a prevedere l'esito delle nuove richieste
- Salva sia il modello addestrato sia lo scaler in formato .pkl pronti per l'uso

---

## 📁 I tre file

* 1_credential.py: crea la tabella iniziale con i dati simulati e la salva in credenziali.csv
* 2_clear_data.py: trasforma le categorie del lavoro in numeri, toglie l'ID utente e crea credenziali_pulite.csv
* trasform_data.py: riscala i valori numerici, addestra la Random Forest, calcola l'accuratezza e salva i file .pkl

---

## ⚙️ Come si usa

1. Installa i pacchetti necessari:
pip install pandas numpy scikit-learn joblib

2. Esegui i file nell'ordine corretto:
python 1_credential.py
python 2_clear_data.py
python trasform_data.py

---

Autore: Mattia Dellanoce
