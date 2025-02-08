from math import sin, cos
from lib.Aritmetica import exponencialRapida as expon

def PositionalEncoding(x, dmodel):
    positionalEncoding = []
    for i in range(x):
        positionalEncoding.append([])
        for j in range(dmodel):
            if(x % 2 == 0):
                positionalEncoding.append(sin(i/expon(10000, j / dmodel)))
            else:
                positionalEncoding.append(cos(i/expon(10000, j / dmodel)))
                
    return positionalEncoding

# TODO O ideal era deixar o Positional Encoding pré computado para receber um texto enorme,
# porém como este não é o objetivo da avaliação atual preferi focar apenas no multi-head attention