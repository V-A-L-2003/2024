catalago = { 
    1: {"Resolucao_Da_Imagem_visao_digital": "HD (720p)", "capacidade_de_armazenamento": "32GB", "valor": 150},
    2: {"Resolucao_Da_Imagem_visao_digital": "Full HD", "capacidade_de_armazenamento": "64GB", "valor": 200},
    3: {"Resolucao_Da_Imagem_visao_digital": "Ultra HD", "capacidade_de_armazenamento": "128GB", "valor": 300},
    4: {"Resolucao_Da_Imagem_visao_digital": "Ultra HD", "capacidade_de_armazenamento": "256GB", "valor": 430},
    5: {"Resolucao_Da_Imagem_visao_digital": "Ultra HD", "capacidade_de_armazenamento": "512GB", "valor": 500}
}

class Visao_digital:
    def __init__(self):
        self.catalago = catalago

    @staticmethod
    def menu():
        print("Seja bem vindo a visão digital terminal de compra")
        for i in range(1, 6):
            print(f"Opção {i}: {catalago[i]['Resolucao_Da_Imagem_visao_digital']} - {catalago[i]['capacidade_de_armazenamento']} - R${catalago[i]['valor']}")
        
    def compra(self):
        self.OP_Visao_Digital = int(input("Qual das 5 opções o cliente escolheu? (1,2,3,4,5): "))
        if self.OP_Visao_Digital < 1 or self.OP_Visao_Digital > 5:
            print("Erro: opção de produto não disponível")
            quit()
        self.QT_visao_digital = int(input("Qual a quantidade de produtos o cliente vai levar?: "))
        if self.QT_visao_digital < 0:
            print("Erro: quantidade inválida")
            quit()
        valor_Total = self.catalago[self.OP_Visao_Digital]["valor"] * self.QT_visao_digital
        if valor_Total > 1000:
            valor_Total -= valor_Total * 0.10
            print("Valor total com desconto: R$", valor_Total)
        else:
            print("Valor total: R$", valor_Total)

if __name__ == "__main__":
    v = Visao_digital()
    v.menu()
    v.compra()
    