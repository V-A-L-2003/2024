'''



'''

erro = True

print("seja bem vindo a visão digital terminal de compra")
while erro:
    OP_Visao_Digital= int(input("qual das 5 opções o cliente escolheu?:(1,2,3,4,5) "))
    if OP_Visao_Digital < 1 or OP_Visao_Digital > 5:
        print("erro opção de produto não disponivel")
        quit
    if OP_Visao_Digital == "1" or OP_Visao_Digital == "2" or OP_Visao_Digital == "3" or OP_Visao_Digital == "4" or OP_Visao_Digital != "5":
        pass
    if erro == True:
        QT_visao_digital = int(input("qual a quantidade de produtos o cliente vai levar?: "))
        if QT_visao_digital < 0:
            print("um erro foi encontrado")
            quit
    if OP_Visao_Digital == (1):
        Resolucao_Da_Imagem_visao_digital = ("HD (720p)")
        capacidade_de_armazenamento = ("32GB")
        valor = (150)
    elif OP_Visao_Digital == (2):
        Resolucao_Da_Imagem_visao_digital = ("Full HD")
        capacidade_de_armazenamento = ("64GB")
        valor = (200)
    elif OP_Visao_Digital == (3):
        Resolucao_Da_Imagem_visao_digital = ("Ultra HD")
        capacidade_de_armazenamento = ("128GB")
        valor = (300)
    elif OP_Visao_Digital == (4):
        Resolucao_Da_Imagem_visao_digital = ("Ultra HD")
        capacidade_de_armazenamento = ("256GB")
        valor = (430)
    elif OP_Visao_Digital == (5):
        Resolucao_Da_Imagem_visao_digital = ("Ultra HD")
        capacidade_de_armazenamento = ("512GB")
        valor = (500)

    valor_Total = (valor)*(QT_visao_digital)
    if valor_Total > 1000:
        valor_Total = valor_Total -(valor_Total*0.10)

    print("opção escolhida",OP_Visao_Digital, "Resolução da opção", Resolucao_Da_Imagem_visao_digital, "Capacidade de armazenamento", capacidade_de_armazenamento,"Valor: R$",valor_Total)