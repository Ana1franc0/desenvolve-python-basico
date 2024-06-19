import requests

with open('estomago.txt', 'r', encoding='utf-8') as file:
    linhas = file.readlines()
print("Primeiras 25 linhas do arquivo: ")
for linha in linhas[:25]:
    print(linha.strip())

num_linhas = len(linhas)
print(f"\nNúmero de linhas do arquivo: {num_linhas}")
max_linhas = max(linhas, key=len)
print(f"\nLinha com maior número de caracteres ({len(max_linhas)}) caracteres: ")
print(max_linhas.strip())

nonato_mençoes = sum(1 for linha in linhas if 'Nonato' in linha or 'nonato' in linha)
iria_mençoes = sum(1 for linha in linhas if 'Iria' in linha or 'iria' in linha and not any(palavra in linha for palavra in ['iria']))

print(f"\nNúmero de menções ao personagem 'Nonato': {nonato_mençoes} ")
print(f"\nNúmero de menções ao personagem 'Iria': {iria_mençoes} ")