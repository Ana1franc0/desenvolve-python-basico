frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
contador_vogais = 0
indices_vogais = []
for indice, caractere in enumerate(frase):
    if caractere in vogais:
        contador_vogais += 1
        indices_vogais.append(indice)

print(f"Vogais: {contador_vogais}")
print(f"índices: {indices_vogais}")