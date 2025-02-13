from lib.Aritmetica import criaMatriz, exponencialRapida, getTransposta, multMatriz

# Geral

dmodel = 512

heads = 8

dk = int(dmodel / heads)

# Pré-Computados

Wq = criaMatriz(2, 3)
Wk = criaMatriz(2, 3)
Wv = criaMatriz(2, 3)

# Entrada da MHA

query = [
    [2, 4, 8],
    [9, 5, 4]
]

keys = [
    [3, 2, 1],
    [2, 1, 5]
]

values = [
    [5, 5, 5],
    [7, 7, 9]
]

keysT = getTransposta(keys)

