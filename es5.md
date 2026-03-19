# ES5: Conteggio Picchi (Olimpiadi Style)

**Input formato Olimpiadi:**
```
5
1 3 2 4 1
```

**Output atteso:** `1` (picco a 3)

**Obiettivo:** Conta elementi > precedente E > successivo.

**Istruzioni:**
1. `n = int(input())`
2. `quote = list(map(int, input().split()))`
3. Ciclo da 1 a n-2: if quote[i] > quote[i-1] and > quote[i+1]

**Livello:** Liste + indici + olimpiadi