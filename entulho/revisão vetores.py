ex=input("qual exercicio deseja ver?")

match ex:
    case 1:
        """Faça um algoritmo que possua um vetor denominado A que armazene 8
        números inteiros. O programa deve executar os seguintes passos:
        (a) Atribua os seguintes valores a esse vetor:
        1 0 9 -2 -5 7 4 6
        (b) Remova do vetor os valores maiores que 5.
        (c) Armazene em uma variável inteira (simples) a soma entre os valores
        das posições A[0], A[1] e A[4] do vetor e mostre na tela esta soma.
        (d) Modifique o vetor na posição 4, atribuindo a esta posição o valor 100.
        (e) Mostre na tela cada valor do vetor A.""" 
        # Passo (a) - Atribuir os valores ao vetor A
        A = [1, 0, 9, -2, -5, 7, 4, 6]

        # Passo (b) - Remover os valores maiores que 5
        A = [x for x in A if x <= 5]

        # Passo (c) - Somar os valores das posições A[0], A[1] e A[4]
        soma = A[0] + A[1] + A[4]
        print(f"Soma das posições A[0], A[1] e A[4]: {soma}")

        # Passo (d) - Modificar o valor na posição 4 para 100
        A[4] = 100

        # Passo (e) - Mostrar todos os valores do vetor A
        print("Valores do vetor A após as modificações:")
        for valor in A:
            print(valor)

    case 2:
        # Inicializa o vetor e a soma
        vetor = []
        soma = 0

        # Loop para ler até 10 valores ou até que um valor negativo ou zero seja informado
        for i in range(10):
            valor = int(input(f"Digite o valor para a posição {i+1} (ou um valor negativo/zero para encerrar): "))
            
            # Verifica se o valor é negativo ou zero
            if valor <= 0:
                break
            
            # Adiciona o valor ao vetor
            vetor.append(valor)

        # Calcula a soma dos valores maiores que 5
        for num in vetor:
            if num > 5:
                soma += num

        # Exibe a soma dos valores maiores que 5
        print(f"Soma dos valores maiores que 5: {soma}")
    case 3:
        # Inicializando os vetores X e Y
        X = []
        Y = []

        # Lendo os valores de X
        print("Digite 10 valores para o vetor X:")
        for i in range(10):
            valor_x = int(input(f"X[{i}]: "))
            X.append(valor_x)

        # Lendo os valores de Y
        print("Digite 10 valores para o vetor Y:")
        for i in range(10):
            valor_y = int(input(f"Y[{i}]: "))
            Y.append(valor_y)

        # Inicializando o vetor R de 20 elementos
        R = [0] * 20

        # Preenchendo o vetor R
        for i in range(10):
            R[2 * i] = X[i]     # Posições pares recebem os valores de X
            R[2 * i + 1] = Y[i] # Posições ímpares recebem os valores de Y

        # Exibindo o vetor R
        print("Vetor R (intercalado):")
        print(R)
    case 4:
        # Inicializando o vetor D com os valores fornecidos
        D = [3, -3, 7, 18, -1, 6, 1, -4, 25, 29]

        # Passo (a) - Substituir valores negativos por 0, menores que 10 por 1 e os demais por 2
        for i in range(len(D)):
            if D[i] < 0:
                D[i] = 0
            elif D[i] < 10:
                D[i] = 1
            else:
                D[i] = 2

        # Mostrando o vetor após o passo (a)
        print("Vetor após substituições:")
        print(D)

        # Passo (c) - Remover todas as ocorrências de zero
        D = [x for x in D if x != 0]

        # Mostrando o vetor após o passo (c)
        print("Vetor após remover os valores iguais a zero:")
        print(D)

    case 5:
        # Inicializando o vetor V com 8 elementos
        V = []

        # Lendo os valores do vetor V
        print("Digite 8 letras para o vetor V:")
        for i in range(8):
            letra = input(f"V[{i}]: ").upper()  # Armazena a letra em maiúsculo para uniformidade
            V.append(letra)

        # Exibindo o vetor original
        print("Vetor V (original):")
        print(V)

        # Solicitar a letra a ser removida
        letra_remover = input("Digite a letra a ser removida: ").upper()

        # Verificando se a letra está presente no vetor e removendo-a
        if letra_remover in V:
            V.remove(letra_remover)
            print(f"A letra '{letra_remover}' foi removida.")
        else:
            print(f"A letra '{letra_remover}' não está no vetor.")

        # Exibindo o vetor após a remoção
        print("Vetor V (após a remoção):")
        print(V)

