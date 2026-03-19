palline = []
conteggi = {'blu': 0, 'rossa': 0}
while True:
    inserimento = input("Inserisci rossa o blu (stop per finire, del per eliminare ultimo): ")
    if inserimento == "stop":
        break
    if inserimento == "blu":
        palline.append(inserimento)
        conteggi[inserimento] += 1
    elif inserimento == "rossa":
        palline.append(inserimento)
        conteggi[inserimento] += 1
    elif inserimento == "del":
        if palline:
            last = palline.pop()
            conteggi[last] -= 1
            print(f"Rimossa: {last}")
        else:
            print("Lista vuota!")
    else:
        print("Colore non valido!")
print(f"Sequenza palline: {palline}")
print(f"Conteggi: blu={conteggi['blu']} rossa={conteggi['rossa']}")