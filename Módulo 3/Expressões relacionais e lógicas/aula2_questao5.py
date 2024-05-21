# 5) Solicite de um usuário seu gênero ("M" ou "F"), sua idade e seu tempo de serviço (em anos) e escreva uma expressão que imprima 
# True se a pessoa já pode se aposentar, ou False caso contrário, de acordo com as seguintes regras:
# A: Para mulheres, ter mais de 60 anos. Para homens, 65.
# B: Ou ter trabalhado pelo menos 30 anos
# C: Ou ter 60 anos  e trabalhado pelo menos 25.

# Leitura dos dados (entrada)
genero = input("Digite seu gênero (M ou F): ")
idade = int(input("Digite sua idade: "))
tempo_serviço = int(input("Digite seu tempo de serviço em anos: "))

# Processamento
a = genero == 'F' and idade >= 60 or genero == 'M' and idade >= 65 
b = tempo_serviço >= 30
c = idade >= 60 and tempo_serviço >= 25
pode_aposentar = a or b or c


# Impressão de dados (saída)
print(pode_aposentar)