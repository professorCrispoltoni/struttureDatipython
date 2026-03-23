squadra = {
    "Mario": 17,
    "Luca": 25,
    "Giulia": 19,
    "Sara": 12
}

# 1. Giocatori maggiorenni
print("Giocatori maggiorenni:")
for nome, eta in squadra.items():
    if eta >= 18:
        print(f"{nome} - {eta}")

# 2. Età minima
eta_min = 200
persona_min = ""

# 3. Età massima
eta_max = 0
persona_max = ""

# 4. Media età
somma_eta = 0

for nome, eta in squadra.items():
    # minimo
    if eta < eta_min:
        eta_min = eta
        persona_min = nome

    # massimo
    if eta > eta_max:
        eta_max = eta
        persona_max = nome

    # somma per media
    somma_eta += eta

media = somma_eta / len(squadra)

print(f"\nEtà minima: {eta_min} ({persona_min})")
print(f"Età massima: {eta_max} ({persona_max})")
print(f"Media età: {media:.2f}")
