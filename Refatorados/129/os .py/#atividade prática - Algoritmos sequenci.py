class AtividadePratica:

    @staticmethod
    def um():  # Calculo de hipotenusa
        import math
        q1a = float(input("Valor do cateto oposto: "))
        q1b = float(input("Valor do cateto adjacente: "))
        if q1a > 0 and q1b > 0:
            hipotenusa = math.sqrt(q1a**2 + q1b**2)
            print(f"A hipotenusa é: {hipotenusa}")
        else:
            print("Valor inválido")
    
    @staticmethod
    def dois():  # Calculo de trapezio
        q2a = float(input("Valor da base maior: "))
        q2b = float(input("Valor da base menor: "))
        q2c = float(input("Altura: "))
        area = ((q2a + q2b) * q2c) / 2
        print(f"A área do trapézio é: {area}")
    
    @staticmethod
    def tres():  # Conversão de temperatura
        q3a = input("Escolha para qual base converter: 'F' para Fahrenheit ou 'C' para Celsius: ").strip().lower()
        if q3a == "f":
            q3b = float(input("Qual o valor em Fahrenheit para converter em Celsius? "))
            celsius = (q3b - 32) * 5/9
            print(f"A conversão é: {celsius}°C")
        elif q3a == "c":
            q3c = float(input("Qual o valor em Celsius para converter em Fahrenheit? "))
            fahrenheit = (q3c * 9/5) + 32
            print(f"A conversão é: {fahrenheit}°F")
        else:
            print("Opção inválida")
    
    @staticmethod
    def quatro():  # Calculo de área e perímetro de um quadrado
        q4a = float(input("Valor do lado de um quadrado: "))
        area = q4a**2
        perimetro = 4 * q4a
        print(f"Área do quadrado: {area}\nPerímetro do quadrado: {perimetro}")
    
    @staticmethod
    def cinco():  # Calculo de média ponderada
        q5a = input("Nome do aluno: ")
        q5b = float(input("Nota na prova: "))
        q5c = float(input("Nota no trabalho: "))
        q5d = float(input("Nota qualitativa: "))
        media = (q5b * 5 + q5c * 3 + q5d * 2) / 10
        print(f"A média do {q5a} é: {media}")
    
    @staticmethod
    def seis():  # Calculo de valor por cliente
        q6a = float(input("Valor da conta: "))
        q6b = float(input("Número de clientes: "))
        valor_por_cliente = q6a / q6b
        print(f"Valor por cliente: R$ {valor_por_cliente}")
    
    @staticmethod
    def sete():  # Calculo de valor de compra
        q7a = float(input("Valor da compra: "))
        prestacao = q7a / 5
        desconto = q7a * 0.20
        valor_a_vista = q7a - desconto
        print(f"Valor de compra: R$ {q7a}\nValor das prestações: R$ {prestacao}\nValor à vista com desconto: R$ {valor_a_vista}")
    
    @staticmethod
    def oito():  # Calculo de salário
        q8a = float(input("Salário atual: "))
        q8b = float(input("Reajuste (%): "))
        q8c = float(input("Imposto (%): "))
        reajuste = q8a * (q8b / 100)
        salario_ajustado = q8a + reajuste
        imposto = salario_ajustado * (q8c / 100)
        salario_final = salario_ajustado - imposto
        print(f"Salário inicial: R$ {q8a}\nReajuste: R$ {reajuste}\nImpostos: R$ {imposto}\nSalário final: R$ {salario_final}")
    
    @staticmethod
    def nove():  # Calculo de valor de jantar
        q9a = float(input("Valor do jantar: R$ "))
        taxa = q9a * 0.10
        total = q9a + taxa
        print(f"Valor do garçom: R$ {taxa}\nValor total a pagar: R$ {total}")
    
    @staticmethod
    def dez():  # Calculo de dias e horas
        q10a = float(input("Dias percorridos: "))
        q10b = float(input("Horas percorridas: "))
        total_horas = (q10a * 24) + q10b
        print(f"Número de dias: {q10a}\nNúmero de horas: {q10b}\nTotal de horas: {total_horas}")
    
    @staticmethod
    def menu():
        while True:
            try:
                opcao = int(input("Qual questão testar? (1-10): "))
                if 1 <= opcao <= 10:
                    metodo = getattr(AtividadePratica, f'{"um dois tres quatro cinco seis sete oito nove dez".split()[opcao - 1]}')
                    metodo()
                else:
                    print("Opção inválida")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número entre 1 e 10.")
                
if __name__ == "__main__":
    AtividadePratica.menu()
