numeros_pares = [num for num in range(20, 51) if num % 2 == 0]
print("Os números pares entre 20 e 50 são: ", numeros_pares)

valores_quadrados = [num ** 2 for num in [1,2,3,4,5,6,7,8,9]]
print("Os quadrados de todos os valores da lista 1 um a 9 são: ", valores_quadrados)

divisiveis = [num for num in range(1, 101) if num % 7 == 0]
print("Os números entre 1 e 100 divisíveis por 7 são: " ,divisiveis)

paridade = ["Par" if num % 2 == 0 else "ímpar" for num in range(0, 30, 3)]
print("A paridade entre os valores é: ", paridade)