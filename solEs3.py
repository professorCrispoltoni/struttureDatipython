import statistics

giorni = ("lun","mar","mer","gio")

temp = []

for g in giorni:
    t = int(input(f"inserisci temp giorno {g}: "))
    temp.append(t)

media = sum(temp)/len(giorni)

print("media",media)

# VARIANZA
sommatoria = 0
for i in range(len(temp)):
    scarto = temp[i]-media
    sommatoria += (scarto**2)

varianza = sommatoria/(len(temp)-1)
dev_standard = round(varianza**0.5,2)

print("dev_standard", dev_standard)
print("dev_standard_formula", round(statistics.stdev(temp),2))

print("giorni con temperatura sopra la media")
for i in range(len(temp)):
    if temp[i] > media:
        print(giorni[i])