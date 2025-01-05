import math

class Calculadora:
    @staticmethod
    def evaluation():
        try:
            expression = input("Calculadora:\n ")
            # Ambiente seguro, permitindo apenas funções e operadores matemáticos
            safe_env = {
                "__builtins__": None,
                "abs": abs,
                "round": round,
                "math": math,
                "pow": pow,
            }
            result = eval(expression, {"__builtins__": None}, safe_env)
            return result
        except Exception as e:
            return f"Erro na avaliação da expressão: {e}"

    def menu(self):
        while True:
            w = input("Deseja fazer um cálculo? (S/N): ").upper()
            if w == "S":
                result = self.evaluation()
                print(f"Resultado: {result}")
            elif w == "N":
                print("Encerrando a calculadora.")
                break
            else:
                print("Opção inválida. Por favor, insira 'S' para sim ou 'N' para não.")

if __name__ == "__main__":
    c = Calculadora()
    c.menu()
