import random

n = random.randint(1, 10)

while True: 
    palpite = int(input("Adivinhe o número entre 1 e 10: "))
    if palpite > n:
        print("Muito alto, tente novamente!")
    elif palpite < n:
         print("Muito baixo, tente novamente!")
    else:
        print("Correto!")
        break
