import json

try:
    with open('value.json', 'r') as arq:
        alfanum = json.load(arq)
except FileNotFoundError:
    print("Arquivo value.json não encontrado.")
    

def convert(word):
    numbers = []
    for letter in word:
        up_letter = letter.upper()
        if up_letter in alfanum:
            numbers.append(str(alfanum[up_letter]))
        else:
            numbers.append(letter)
    return ''.join(numbers)


word = input("Insira a frase para conversão: ")

print("A palavra convertida é: \n --->",convert(word))

