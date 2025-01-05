class Media:
        def __init__(self):
                self.q1 = 0
                self.q2 = 0
                self.q3 = 0
                self.rfinal = 0
        def calculomedia(self):
                self.q1= float(input("nota 1"))
                if self.q1>10 or self.q1<0:
                        print("o numero da nota não atigem o padrão 10 maxima e 0 minima")
                        return self.q1
                self.q2=float(input("nota 2"))
                if self.q2>10 or self.q2<0:
                        print("o numero da nota não atigem o padrão 10 maxima e 0 minima")
                        return self.q2
                self.q3=float(input("nota 3"))
                if self.q3>10 or self.q3<0:
                        print("o numero da nota não atigem o padrão 10 maxima e 0 minima")
                        return self.q3
                self.rfinal=(self.q1+self.q2+self.q3)/3
                if self.rfinal == 6 or self.rfinal >=6:
                        print(self.rfinal, "foi o suficiente para ser aprovado")
                        if self.rfinal == 4:
                                print(self.rfinal,"essa nota não foi o suficiente para ser aprovado porem o exame ainda é uma opção")
                                if self.rfinal <4:
                                        print("exame não é mais uma opção o aluno foi reprovado")
                                        return self.rfinal
                                        
        def __main__(self):                 
                while True:
                        w=str(input("deseja descobrir a media e com isso descobrir se foi aprovado?:(S),(N)"))
                        if w=="S":
                                media=Media()
                                media.calculomedia()
                        else:
                                break
if __name__ == "__main__":
        media = Media()
        media.__main__()