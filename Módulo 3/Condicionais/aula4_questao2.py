# 2) Você está criando um sistema de classificação de filmes com base nas avaliações dos usuários. Escreva um programa em Python 
# que solicita ao usuário para inserir a avaliação de um filme em uma escala de 1 a 5. O programa deve imprimir uma mensagem 
# correspondente à classificação do filme:
# Se a avaliação for 5, imprima "Excelente!"
# Se a avaliação for 4, imprima "Muito Bom!"
# Se a avaliação for 3, imprima "Bom!"
# Se a avaliação for 2, imprima "Regular."
# Se a avaliação for 1, imprima "Ruim."

# Leitura dos dados (entrada)
classificação = int(input("Insira a avaliação de um filme em uma escala de 1 a 5: "))

# Processamento
if classificação == 5:
    print("Excelente")
if classificação == 4:
    print("Muito bom!")
if classificação == 3:
    print("Bom!")
if classificação == 2:
    print("Regular")
if classificação == 1:
    print("Ruim")

# Impressão de dados (saída)
