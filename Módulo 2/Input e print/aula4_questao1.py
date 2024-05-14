# 1) Faça um programa para ler as dimensões de um terreno em inteiros (comprimento e largura), bem como o preço do metro quadrado 
# da região em ponto flutuante. Calcule o valor do terreno e imprima o resultado com a formatação apresentada a seguir.
# O terreno possui 250m2 e custa R$512,490.50. Comente na linha acima de cada instrução uma breve descrição da instrução.
# Fórmulas:
# area_m2 = comprimento * largura
# preco_total = preco_m2 * area_m2

# Leitura dos dados (entrada)
Comprimento = int(input("Digite o comprimento: "))
Largura = int(input("Digite a largura: "))
Preço_m2 = float(input("Valor do m2: "))

# Processamento 
Area = Comprimento * Largura
Preço_total = Area * Preço_m2

# Impressão de dados (saída)
print(f"O terreno possui {Area}m2 e custa R${Preço_total:,.2f}.")
