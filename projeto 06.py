class Cadastro:
    def __init__(self):
        self.cadastros = []
        self.logar = False

    def linha(self):
        print("-" * 30)

    def registrar(self):
        self.linha()
        cad = input("Você deseja se cadastrar? (sim/não): ").strip().lower()
        self.linha()
        if cad == 'sim':
            nome = input("Digite seu nome completo: ").strip()
            sen = input("Digite sua nova senha: ").strip()

            # Validação para evitar duplicidade de nomes
            if any(user['nome'] == nome for user in self.cadastros):
                print("Este nome já está cadastrado.")
                return

            # Armazenando o cadastro
            self.cadastros.append({"nome": nome, "senha": sen})
            print("Seu cadastro foi realizado.")
        else:
            print("Você não criou um cadastro.")

    def login(self):
        if len(self.cadastros) > 0:
            nome = input("Digite seu nome: ").strip().capitalize()  
            senha = input("Digite sua senha: ").strip().capitalize()  

            # Verifica se o nome e senha estão corretos
            if any(user['nome'] == nome and user['senha'] == senha for user in self.cadastros):
                print("Seu login foi realizado com sucesso.")
                self.logar = True
            else:
                print("Nome ou senha incorretos.")
        else:
            print("Não há cadastros registrados. Cadastre-se primeiro.")

# Instanciando a classe Cadastro
cadastro = Cadastro()

# Menu interativo
while True:
    cadastro.linha()
    print("\n--- Menu ---")
    cadastro.linha()
    print("1. Cadastro")
    print("2. Login")
    print("3. Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == '1':
        cadastro.registrar()
    elif opcao == '2':
        cadastro.login()
    elif opcao == '3':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")