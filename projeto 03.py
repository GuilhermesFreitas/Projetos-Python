import random as r


def linha():
    print('-' * 50)


while True:  # para que o numero aleatorio fosse gerado apenas uma vez foi criado um outro while true
    try:
        linha()
        print("         JOGO DA ADIVIAÇÃO       ")
        linha()
        num = range(1, 11)  # Define o intervalo de números de 1 a 10
        num_a = r.choice(num)  # Número aleatório gerado uma vez
        # Mensagem para o jogador
        print("Um número foi escolhido entre 1 e 10.")

        while True:  # Loop para tentativas do jogador
            # Entrada do usuário
            E = int(input(f"Digite um número de 1 a 10: "))

            if E < 1 or E > 10:
                print("Por favor, digite um número de 1 a 10.")
                continue  # Se o número estiver fora do intervalo, continua para a próxima iteração

            if E > num_a:
                print("Tente um número mais baixo...")
            elif E < num_a:
                print("Tente um número mais alto...")
            elif E == num_a:
                linha()
                print(f"Parabéns!!! Você ganhou! A resposta era {num_a}")
                linha()
                break  # Sai do loop de tentativas

    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro de 1 a 10.")