#atividade prática - Algoritmos sequenciais

match (input(""))
'''
#1  apresentar raiz quadrada e sua potencia quadrada
import math
q1a =int(input("um numero por favor"))
q1b =math.sqrt(q1a)
print (q1a*q1a,q1b)
'''
'''
#2 area de um trapézio
q2a = float(input("valor da base maior"))
q2b = float(input("valor da base menor"))
q2c = float(input("altura"))
q2d = ((q2a+q2b)*q2c)/2
print (q2d)
'''
'''
#3 convertor d temperatura

q3a = input("escolha para qual base converte fahrenheit para celsius ou celsius para fahrenheit\n\tvocê tem uma medida em F para Fahrnheit ou em C para celsius\n")
#q3a variavel de definição de tipo de calculo
if q3a =="f" or q3a=="F":
    q3b = input("qual o valor em fahrenheit para converter em celsius?\n")
    
    try:
            q3b = float(q3b)
            print("A conversão é:\n", ((q3b - 32) * 5/9))
    except ValueError:
              print("Cálculo inválido. Tente digitar um número válido.")

if q3a =="c" or q3a=="C":
    q3c = input("qual o valor em celsius para converter em fahrenheit\n")
    if q3c != "back" or q3c != "Back":
        try:
            q3c = float(q3c)
            print("A conversão é:\n", ((q3c * 9/5) + 32))
        except ValueError:
              print("Cálculo inválido. Tente digitar um número válido.")

'''
#4 
'''
q4a = float(input("valor do lado de um quadrado "))
q4b = q4a*q4a
q4c = q4a+q4a
print("area do quadrado\n",q4b,"\nperimitro do quadrado\n",q4c)
'''
#5
'''
print("calculadora de nota")
q5a = str(input("nome do aluno: "))
q5b = int(input("nota na prova: "))
q5c = int(input("nota no trabalho: "))
q5d = int(input("nota qualitativa: "))
q5b = (q5b*5)/10
q5c = (q5c*3)/10
q5d = (q5d*2)/10
q5f = q5b + q5c + q5d
print ("media do",q5a,"é : ",q5f)
'''
#6
'''
q6a=float(input("valor da conta: "))
q6b=float(input("numero de clientes: "))
q6c = q6a/q6b
print ("valor por cliente: R$",q6c)
'''
#7
'''
q7a=float(input("valor da compra: "))
q7b= q7a/5
q7c= q7a-(q7a*0.20)
print("valor de compra é: R$",q7a,"\nvalor das prestações é: R$",q7b,"\nvalor a vista: R$",q7c)
'''
#8
"""
F= float(input("salário atual: "))
A=float(input("reajuste: "))
Z=float(input("imposto: "))
G= F*(A*0.01)
H= F+G
J= H*(Z*0.01)
K= H-J
print("salario inicial: R$",F,"\nreajuste: R$",G,"\nimpostos: R$",J,"\nsalario final: R$",K)
"""
#9
'''
q9a=float(input("valor do jantar: R$"))
q9b= q9a*0.10
q9c= q9a+q9b
print("valor do garçom: R$",q9b,"\nvalor total a pagar: R$",q9c)
'''
#10
'''
q10a=float(input("dias percoridos:"))
q10b=float(input("hora percoridas:"))
q10c=q10a*24
q10d=q10c+q10b
print("N° dias",q10a,"\nN° de horas:",q10b,"\ntotal de horas:",q10d)
'''