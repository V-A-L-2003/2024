numeros = []

# Leitura de 10 números
for i in range(10):
    numero = float(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

# a) Soma de todos os elementos
soma = sum(numeros)
print(f"Soma dos elementos: {soma}")

# b) Média dos elementos
media = soma / len(numeros)
print(f"Média dos elementos: {media}")

# c) Maior e menor elemento
maior = max(numeros)
menor = min(numeros)
print(f"Maior elemento: {maior}")
print(f"Menor elemento: {menor}")

# d) Quantidade de elementos positivos e negativos
positivos = len([n for n in numeros if n > 0])
negativos = len([n for n in numeros if n < 0])

print(f"Quantidade de elementos positivos: {positivos}")
print(f"Quantidade de elementos negativos: {negativos}")
