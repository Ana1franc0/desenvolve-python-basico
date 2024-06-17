import random

def criar_lista():
    lista = [random.randint(-10, 10) for i in range(20)]
    return lista

def encontrar_maior_intervalo_negativo(lista):
    maior_contagem = 0
    indice_inicio = 0
    indice_fim = 0
    contagem_atual = 0
    inicio_atual = 0
    for i in range(len(lista)):
        if lista[i] < 0:
            contagem_atual += 1
            if contagem_atual == 1:
                inicio_atual = 1
            else:
                if contagem_atual > maior_contagem:
                    maior_contagem = contagem_atual
                    indice_inicio = inicio_atual
                    indice_fim = i 
                    contagem_atual = 0
    if contagem_atual > maior_contagem:
        maior_contagem = contagem_atual
        indice_inicio = inicio_atual
        indice_fim = len(lista)
    return indice_inicio, indice_fim

def deletar_maior_intervalo(lista, inicio, fim):
    del lista[inicio:fim]

lista_original = criar_lista()
inicio, fim = encontrar_maior_intervalo_negativo(lista_original)
deletar_maior_intervalo(lista_original)
print(f"Original: {lista_original}")