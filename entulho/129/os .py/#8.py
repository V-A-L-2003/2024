w=True
while w:
    w=str(input("deseja descobrir a media e com isso descobrir se foi aprovado?:(S),(N)"))
    if w=="S":
           w= True
    if w=="N":
            w=False

    q1= float(input("nota 1"))
    if q1>10 or q1<0:
        print("o numero da nota não atigem o padrão 10 maxima e 0 minima")
    q2=float(input("nota 2"))
    if q2>10 or q2<0:
                print("o numero da nota não atigem o padrão 10 maxima e 0 minima")
    q3=float(input("nota 3"))
    if q3>10 or q3<0:
            print("o numero da nota não atigem o padrão 10 maxima e 0 minima")

    rfinal=(q1+q2+q3)/3
    if rfinal == 6 or rfinal >=6:
            print(rfinal, "foi o suficiente para ser aprovado")
    if rfinal == 4:
            print(rfinal,"essa nota não foi o suficiente para ser aprovado porem o exame ainda é uma opção")
    if rfinal <4:
            print("exame não é mais uma opção o aluno foi reprovado")
    else:
            w=str(input("deseja descobrir a media e com isso descobrir se foi aprovado?:(S),(N)"))
    if w=="S":
        w= True
    if w=="N":
        w= False
