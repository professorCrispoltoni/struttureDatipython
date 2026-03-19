magazzino = {
    "matita": 3,
    "penna": 2,
    "quaderno":5
}
magazzino["matita"] += 1
scelta = input("cosa modificare?")
quantita = int(input("scelta quantità"))

if scelta in magazzino.keys():
    magazzino[scelta]=quantita

print(magazzino)