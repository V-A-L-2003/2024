import random
from collections import deque

carrosN = {
    0: "Audi",
    1: "BMW",
    2: "Ferrari",
    3: "Lamborghini",
    4: "Aston Martin",
    5: "Ford",
    6: "Chevrolet",
    7: "Bentley",
    8: "Toyota",
    9: "Nissan",
    10: "Honda",
}

fila = deque()  # Fila (FIFO)
pilha = []      # Pilha (LIFO)
Ncarros = 10

# Adicionando carros à fila e gerenciando a pilha
while len(fila) < Ncarros:
    jafoi = random.randint(0, 10)  # Gera um número aleatório entre 0 e 10
    if jafoi not in fila:  # Verifica se o carro já foi escolhido
        fila.append(jafoi)  # Adiciona o carro à fila
        
        # Se dois carros foram adicionados, remove um da pilha
        if len(fila) % 2 == 0:
            if pilha:  # Verifica se há carros na pilha
                removido = pilha.pop()  # Remove o carro do topo da pilha
                print(f"Removido da pilha: {carrosN[removido]}")

        pilha.append(jafoi)  # Adiciona o carro à pilha também

# Exibe os carros que estão na fila da corrida
print("Os seguintes carros estão na corrida:")
for carro in fila:
    print(carrosN[carro])

# Exibe os carros que ainda estão na pilha
print("\nOs carros na pilha:")
for carro in pilha:
    print(carrosN[carro])
