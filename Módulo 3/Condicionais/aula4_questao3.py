# 3) Você está desenvolvendo um programa para verificar se um ano é bissexto. Escreva um código em Python que solicita ao usuário 
# para inserir um ano e imprime "Bissexto" se o ano for (1) divisível por 4 e não for divisível por 100, ou (2) se for divisível 
# por 400. Caso contrário, imprima "Não Bissexto".
# Teste seu código com os valores: 1900 (não bissexto), 2000 (bissexto), 2016 (bissexto) e 2017 (não bissexto). 

# Leitura dos dados (entrada)
ano = int(input("insira um ano: "))

# Processamento
bissexto = ano/4 or not ano/100 or ano/400

# Impressão de dados (saída)
if  ano == bissexto:
    print("Bissexto")
else:
    print("Não bissexto")