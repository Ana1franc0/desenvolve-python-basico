import os

frase = input("Digite uma frase: ")
nome_arquivo = "frase.txt"
diretorio_atual = os.path.dirname(os._fspath(__file__))
caminho_arquivo = os.path.join(diretorio_atual, nome_arquivo)
with open(caminho_arquivo, 'w') as arquivo: 
    arquivo.write(frase)
print(f"Frase salva em {caminho_arquivo}")