# ES1: Gestione Magazzino

**Obiettivo:** Modifica quantità articoli con input utente.

**Dati iniziali:**
```python
magazzino = {"matita": 3, "penna": 2, "quaderno": 5}
```

**Input esempio:**
```
cosa modificare? penna
scelta quantità? 4
```

**Output atteso:**
```
{'matita': 4, 'penna': 4, 'quaderno': 5}
```

**Istruzioni:**
1. Aumenta "matita" di 1
2. Chiedi chiave e nuova quantità
3. Aggiorna solo se chiave esiste
4. Stampa dizionario finale

**Livello:** Base dizionari
**Hint:** `if scelta in magazzino:`