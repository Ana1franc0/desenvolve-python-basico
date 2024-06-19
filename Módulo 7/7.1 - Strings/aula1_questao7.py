import random

def encrypt(nomes):
    chave = random.randint(1, 10)
    nomes_criptografados = []
    for nome in nomes:
        nome_criptografado = "" 
        for character in nome:
            novo_caractere = ord(character) + chave
            if novo_caractere > 126:
                novo_caractere = 33 + (novo_caractere - 127)
            nome_criptografado += character(novo_caractere)
            nomes_criptografados.append(nome_criptografado)
    return nomes_criptografados, chave

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_scrypt, chave = encrypt(nomes)
print("Chave de criptografia: ", chave) 
print("Nomes criptografados: ", nomes_scrypt)