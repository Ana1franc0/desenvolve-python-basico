import random

def carrega_palavras():
    with open('gabarito_forca.txt', 'r', encoding='utf-8') as f:
        palavras = f.read().splitlines()
    return palavras

def carrega_estagios():
    with open('gabarito_enforcado.txt', 'r', encoding='utf-8') as f:
        estagios = f.read().strip().split('\n')
    return estagios

def escolhe_palavra(palavras):
    return random.choice(palavras)

def inicializa_palavra_escondida(palavra):
    return['-'] * len(palavra)

def imprime_palavra(palavra_escondida):
    print(' '.join(palavra_escondida))

def imprime_enforcado(erros, estagios):
    print(estagios[erros])

def jogo_da_forca():
    palavras = carrega_palavras()
    estagios = carrega_estagios()
    palavra = escolhe_palavra(palavras)
    palavra_escondida = inicializa_palavra_escondida(palavra)
    letras_erradas = []
    tentativas = 0
    max_tentativas = 6

    print("Bem-vindo ao jogo da forca!")
    print("Advinhe a palavra secreta:")
    imprime_palavra(palavra_escondida)

    while '_' in palavra_escondida and tentativas < max_tentativas:
        letra = input("\nDigite uma letra: ").strip().lower()
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, digite uma única letra válida.")
            continue
        if letra in palavra:
            for i, l in enumerate(palavra):
                if l == letra:
                    palavra_escondida[i] = letra
                    imprime_palavra(palavra_escondida)
                else:
                    if letra not in letras_erradas:
                        letras_erradas.append(letra) 
                        tentativas += 1
    imprime_enforcado(tentativas, estagios)
    print(f"Letras erradas até agora: {' '.join(letras_erradas)}")
    if '-' not in palavra_escondida:
        print("\nParabéns! Você acertou a palavra!")
    else:
        print("\nInfelizmente você perdeu. A palavra era:", palavra)
