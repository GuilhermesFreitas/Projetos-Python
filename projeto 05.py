class Agenda:
    def __init__(self):
        # Lista de amigos disponíveis para adicionar
        self.lista = ["Guilherme", "Emilly", "Isabella", "Igor", "Izabel", "Meire", "Ernandes"]
        # Lista de amigos adicionados pelo usuário
        self.minha_lista = []

    def mostrar_lista(self):
        # Mostrar os amigos disponíveis e os amigos adicionados
        print("\nAmigos disponíveis:")
        for amigo in self.lista:
            print(amigo)
        print("\nSua lista de amigos:")  # \n serve para quebrar a linha
        if self.minha_lista:
            for amigo in self.minha_lista:
                print(amigo)
        else:
            print("Sua lista de amigos está vazia.")

    def adicionar_amigos(self):
        escolha = input("Deseja adicionar alguém à sua lista de amigos? (sim ou nao): ")

        if escolha.lower() == 'sim':
            self.mostrar_lista()  # Mostra a lista de amigos disponíveis
            amigo = input("Quem você quer adicionar à sua lista de amigos? ").capitalize()  # Corrige a caps
            # Verifica se o nome está na lista de amigos disponíveis
            if amigo in [nome.capitalize() for nome in self.lista] and amigo not in self.minha_lista:
                self.minha_lista.append(amigo)
                print(f"Você adicionou {amigo} à sua lista de amigos.")
            else:
                print(f"{amigo} não está na lista de amigos disponíveis ou já foi adicionado à sua lista.")
        else:
            print("Você não adicionou nenhum amigo.")

    def remover_amigos(self):
        escolha = input("Deseja remover alguém da sua lista de amigos? (sim ou não): ")

        if escolha.lower() == "sim":
            self.mostrar_lista()
            if self.minha_lista:  # Verifica se há amigos na lista antes de tentar remover
                remover = input("Quem você deseja remover da sua lista de amigos? ").capitalize()  # Corrige a caps
                if remover in self.minha_lista:
                    self.minha_lista.remove(remover)
                    print(f"Você removeu {remover} da sua lista de amigos.")
                else:
                    print(f"{remover} não está na sua lista de amigos.")
            else:
                print("Sua lista de amigos está vazia. Não há nada para remover.")
        else:
            print("Você não removeu ninguém da sua lista.")


# Criação da agenda e interação com o usuário
agenda = Agenda()

# Loop para o usuário poder adicionar e remover amigos várias vezes
while True:
    print("\n--- Menu da Agenda ---")
    print("1. Adicionar amigo")
    print("2. Remover amigo")
    print("3. Mostrar lista de amigos")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        agenda.adicionar_amigos()
    elif opcao == '2':
        agenda.remover_amigos()
    elif opcao == '3':
        agenda.mostrar_lista()
    elif opcao == '4':
        print("Saindo da agenda...")
        break
    else:
        print("Opção inválida. Tente novamente.")