frase = "O meu amor mora em Roma e me deu um ramo de flores"
objetivo = sorted("amor")
lista_palavras = frase.lower().split(" ")
for palavra in lista_palavras:
    if sorted(palavra) == objetivo:
        print(palavra)
