#10
''
class Dias:
    def __init__(self):
        self.dia = 0
        self.hora = 0
        self.total = 0
    def conversor(self):
        self.dia = float(input("Dias percorridos: "))
        self.hora = float(input("Horas percorridas: "))
        self.total = self.dia * 24 + self.hora
        return "total de horas", self.total
    def menu(self):
        while True:
            w = input("Deseja converter dias e horas passadas em horas totais? (S/N): ").upper()
            if w == "S":
                print(self.conversor())
            else:
                break

dias = Dias()
if __name__ == "__main__":
    dias.menu()
