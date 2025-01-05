import random

Random_in_python_code_dictionary = {
    '1': 'print',
    '2': 'if',
    '3': 'else',
    '4': 'elif',
    '5': 'match',
    '6': 'case',
    '7': 'while',
    '8': 'for',
    '9': 'type'
}

gene = [0]  # Initialize gene with a list containing one element
contador = -1
codegene = []

while True:
    geracao = gene[0]
    match geracao:
        case 0:
            gene[0] = 1
        case _:
            if gene[0] == 1:
                Lencodegene = random.randint(1, 10)  # Generate a random length
                codegene = []  # Reset codegene for each generation
                while Lencodegene > 0:  # Loop until Lencodegene is 0
                    contador += 1
                    random_key = str(random.randint(1, 9))  # Get a random key as a string
                    codegene.append(Random_in_python_code_dictionary[random_key])  # Append to codegene
                    Lencodegene -= 1  # Decrease the length counter
                gene.append(' '.join(codegene))  # Join the codegene list into a string
                print(gene)
                break 