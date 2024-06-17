import random

aleatorios = []
for i in range(20):
    valor = random.randint(-100, 100)
    aleatorios.append(valor)

print("Lista ordenada:", sorted(aleatorios))
print("Lista original:", aleatorios)
print("O maior valor está no índice:", aleatorios.index(max(aleatorios)))
print("O menor valor está no índice:", aleatorios.index(min(aleatorios)))