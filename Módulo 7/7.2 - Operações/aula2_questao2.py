def substituir_vogais_por_asteriscos(frase):
    vogais = 'aeiouAEIOU'
    frase_modificada = ''
    for char in frase:
        if char in vogais:
            frase_modificada += '*'
        else:
            frase_modificada += char
    return frase_modificada

frase = input("Digite uma frase: ")
frase_modificada = substituir_vogais_por_asteriscos(frase)
print("Frase modificada: ", frase_modificada)