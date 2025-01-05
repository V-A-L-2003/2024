numeros = []

for i in range(10):
    try:
        num = float(input(f"Digite o {i+1}º número real: ")) 
        numeros.append(num)
    except ValueError:  
        print("Por favor, insira um número válido.")

if numeros:
    soma = sum(numeros)
    media = soma / len(numeros)
    maior = max(numeros)
    menor = min(numeros)

    positivos = len([num for num in numeros if num > 0])
    negativos = len([num for num in numeros if num < 0])

    print(f"Soma: {soma}")
    print(f"Média: {media}")
    print(f"Maior elemento: {maior}")
    print(f"Menor elemento: {menor}")
    print(f"Quantidade de elementos positivos: {positivos}")
    print(f"Quantidade de elementos negativos: {negativos}")
else:
    print("Nenhum número válido foi inserido.")
