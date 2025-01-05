"""Faça um algoritmo que possua um vetor
denominado A que armazene 8 números inteiros. O
programa deve executar os seguintes passos:
 (a) Atribua os seguintes valores a esse vetor: 1 0 9
-2 -5 7 4 6
 (b) Remova do vetor os valores maiores que 5.
 (c) Armazene em uma variável inteira (simples) a
soma entre os valores das posições A[0], A[1] e
A[4] do vetor e mostre na tela esta soma.
 (d) Modifique o vetor na posição 4, atribuindo a
esta posição o valor 100.
 (e) Mostre na tela cada valor do vetor A"""
# (a) Atribuir os valores ao vetor A
A = [1, 0, 9, -2, -5, 7, 4, 6]
print(A)
# (b) Remover do vetor os valores maiores que 5
A = [x for x in A if x <= 5]
print(A)
# (c) Armazenar a soma entre os valores das posições A[0], A[1] e A[4]
# Note que após a remoção de valores maiores que 5, pode haver menos de 5 elementos no vetor.
if len(A) > 4:
    simple = A[0] + A[1] + A[4]
else:
    simple = "O vetor tem menos de 5 elementos após remoção."

# Mostrar a soma
print(f"Soma dos valores das posições A[0], A[1] e A[4]: {simple}")

# (d) Modificar o vetor na posição 4, atribuindo o valor 100
if len(A) > 4:
    A[4] = 100

# (e) Mostrar cada valor do vetor A
print("Valores do vetor A após modificações:")
for valor in A:
    print(valor)
