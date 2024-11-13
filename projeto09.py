import random
from rich import print

# Configurações iniciais do jogo
nome_jogador = input("Digite seu nome ou apelido: ")
lista = ["Inspiração", "Constelação", "Lúdico", "Serendipidade", "Euforia",
         "Labirinto", "Sutileza", "Introspecção", "Equilíbrio", "Horizonte"]
palavra_aleatoria = random.choice(lista).lower()
letras = len(palavra_aleatoria)
tentativas = 10
letras_acertadas = []  # Lista para armazenar letras acertadas

print("[red]\nJogo da forca[/red]")
print(f"{nome_jogador}, você tem seis chances para acertar. Boa sorte!")
print(f"A palavra tem {letras} [blue]letras.[/blue]")

# Loop de tentativas
for cada in range(tentativas):
    letra_jogador = input(
        f"\nTentativa {cada + 1}/{tentativas}: Escolha uma letra: ").lower()

    if letra_jogador in palavra_aleatoria:
        print(f"A letra '{letra_jogador}' está na palavra!")
        letras_acertadas.append(letra_jogador)
    else:
        print(f"A letra '{letra_jogador}' não está na palavra.")

    # Mostrar o progresso do jogador na palavra
    progresso = [
        letra if letra in letras_acertadas else "_" for letra in palavra_aleatoria]
    print("Progresso: ", " ".join(progresso))

    # Verifica se o jogador adivinhou todas as letras
    if all(letra in letras_acertadas for letra in palavra_aleatoria):
        print("[green]\nParabéns! Você adivinhou a palavra corretamente![/green]")
        break
else:
    # Permitir que o jogador chute a palavra completa após as tentativas
    chute = input(
        "\nSuas tentativas acabaram. Qual é a palavra completa? ").lower()
    if chute == palavra_aleatoria:
        print("[green]Parabéns! Você acertou a palavra![/green]")
    else:
        print("[red]Não foi dessa vez. A palavra correta era:[/red]",
              palavra_aleatoria)
