def formatar_numero_celular(numero):
    if len(numero) == 8:
        numero_completo = '9' + numero
    elif len(numero) == 9 and numero[0] == '9':
        numero_completo = numero
    else:
        return "Número inválido!"
    numero_formatado = numero_completo[:5] + '-' + numero_completo[5:]
    return numero_formatado

numero = input("Digite o número: ")
numero_completo = formatar_numero_celular(numero)
print(f"Número completo: {numero_completo}") 