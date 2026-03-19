# ES2: Calcolo Mediana

**Input dati:** `lista = [1,2,7,3,5,2]`

**Output atteso:**
```
[1, 2, 2, 3, 5, 7]
3.0
```

**Istruzioni:**
1. Ordina la lista
2. Calcola mediana:
   - Se lunghezza pari: `(lista[n//2] + lista[n//2-1])/2`
   - Se dispari: `lista[n//2]`
3. Stampa lista ordinata e mediana

**Livello:** Liste + if/else
**Hint:** `lista.sort()`, `n = len(lista)`