import random

# Parâmetros
TAMANHO_POPULACAO = 10
TAMANHO_GENOMA = 8
TAXA_MUTACAO = 0.1
GERACOES = 20
CAPACIDADE_MOCHILA = 15

# Itens (peso, valor)
itens = [(2, 3), (3, 4), (4, 5), (5, 8), (9, 10), (4, 7), (2, 6), (1, 2)]

def calcular_aptidao(genoma):
    peso_total = 0
    valor_total = 0
    for i in range(TAMANHO_GENOMA):
        if genoma[i] == 1:
            peso_total += itens[i][0]
            valor_total += itens[i][1]
    if peso_total > CAPACIDADE_MOCHILA:
        return -1  # Penalidade para excesso de peso
    return valor_total

def inicializar_populacao():
    return [[random.randint(0, 1) for _ in range(TAMANHO_GENOMA)] for _ in range(TAMANHO_POPULACAO)]

def selecionar(populacao):
    # Seleção por torneio
    torneio_size = 3
    selecionados = []
    for _ in range(TAMANHO_POPULACAO):
        torneio = random.sample(populacao, torneio_size)
        selecionados.append(max(torneio, key=calcular_aptidao))
    return selecionados

def cruzar(pai1, pai2):
    ponto = random.randint(1, TAMANHO_GENOMA - 1)
    filho1 = pai1[:ponto] + pai2[ponto:]
    filho2 = pai2[:ponto] + pai1[ponto:]
    return filho1, filho2

def mutar(genoma):
    return [bit if random.random() > TAXA_MUTACAO else 1 - bit for bit in genoma]

def evoluir(populacao):
    nova_populacao = []
    for i in range(0, TAMANHO_POPULACAO, 2):
        pai1 = populacao[i]
        pai2 = populacao[i + 1]
        filhos = cruzar(pai1, pai2)
        nova_populacao.extend([mutar(filhos[0]), mutar(filhos[1])])
    return nova_populacao

# Execução do algoritmo
populacao = inicializar_populacao()
for geracao in range(GERACOES):
    populacao = selecionar(populacao)
    populacao = evoluir(populacao)

# Resultados
melhor_individuo = max(populacao, key=calcular_aptidao)
print(f'Melhor Genoma: {melhor_individuo}, Aptidão: {calcular_aptidao(melhor_individuo)}')
