materie = ['Matematica', 'Filosofia', 'Geografia', 'Musica']
fasce_giudizi = {
    'A': [70, 100], 'B': [60, 69], 'C': [50, 59],
    'D': [40, 49], 'E': [30, 39], 'F': [0, 29],
}
print('\n--- Inserimento voti ---')
risultati = {}
for materia in materie:
    while True:
        voto = float(input(f'Che voto hai preso in {materia}? '))
        if 0 <= voto <= 100:
            break
        else:
            print('Il voto deve essere tra 0 e 100. Riprova.')
    for giudizio in fasce_giudizi:
        if fasce_giudizi[giudizio][0] <= voto <= fasce_giudizi[giudizio][1]:
            risultati[materia] = giudizio
            break
print(risultati)