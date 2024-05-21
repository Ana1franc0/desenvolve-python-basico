# 4) Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete com base na distância e no peso 
# do pacote. Escreva um código que solicita a distância da entrega em quilômetros e o peso do pacote em quilogramas. O programa 
# deve calcular e imprimir o valor do frete de acordo com as seguintes regras:
# Distância até 100 km: R$1 por kg.
# Distância entre 101 e 300 km: R$1.50 por kg.
# Distância acima de 300 km: R$2 por kg.
# Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg

# Leitura dos dados (entrada)
distancia = int(input("Qual é a distância da entrega em quilômetros: "))
peso = int(input("Qual é o peso do pacote em quilogramas: "))

# Processamento
if distancia <= 100:
    frete = peso
elif distancia >= 101 or distancia <= 300:
    frete = peso * 1,5
elif distancia > 300:
    frete = peso * 2
if peso > 10:
    frete + 10

# Impressão de dados (saída)
print(f"O valor do frete é {frete}")