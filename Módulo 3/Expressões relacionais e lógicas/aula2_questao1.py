# 1) Juliana e Cris querem entrar em um bar, mas só podem se ambos forem maiores de idade (>17). Escreva um programa que solicite 
# as idades de Juliana e Cris e imprima True se ambas forem maiores de 17 anos, indicando que podem entrar no bar, e False caso 
# contrário.

# Leitura dos dados (entrada)
Idade_juliana =  int(input("Qual é a idade de Juliana? "))
Idade_cris =  int(input("Qual é a idade de Cris? "))

# Processamento
pode_entrar = Idade_juliana >= 18 and Idade_cris >= 18
nao_pode_entrar = not Idade_juliana >= 18 and Idade_cris >= 18

# Impressão de dados (saída)
print(pode_entrar)
