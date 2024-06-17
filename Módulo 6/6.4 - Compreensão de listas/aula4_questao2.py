frase = input("Digite uma frase: ")
vogais = 'aeiouAEIOU'
alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
lista_vogais = sorted([caractere for caractere in frase if caractere in vogais])
lista_consoantes = [caractere for caractere in frase if caractere in alfabeto and caractere not in vogais]
print("Vogais: ", lista_vogais)
print("Consoantes: ", lista_consoantes)