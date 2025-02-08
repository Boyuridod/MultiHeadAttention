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
    if len(x[0]) != len(y):  
        raise ValueError("Número de colunas de x deve ser igual ao número de linhas de y.")

    # Criando a matriz resultante com zeros
    mult = [[0] * len(y[0]) for _ in range(len(x))]

    # Multiplicação correta das matrizes
    for i in range(len(x)):  # Itera sobre as linhas da matriz x
        for j in range(len(y[0])):  # Itera sobre as colunas da matriz y
            for k in range(len(y)):  # Itera sobre os elementos da multiplicação
                mult[i][j] += x[i][k] * y[k][j]

    return mult

def criaMatriz(x, y):
    matriz = []
    for i in range(x):
        matriz.append([])
        for j in range(y):
            matriz[i].append(1)

    return matriz