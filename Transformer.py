from lib.Vocabulario import vocabulario
from lib.PositionalEncoding import PositionalEncoding
from lib.Aritmetica import multMatriz, getTransposta, criaMatriz
import multiprocessing
import math

def attention(encoderInput, mat, queue):
    try:
        print("📢 [DEBUG] Iniciando multiplicação de matrizes")  # DEBUG
        result = multMatriz(encoderInput, mat)  # Calcula a matriz transformada
        queue.put(result)  # Envia o resultado para a fila
        print("✅ [DEBUG] Multiplicação concluída!")  # DEBUG
    except Exception as e:
        print(f"❌ [ERRO] Exception na função attention: {e}")
        queue.put(None)  # Garante que a fila recebe algo, evitando deadlock

if __name__ == "__main__":

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

    queue = multiprocessing.Queue()

    heads = []

    for mat in [query, keys, values]:
        p = multiprocessing.Process(target=attention, args=(encoderInput, mat, queue))
        heads.append(p)
        p.start()

    for head in heads:
        print(f"🔄 [DEBUG] Aguardando processo {head.pid} terminar...")
        head.join(timeout=10)  # Timeout de 10 segundos
        if head.is_alive():
            print(f"❌ [ERRO] Processo {head.pid} não respondeu! Pode estar travado.")
            head.terminate()

    resultados = []
    for _ in range(len(heads)):
        if queue.empty():
            print("❌ [ERRO] Fila está vazia! Algum processo pode ter falhado.")
            break
        resultados.append(queue.get())

    # Verifica se recebemos todos os resultados esperados
    if len(resultados) < len(heads):
        print("❌ [ERRO] Não recebemos todos os resultados esperados!")
        exit(1)

    query = resultados[0]
    keys = resultados[1]
    values = resultados[2]

    heads = []

    ## Softmax

    T = 1

    for i in range(dmodel):
        heads.append([])
        for j in range(tamFrase):
            heads[i].append((query[i][j] * (keys[i][j] ** T)) / math.sqrt(dmodel/tamFrase))

    Wo = criaMatriz(dmodel, dmodel)

    MultiHead = multMatriz(heads, Wo)

    for i in MultiHead:
        print(i)