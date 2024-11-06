
class carro:  # classe carro
    # o init define os valores iniciais e inicia os atributos
    def __init__(self, modelo, placa, cor):
        self.modelo = modelo
        self.placa = placa
        self.cor = cor
        self.gasolina = 100
        self.esta_ligado = False
        self.esta_andando = False

    def ligar(self):
        if self.esta_ligado:
            print(f"{self.modelo} já está ligado")
        else:
            self.esta_ligado = True
            print(f"{self.modelo} foi ligado")

    def desligar(self):
        if self.esta_ligado:
            self.esta_ligado = False
            print(f"{self.modelo} foi desligado")
        else:
            print(f"{self.modelo} já está desligado")

    def andar(self):
        if self.esta_ligado and self.gasolina > 0:
            self.esta_andando = True
            self.gasolina -= 10
            print(f"{self.modelo} andou. Gasolina restante: {self.gasolina}%")
        elif not self.esta_ligado:
            print(f"{self.modelo} precisa estar ligado para andar")
        else:
            print(f"{self.modelo} está sem gasolina")

    def posto_gasolina(self):
        if self.gasolina <= 50:
            tanque = input(f"Seu tanque está em {
                           self.gasolina}%. Você deseja abastecer? (sim/não): ")
            if tanque.lower() == 'sim':
                valor = int(
                    input("Digite a quantidade de gasolina que você quer abastecer: "))

                if valor > 100:
                    print("Esse valor excede o máximo do tanque")
                elif (valor + self.gasolina) > 100:
                    print("Esse valor excede o tanque, por favor tente novamente")
                else:
                    self.gasolina += valor
                    print(f"Seu {self.modelo} foi abastecido. Gasolina atual: {
                          self.gasolina}%")
            else:
                print("Abastecimento cancelado")
        else:
            print(
                f"Seu {self.modelo} ainda tem gasolina suficiente ({self.gasolina}%).")


celta = carro('celta', 'JPL3K21', 'preto')
uno = carro('fiat uno', 'lop1k39', 'branco')
civic = carro('Honda Civic', 'FRT5H84', 'Azul')
corolla = carro('Toyota Corolla', 'MLP2J76', 'preto')

civic.ligar()
civic.andar()
civic.andar()
civic.andar()
civic.posto_gasolina()
civic.andar()
civic.andar()
civic.andar()
civic.andar()
civic.posto_gasolina()
civic.andar()
civic.andar()
civic.andar()
civic.andar()
civic.desligar()
