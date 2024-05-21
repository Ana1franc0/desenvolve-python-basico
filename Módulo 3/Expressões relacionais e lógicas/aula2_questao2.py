# 2) Dando continuidade à questão anterior, um outro bar permite a entrada de grupos onde pelo menos uma pessoa é maior de idade 
# (ficando responsável pelas outras). Ajuste sua resposta da questão anterior, ainda solicitando as idades de Juliana e Cris, mas
# ajustando a expressão para esse novo cenário, imprimindo True se puderem entrar no bar, e False caso contrário.

# Leitura dos dados (entrada)
Idade_juliana =  int(input("Qual é a idade de Juliana? "))
Idade_cris =  int(input("Qual é a idade de Cris? "))

# Processamento
pode_entrar = Idade_juliana >= 18 or Idade_cris >= 18

# Impressão de dados (saída)
print(pode_entrar)