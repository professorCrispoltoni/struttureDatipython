import math

A = (0, 0)
B = (2, 0)
C = (2, 2)
D = (0, 2)

def distanza(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

AB = distanza(A, B)
BC = distanza(B, C)
CD = distanza(C, D)
DA = distanza(D, A)

AC = distanza(A, C)
BD = distanza(B, D)

if AB == BC == CD == DA and AC == BD:
    print("I quattro punti formano un quadrato.")
else:
    print("I quattro punti NON formano un quadrato.")