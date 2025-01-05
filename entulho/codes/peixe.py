"""
Trabalho de Estrutura de Dados
Autores: Vinicius E Léonardo
Domínio: Jogo de Pesca

Regras de Inserção e Exclusão:
  - A pilha representa camadas de profundidade, onde cada camada simboliza uma nova oportunidade de pesca. A pilha suporta até 10 camadas. 
  - A cada duas camadas removidas, uma nova camada é adicionada, simulando a variação na profundidade do local de pesca.
  - A fila representa a pontuação de peixes pescados e armazena até 10 peixes. Quando o limite é atingido, o peixe mais antigo é removido para liberar espaço.
  - O jogador joga um mini-jogo de "Pedra, Papel e Tesoura" para determinar se consegue ou não pescar um peixe. Ao vencer, um peixe comum é adicionado à fila de pontuação.
  - A cada três peixes comuns pescados, um peixe raro é adicionado à fila.

Descrição:
Este programa utiliza uma pilha e uma fila para simular um jogo de pesca:
1. A **pilha** (camadas) permite empilhar e desempilhar camadas de profundidade, com a capacidade de até 10 camadas, adicionando uma camada nova a cada duas removidas.
2. A **fila** (pontuação) mantém os peixes pescados, com uma capacidade de até 10 peixes. Quando a fila está cheia, o peixe mais antigo é removido automaticamente.

No final, é exibida uma contagem final dos tipos de peixes pescados (comuns e raros).
"""


import random

# Pilha de Camadas de Pesca
max_tamanho_camadas = 10
camadas = []

def empilha(camada):
    if len(camadas) >= max_tamanho_camadas:
        print("Erro: Limite de camadas alcançado! Não é possível adicionar mais camadas.")
    else:
        camadas.append(camada)
        print(f"Camada '{camada}' adicionada.")

def desempilha():
    if not camadas:
        print("Erro: Nenhuma camada disponível para pescar.")
        return None
    else:
        camada = camadas.pop()
        print(f"Pescando na camada '{camada}'.")
        return camada

def exibir_pilha():
    print("\nCamadas restantes:", camadas)
    print("Camada no topo:", camadas[-1] if camadas else None)
    print("Total de camadas:", len(camadas))

# Fila de Pontuação de Peixes Pescados
max_tamanho_peixes = 10
fila_pontuacao = []

# Contador de tipos de peixes
contagem_peixes = {"comum": 0, "raro": 0}

def enfileira(peixe, tipo="comum"):
    if len(fila_pontuacao) >= max_tamanho_peixes:
        desenfileira()  # Remove o peixe mais antigo para liberar espaço
    fila_pontuacao.append(peixe)
    contagem_peixes[tipo] += 1
    print(f"Peixe '{peixe}' ({tipo}) adicionado à fila de pontuação.")
    

def desenfileira():
    if not fila_pontuacao:
        print("Erro: Nenhum peixe para remover.")
        return None
    else:
        peixe = fila_pontuacao.pop(0)
        print(f"Peixe '{peixe}' removido da fila de pontuação.")
        return peixe

def exibir_fila():
    print("\nPeixes restantes na fila de pontuação:", fila_pontuacao)
    print("Primeiro peixe na fila:", fila_pontuacao[0] if fila_pontuacao else None)
    print("Total de peixes na fila:", len(fila_pontuacao))

# Função do Jogo Pedra, Papel e Tesoura
def escolher_opcao():
    print("Escolha uma isca para por no anzol")
    opcoes = ['pantano', 'salgado', 'doce']
    escolha = input("Escolha pantano, salgado ou doce: ").lower()
    if escolha not in opcoes:
        print("Opção inválida! Tente novamente.")
        return escolher_opcao()
    return escolha

def jogar_jokempo():
    opcoes = ['pantano', 'salgado', 'doce']
    computador = random.choice(opcoes)
    jogador = escolher_opcao()

    print(f"\nVocê escolheu: {jogador}")
    print(f"O peixe queria: {computador}")

    if jogador == computador:
        print("Você acertou o que o peixe queria! Ganhou um peixe!")
        return True
    else:
        print("Você perdeu sua isca.")
        return False

# Inicialização das camadas e pontuação de peixes
for i in range(10):
    empilha(f"Camada {i + 1}")

for i in range(10):
    enfileira(f"Peixe comum {i + 1}")

# Regras de pesca e jogo com camadas e peixes raros
remocoes_camadas = 0
pescados = 0

while remocoes_camadas < 11:
    # Pescando de uma camada
    camada = desempilha()
    if camada:
        remocoes_camadas += 1
        # A cada 2 camadas removidas, adiciona uma nova camada
        if remocoes_camadas % 2 == 0:
            empilha(f"Camada Nova {remocoes_camadas + 9}")

        # Jogando jokempô para ganhar peixe
        if jogar_jokempo():
            peixe = f"Peixe da {camada}"
            enfileira(peixe)
            pescados += 1
            
            # A cada 3 peixes, adiciona um peixe raro
            if pescados % 3 == 0:
                enfileira("Peixe raro", tipo="raro")

# Exibir estado final das camadas de pesca e pontuação de peixes
print("\n--- Estado Final das Camadas de Pesca ---")
exibir_pilha()

print("\n--- Estado Final da Fila de Pontuação ---")
exibir_fila()

# Exibir contagem final dos peixes pescados
print("\n--- Contagem Final dos Peixes Pescados ---")
print(f"Peixes Comuns: {contagem_peixes['comum']}")
print(f"Peixes Raros: {contagem_peixes['raro']}")
print("Total de Peixes:", contagem_peixes['comum'] + contagem_peixes['raro'])
