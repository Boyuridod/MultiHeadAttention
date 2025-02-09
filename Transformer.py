from lib.Vocabulario import vocabulario
from lib.PositionalEncoding import PositionalEncoding
from lib.Aritmetica import multMatriz, getTransposta, criaMatriz
import math

def attention(encoderInput, mat):
    try:
        return multMatriz(encoderInput, mat)  # Calcula a matriz transformada
    except Exception as e:
        print(f"❌ [ERRO] Exception na função attention: {e}")

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
for i in range(tamFrase):
    embedding.append([])
    for j in range(dmodel):
        embedding[i].append(inputID[i] * j)

# Positional Encoding

PE = PositionalEncoding(tamFrase, dmodel)

# Encoder Input

encoderInput = []

for i in range(tamFrase):
    encoderInput.append([])
    for j in range(dmodel):
        encoderInput[i].append(embedding[i][j] + PE[i][j])

# Multi-Head Attention

query = criaMatriz(dmodel, dmodel)
keys = criaMatriz(dmodel, dmodel)
values = criaMatriz(dmodel, dmodel)

query = attention(encoderInput, query)
keys = attention(encoderInput, keys)
values = attention(encoderInput, values)

## Softmax

keysT = getTransposta(keys)

heads = []

for i in range(tamFrase):
    heads.append([])
    for j in range(dmodel):
        heads[i].append((query[i][j] * keysT[j][i]) / math.sqrt(dmodel/tamFrase))

Wo = criaMatriz(dmodel, dmodel)

MultiHead = multMatriz(heads, Wo)

arquivo = open("resultado.txt", "w")

for i in MultiHead:
    arquivo.write(str(i) + "\n")

arquivo.close()

print("✅ [Concluído] Saída salva em 'resultado.txt'")