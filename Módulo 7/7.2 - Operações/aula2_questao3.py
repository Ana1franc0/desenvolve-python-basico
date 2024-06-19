import string

def remover_pontuação(s):
    return ''.join(char for char in s if char not in string.punctuation)

def eh_palindromo(s):
    s = remover_pontuação(s).lower().replace(" ", "")
    return s == s[::-1]

def main():
    while True:
        frase = input("Digite uma frase (Digite 'fim' para encerrar): ")
        if frase.lower() == 'fim':
            break
        if eh_palindromo(frase):
            print(f"{frase} é palíndromo")
        else: 
            print(f"{frase} não é palíndromo")

