# 3) Você está desenvolvendo um sistema de admissão para um clube juvenil de jogos de tabuleiro. Escreva um programa em Python que
# pergunte ao usuário sua idade, se já jogou pelo menos 3 jogos de tabuleiro (resposta deve ser True ou False) e quantas vezes venceu
# um jogo. O programa deve imprimir True, permitindo o ingresso do participante no clube, se:
# tiver entre 16 e 18 anos
# já tiver jogado pelo menos 3 jogos
# já ter vencido pelo menos 1 jogo, 
# Sua expressão deve imprimir False caso contrário. Aqui está um exemplo de interação com seu código no terminal, com entradas de dados
# destacadas em negrito e as impressões de seu código em itálico (apenas para facilitar sua visualização).
# Digite sua idade: 17
# Já jogou pelo menos 3 jogos de tabuleiro? True
# Quantos jogos já venceu? 2
# Apto para ingressar no clube de jogos de tabuleiro: True

# Leitura dos dados (entrada)
Idade_usuario =  int(input("Qual é a sua idade? "))
ja_jogou_jogos = input("Já jogou pelo menos 3 jogos de tabuleiro? (true ou false) ")
vzs_venceu_jogo =  int(input("Quantas vezes venceu um jogo? "))

# Processamento
resposta_jogos = ja_jogou_jogos == "true" or not ja_jogou_jogos == "false"
resposta_idade = Idade_usuario >= 16 or Idade_usuario <= 18 and not Idade_usuario <= 15 or Idade_usuario >= 19 
resposta_quant_jogos = vzs_venceu_jogo >= 1 and not vzs_venceu_jogo < 1
permiçao = {resposta_idade} or {resposta_jogos} or {resposta_quant_jogos} == True

# Impressão de dados (saída)
print(resposta_idade)
print(resposta_jogos)
print(resposta_quant_jogos)
print("Apto para ingressar no clube de jogos de tabuleiro: ")
print(permiçao)
