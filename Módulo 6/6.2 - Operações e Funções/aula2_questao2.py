import random

num_elementos = random.randint(5, 20)
elementos = [random.randint(1, 10) for i in range(num_elementos)]

print("A lista de elementos:", elementos)
soma = sum(elementos)
print("A soma dos valores da lista:", soma)
media = soma / num_elementos
print("A média dos valores da lista:", media)
