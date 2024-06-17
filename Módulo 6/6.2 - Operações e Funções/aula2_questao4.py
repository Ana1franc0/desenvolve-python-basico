def receber_lista(n):
    lista = []
    for i in range(n):
        elemento = int(input(f"Digite o elemento {i + 1} da lista: "))
        lista.append(elemento)
    return lista

def intercalar_listas(Lista1, Lista2):
    lista_intercalada = []
    len1, len2 = len(Lista1), len(Lista2)
    min_len = min(len1, len2)
    for i in range(min_len):
        lista_intercalada.append(Lista1[i])
        lista_intercalada.append(Lista2[i])
    if len1 > len2:
        lista_intercalada.extend(Lista1[min_len:])
    else:
        lista_intercalada.extend(Lista2[min_len:])
    return lista_intercalada

def principal():
    quant1 = int(input("Digite a quantidade de elementos da lista 1: "))
    lista1 = receber_lista(quant1)
    quant2 = int(input("Digite a quantidade de elementos da lista 2: "))
    lista2 = receber_lista(quant2)
    lista_intercalada = intercalar_listas(lista1, lista2)