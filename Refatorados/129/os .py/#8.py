class Aluno:
    def __init__(self):
        self.q1 = 0
        self.q2 = 0
        self.q3 = 0
        self.rfinal = 0

    def calculomedia(self):
        self.q1 = float(input("Nota 1: "))
        if self.q1 > 10 or self.q1 < 0:
            print("A nota deve estar entre 0 e 10.")
            return

        self.q2 = float(input("Nota 2: "))
        if self.q2 > 10 or self.q2 < 0:
            print("A nota deve estar entre 0 e 10.")
            return

        self.q3 = float(input("Nota 3: "))
        if self.q3 > 10 or self.q3 < 0:
            print("A nota deve estar entre 0 e 10.")
            return

        self.rfinal = (self.q1 + self.q2 + self.q3) / 3

        if self.rfinal >= 6:
            print(self.rfinal, "foi o suficiente para ser aprovado.")
        elif self.rfinal == 4:
            print(self.rfinal, "essa nota não foi o suficiente para ser aprovado, porém o exame ainda é uma opção.")
        else:
            print("Exame não é mais uma opção, o aluno foi reprovado.")

    def menu(self):
        while True:
            w = input("Deseja descobrir a média e com isso descobrir se foi aprovado? (S/N): ").upper()
            if w == "S":
                self.calculomedia()
            else:
                break

if __name__ == "__main__":
    aluno = Aluno()
    aluno.menu()
