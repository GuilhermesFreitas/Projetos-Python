class Carro:
    def linha(self):
        print('-' * 70)

    def __init__(self, modelo, placa, cor, velocidade_max):
        # Inicialização
        self.modelo = modelo
        self.placa = placa
        self.cor = cor
        self.velocidade_min = 10
        self.velocidade_max = velocidade_max
        self.gasolina = 100
        self.esta_ligado = False
        self.esta_andando = False
        self.velocidade_atual = 0
        self.km_percorridos = 0

    def ligar(self):
        if self.esta_ligado:
            self.linha()
            print(f"{self.modelo} já está ligado.")
            self.linha()
        else:
            self.esta_ligado = True
            print(f"{self.modelo} foi ligado.")

    def desligar(self):
        if self.esta_ligado:
            self.esta_ligado = False
            self.linha()
            print(f"{self.modelo} foi desligado.")
            self.linha()
        else:
            print(f"{self.modelo} já está desligado.")

    def ajuste_velocidade(self, nova_velocidade):
        if self.esta_ligado:
            if self.velocidade_min <= nova_velocidade <= self.velocidade_max:
                self.velocidade_atual = nova_velocidade
                print(f"Velocidade ajustada para {
                      self.velocidade_atual:.2f} km/h.")
            else:
                print(f"Velocidade máxima excedida ou inválida! A velocidade máxima do {
                      self.modelo} é {self.velocidade_max} km/h e a mínima é {self.velocidade_min} km/h.")
        else:
            print(f"{self.modelo} precisa estar ligado para ajustar a velocidade.")

    def andar(self):
        if self.esta_ligado and self.gasolina > 0:
            if self.velocidade_atual > 0:
                consumo_por_km = 0.704
                distancia = self.velocidade_atual * 0.1
                consumo = distancia * consumo_por_km
                if self.gasolina >= consumo:
                    self.gasolina -= consumo
                    self.km_percorridos += distancia
                    self.linha()
                    print(f"{self.modelo} andou a {
                          self.velocidade_atual:.2f} km/h. Gasolina restante: {self.gasolina:.2f}%.")
                    print(f"Distância percorrida: {
                          self.km_percorridos:.2f} km.")
                    self.linha()
                else:
                    print(
                        f"{self.modelo} não tem gasolina suficiente para andar nessa velocidade.")
            else:
                print(f"{self.modelo} não pode andar a 0 km/h.")
        elif not self.esta_ligado:
            print(f"{self.modelo} precisa estar ligado para andar.")
        else:
            print(f"{self.modelo} está sem gasolina.")

    def posto_gasolina(self):
        if self.gasolina <= 30:
            self.linha()
            tanque = input(f"Seu tanque está em {
                           self.gasolina:.2f}%. Você deseja abastecer? (sim/não): ")
            self.linha()
            if tanque.lower() == 'sim':
                valor = float(
                    input("Digite a quantidade de gasolina que você quer abastecer: "))
                if valor > 100:
                    print("Esse valor excede o máximo do tanque.")
                elif (valor + self.gasolina) > 100:
                    print("Esse valor excede o tanque, por favor tente novamente.")
                else:
                    self.gasolina += valor
                    self.linha()
                    print(f"Seu {self.modelo} foi abastecido. Gasolina atual: {
                          self.gasolina:.2f}%.")
                    self.linha()
            else:
                print("Abastecimento cancelado.")
        else:
            print(f"Seu {self.modelo} ainda tem gasolina suficiente ({
                  self.gasolina:.2f}%).")


celta = Carro('Celta', 'JPL3K21', 'Preto', 160)
uno = Carro('Fiat Uno', 'LOP1K39', 'Branco', 140)
civic = Carro('Honda Civic', 'FRT5H84', 'Azul', 180)
corolla = Carro('Toyota Corolla', 'MLP2J76', 'Preto', 200)


civic.ligar()
civic.ajuste_velocidade(20)
civic.andar()
civic.andar()
civic.ajuste_velocidade(80)
civic.andar()
civic.andar()
civic.ajuste_velocidade(120)
civic.andar()
civic.andar()
civic.andar()
civic.andar()
civic.ajuste_velocidade(150)
civic.andar()
civic.andar()
civic.andar()
civic.andar()
civic.posto_gasolina()
civic.andar()
civic.andar()
civic.andar()
civic.andar()
civic.andar()
civic.ajuste_velocidade(180)
civic.andar()
civic.andar()
civic.andar()
civic.posto_gasolina()
civic.andar()
civic.andar()
civic.andar()
civic.andar()
civic.desligar()
