from lib.Vocabulario import vocabulario
from lib.PositionalEncoding import PositionalEncoding
from lib.Aritmetica import multMatriz, getTransposta

dmodel = 512

# Input

## frase = input().split(" ")
frase = ["meu", "primeiro", "cachorro", "chama", "goiaba"]
## frase = "goiaba é minha fruta preferida".split(" ")

tamFrase = len(frase)

# Input Embedding

## Pegar o ID de cada palavra no vocabulário
inputID = []

for i in frase:
    inputID.append(vocabulario[i])

## Fazemos o embedding para cada id de cada palavra
embedding = []

## Uma forma que criei de padronizar os input Embedings
for i in inputID:
    embedding.append([])
    for j in range(dmodel):
        embedding.append(i * j)

# Positional Encoding

PE = PositionalEncoding(tamFrase, dmodel)

# Encoder Input

encoderInput = []

for i in range(tamFrase):
    encoderInput.append([])
    for j in range(dmodel):
        encoderInput.append(embedding[i][j] + PE[i][j])

