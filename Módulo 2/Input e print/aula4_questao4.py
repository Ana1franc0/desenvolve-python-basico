# 4) Escreva um programa que leia um valor inteiro referente a uma quantia em reais e calcule a menor quantidade possível de notas
# necessárias para pagar aquele valor. As notas possíveis são: 100, 50, 20, 10, 5, 2, 1. A saída deve estar formatada exatamente 
# como indicado. 
# Entrada: 576
# Saída:
# 5 nota(s) de R$100,00
# 1 nota(s) de R$50,00
# 1 nota(s) de R$20,00
# 0 nota(s) de R$10,00
# 1 nota(s) de R$5,00
# 0 nota(s) de R$2,00
# 1 nota(s) de R$1,00

# Leitura dos dados (entrada)
valor = int(input("Digite o valor: "))

# Processamento 
#Começar na maior nota
notas_100 = valor//100 #576 - 500 = 76
#Atualizar quanto falta depois da maior nota
notas_100 = valor % 100
#O valor está atualizado
notas_50 = valor//50 #76 - 50 = 26
notas_50 % 50

notas_20 = valor//20 #26 - 20 = 6
notas_20 % 20

notas_10 = valor//10 # 6 // 10 = 0 (a parte inteira)
notas_10 % 10

notas_5 = valor//5 # 6 // 5 = 1 nota (agora falta 1 real)
notas_5 % 5

notas_2 = valor//2 #1 // 2 = 0 (a parte inteira) então ainda falta 1 real
notas_2 % 2

notas_1 = valor//1 # 1 // 1 = 0
notas_1 % 1

# Impressão de dados (saída)
print(f"{notas_100} nota(s) de 100")
print(f"{notas_50}nota(s) de 50")
print(f"{notas_20} nota(s) de 20")
print(f"{notas_10} nota(s) de 10")
print(f"{notas_5} nota(s) de 5")
print(f"{notas_2} nota(s) de 2")
print(f"{notas_1} nota(s) de 1")