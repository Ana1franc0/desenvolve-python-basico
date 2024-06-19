import re

def processar_texto(texto):
    texto_limpo = re.sub(r'[^a-zA-Z\s]', '', texto)
    palavras = texto_limpo.split()
    return palavras

with open('palavras.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()

palavras = processar_texto(conteudo)
with open('palavras.txt', 'w', encoding='utf-8') as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + '\n')

with open('palavras.txt', 'r', encoding='utf-8') as arquivo:
    conteudo_final = arquivo.read()
    print(conteudo_final)