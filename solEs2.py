lista = [1,2,7,3,5,2]

lista.sort()
print(lista)

n = len(lista)

if n % 2 == 0:
    mediana = (lista[n//2]+lista[n//2-1])/2
else:
    mediana = lista[n//2]

print(mediana)