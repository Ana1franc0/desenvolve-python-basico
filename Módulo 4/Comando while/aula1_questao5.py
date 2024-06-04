n = int(input("Digite o número de pessoas: "))
soma = 0
cont = 0 
while cont < n:
    idade = int(input())
    soma = soma + idade
    cont = cont + 1
print(soma)
print(soma/n)