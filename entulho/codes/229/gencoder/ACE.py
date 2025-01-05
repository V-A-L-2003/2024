#ACE V0.1.1
#log create in 02/10/2024 by V.A.L
import random
blocos_chave = {
        0: """
    print({valorPrint}) 
    """,#estrutura print
        1: """
    if {variavelA} {operador} {variavelB}:
        {proximaChave}
    """,#bloco IF
        2: """
    if {variavelA} {operador} {variavelB}:
        {proximaChave}
    else:
        {proximaChave}
    """,#bloco else
        3: """
    if {variavelA} {operador} {variavelB}:
        {proximaChave}
    elif {variavelA} {operador} {variavelB}:
        {proximaChave}
    else:
        {proximaChave}
    """,#bloco elif
        4: """
    while {variavelA} {operador} {variavelB}:
        {proximaChave}
    """,#Bloco While
        5: """
    for {variavelA} in range({variavelB}, {variavelC}, {variavelD}):
        {proximaChave}
    """,#bloco For
        6: """
    for {variavelA} in {grupoA}:
        {proximaChave}
    """,
        7: """
    try:
        {proximaChave}
    except {tipoErro}:
        {acaoErro}
    """,#bloco Try

        8: """
    return {valorRetorno}
    """,
        9: """
    raise {erro}('{mensagemErro}')
    """,
        10: """
    assert {condicao}, '{mensagemErro}'
    """,
        11: """
    break
    """,
        12: """
    continue
    """,
        13: """
    pass
    """,
        14: """
    global {variavel}
    """,
        15: """
    nonlocal {variavel}
    """,
        16: """
    del {variavel}
    """,
        17: """
    from {biblioteca} import {funcao}
    """,
        18: """
    import {biblioteca}
    """
    }
operadores_logicos = {
        0: "==",  # Igual
        1: "!=",  # Diferente
        2: ">",   # Maior que
        3: "<",   # Menor que
        4: ">=",  # Maior ou igual a
        5: "<=",  # Menor ou igual a
        6: "and", # E lógico
        7: "or",  # Ou lógico
        8: "not", # Negação
        9: "is",  # Identidade
        10: "in"  # Pertence
    }
bibliotecas_nativas = {
        0: "os",             # Interação com o sistema operacional
        1: "sys",            # Manipulação de parâmetros do sistema e variáveis
        2: "math",           # Funções matemáticas
        3: "random",         # Geração de números aleatórios
        4: "datetime",       # Manipulação de datas e horas
        5: "json",           # Manipulação de dados JSON
        6: "re",             # Expressões regulares
        7: "collections",    # Estruturas de dados especializadas
        8: "itertools",      # Funções criadoras de iteradores
        9: "functools",      # Funções úteis para programação funcional
        10: "string",        # Manipulação de strings
        11: "time",          # Funções relacionadas ao tempo
        12: "subprocess",    # Executar novos processos
        13: "pickle",        # Serialização de objetos Python
        14: "csv",           # Manipulação de arquivos CSV
        15: "sqlite3",       # Interação com bancos de dados SQLite
        16: "socket",        # Programação de rede
        17: "threading",     # Programação multi-thread
        18: "multiprocessing" # Programação multi-processo
    }   
tipos_de_erro = {
        0: "SyntaxError'",
        1: "TypeError'",
        2: "ValueError'",
        3: "NameError'",
        4: "IndexError'",
        5: "KeyError'",
        6: "AttributeError'",
        7: "FileNotFoundError'",
        8: "ZeroDivisionError'",
        9: "ImportError'",
        10: "IndentationError'",
        11: "OverflowError'",
        12: "StopIteration'",
        13: "MemoryError'",
        14: "RecursionError'",
    }
metodologia_string={
        0:"geração randomica limitada ou por fitness",
        1:"geração randomica com genoma alvo",
        2:"geração procedural sem alvo"
    }

#gen controler

genoma = [0,0,0,0,0]  # Inicializando com três elementos

genoma[2]= 0 #delcarado metodologia do genoma

genoma[3] =0

metodologia=genoma[2]

genomamodelo = []

fitnessmodel=None

#funçoes

def controlador_geracional():#controlado geracional
    if genoma[0] !=0:
        pass
    elif genoma[0] ==0:
        genoma[0] =1
    else:
        genoma[0]+=1
    #genoma[0] é referente a geração isso é apos ele todos serão por cruzamento

def GeradorRandomicoEstipulado():#gera codigos randomicos com metodo estipulado
    fitnessmodel=int(input("qual modelo de limite sera usado?\n Geracional(numero de gerações)\nQualitativo(qualidade buscada)\n"))
    
def geradordegenoma():# controlador da entrada do random para o array 
    while True:
        if genoma[2]==0:
            validacaogeradordegenoma=0
            print(f"O metodo atual é {genoma[2]},{metodologia_string[0]}")
            validacaogeradordegenoma=int(input("deseja manter essa metodologia 1 para sim 0 para não?\n"))
            if validacaogeradordegenoma==1:
                pass
            else:
                print("entenda quais metodologias disponiveis")
                print("randomica com limite estipulado")
                print("randomica com genoma alvo")
                print("procedural")
                genoma[2]=int(input("qual vc deseja usar?\n"))

        if genoma[2]==1:
            print(f"O metodo atual é {genoma[2]},{metodologia_string[1]}")
            validacaogeradordegenoma=int(input("deseja manter essa metodologia 1 para sim 0 para não?\n"))
            if validacaogeradordegenoma==1:
                pass
            else:
                print("entenda quais metodologias disponiveis")
                print("randomica com limite estipulado")
                print("randomica com genoma alvo")
                print("procedural")
                genoma[2]=int(input("qual vc deseja usar?\n"))

        if genoma[2]==2: 
            print(f"O metodo atual é {genoma[2]},{metodologia_string[2]}")
            validacaogeradordegenoma=int(input("deseja manter essa metodologia? 1 para sim 0 para não\n"))
            if validacaogeradordegenoma==1:
                pass
            else:
                print("entenda quais metodologias disponiveis")
                print("randomica com limite estipulado ")
                print("randomica com genoma alvo")
                print("procedural")
                genoma[2]=int(input("qual vc deseja usar?"))

def conversorgenoma():# transforma o array em um codigo e registra ele no db
    pass

def numerodemembrosgeracionais():#chama de entrada para controle de numera de individuos em todas as gerações 
    genoma[1]=0
    if genoma[1]==0:
        genoma[1]=int(input("numero de membros dessa geração"))        
    #genoma[1] é o numero de membros dessa geração proxima atualização do mesmo serão apenas na criação de novos codigos

#controladores

match metodologia:
    case 0:
        pass
    #aqui entra o codigo que objetivamente gera randomicamente  genomas
    case 1:
        fitnessgenoma=int(input("vetor do genoma buscado ponha virugula split não funciona sem elas"))
        genomamodelo=fitnessgenoma.split(",")
    #sistema de busca por genoma gera ate encontrar
    case 2:
        pass
    #sistema de força bruta numero de membros igual numero de combinações possiveis
    case _:
        genoma[2]=int(input("insira valor para genoma[2]de 0 1 2"))
    #sistema de seleção de metologia de geração
        
#randomica com limite estipulado
#randomica com genoma alvo
#procedural 

geradordegenoma()

