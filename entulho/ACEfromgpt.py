import random

# Dicionário que armazena estruturas de código
codigo_dict = {
    1: """
if {variavel1} == {variavel2}:
    {proximapalavrachave}
""",
    2: """
for {variavel} in range({numero}):
    {proximapalavrachave}
""",
    3: """
while {condicao}:
    {proximapalavrachave}
""",
    4: """
print("{mensagem}")
""",
    5: """
try:
    {codigo_a_tentar}
except Exception as e:
    print(f"Ocorreu um erro: {erro}")
"""
}

# Função para gerar um código aleatório
def gerar_codigo(tamanho=3):
    codigo_gerado = []
    numeros_blocos = []  # Lista para armazenar os números dos blocos
    
    for _ in range(tamanho):
        representante_numerico = random.choice(list(codigo_dict.keys()))
        numeros_blocos.append(representante_numerico)  # Armazena o número do bloco

        bloco = codigo_dict[representante_numerico]
        
        # Formatação do bloco (apenas para teste, não será armazenado)
        bloco = bloco.format(
            variavel1="x",
            variavel2="y",
            proximapalavrachave="pass",  # O que vem após a condição
            variavel="i",  # Para o loop 'for'
            numero=random.randint(1, 10),  # Número aleatório para o loop
            condicao="True",  # Condição para o loop 'while'
            mensagem="Hello, World!",  # Mensagem para print
            codigo_a_tentar="print('Tentativa de execução')",  # Código para o bloco 'try'
            erro="str(e)"  # Mensagem de erro no bloco 'except'
        )
        codigo_gerado.append(bloco.strip())  # Adiciona o bloco ao código gerado

    return numeros_blocos  # Retorna apenas os números dos blocos gerados

# Função para testar o código gerado
def testar_codigo(codigo):
    try:
        # Executa o código gerado
        exec("\n".join(codigo))
        return 0  # Sucesso (0 para sucesso)
    except Exception as e:
        print(f"Ocorreu um erro ao executar o código: {str(e)}")
        return 1  # Erro (1 para erro)

# Função principal do ACE
def ace(tentativas=10, tipo_geracao=2):
    for tentativa in range(tentativas):
        # Gera o código e cria o gene
        gene = [tentativa + 1]  # Index 0: Geração
        codigo_numeros = gerar_codigo()  # Gera os números dos blocos de código
        erro = testar_codigo(codigo_numeros)  # Testa o código gerado
        gene.append(erro)  # Index 1: Erro (0 ou 1)
        gene.append(tipo_geracao)  # Index 2: Tipo de geração
        gene.append(len(codigo_numeros))  # Index 3: Número de blocos
        gene.extend(codigo_numeros)  # Adiciona os números dos blocos gerados a partir do índice 4

        print(f"Tentativa {tentativa + 1}: {gene}")
        
        # Verifica se houve sucesso na execução
        if erro == 0:  
            print("Código executado com sucesso!\n")
            break
        else:
            print("Erro encontrado. Tentando novamente...\n")
        
        # Adicionando um limite para não ficar em loop infinito
        if tentativa == tentativas - 1:
            print("Limite de tentativas atingido sem sucesso.")

# Inicia o projeto ACE
if __name__ == "__main__":
    ace()
