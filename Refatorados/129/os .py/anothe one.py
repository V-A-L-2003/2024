#Algoritmo <calculadora>



#Inicio

#Leia v1
print("escolha um numero: ")
v1 = int(input())
#Leia v2
print("escolha um numero: ")
v2 = int(input())
#Leia op
print("escolha a operação:"" 1 para +: 2 para - :  3 para / : 4 para * ")
op = int(input())
#Escolha op
match op:
    case 1:
    # resp = v1+v2;
    #Escreva (resp);
        print(v1+v2)

    case 2:
    # resp = v1-v2;
    #Escreva ( resp);
        print(v1-v2)

    case 3:
    # resp = v1*v2;
    #Escreva ( resp);
        print(v1*v2)

    case 4:
    #resp = v1/v2;
    #Escreva ( resp);
        print(v1/v2)
        
    #Caso contrario
    case _:
    #Escreva('Operação inválida:\n')
        print("Opção invalida")

#Fim_escolha
#Fim