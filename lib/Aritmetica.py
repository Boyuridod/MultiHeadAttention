import math

def exponencialRapida(x, y):
    if(y == 0):
        return 1
    elif(y == 1):
        return x
    elif(y % 2 == 0):
        aux = exponencialRapida(x, y/2)
        return aux * aux
    else:
        aux = exponencialRapida(x, math.floor(y/2))
        return aux * aux * x
    
def getTransposta(x):
    y = []

    for j in range(len(x[0])):
        aux = []
        for i in range(len(x)):
            aux.append(x[i][j])

        y.append(aux)

    return y
    
def multMatriz(x, y):
    mult = []
    for i in range(len(x[0])):
        mult.append([])
        for j in range(len(y)):
            for k in range(len(x)):
                mult[i][j] += x[i][k] * y[k][j]

    return mult