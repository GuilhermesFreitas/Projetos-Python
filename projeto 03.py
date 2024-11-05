import random as r


def linha():
    print('-' * 50)


LIMITE_MIN = 0
LIMITE_MAX = 5  # adcionei limite maximo de tentativas.

linha()
nome = input("Digite seu nome:")
linha()
print(f"Então {nome}, você tem {LIMITE_MAX} tentativas!")
print(f"Boa sorte! {nome}")

while True:
    try:
        linha()
        print(" JOGO DA ADIVIAÇÃO ")
        linha()
        num = range(1, 11)
        num_a = r.choice(num)
        print("Um número foi escolhido entre 1 e 10.")

        # definir que o numero maximo de tentativas são cinco
        for tentativas in range(LIMITE_MAX):
            E = int(input(f"Digite um número de 1 a 10: "))
            linha()

            if E < 1 or E > 10:
                print("Por favor, digite um número de 1 a 10.")
                continue

            if E > num_a:
                print("Tente um número mais baixo...")
            elif E < num_a:
                print("Tente um número mais alto...")
            elif E == num_a:
                linha()
                print(f"Parabéns!!! Você ganhou! A resposta era {num_a}")
                linha()
                break

        else:  # caso o loop de 5 tentativas acabe vai aparecer essa mensagem.
            linha()
            print(
                f"Você usou o numero maximo de tentativas.. o numero certo era {num_a}")
            linha()

    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro de 1 a 10.")
