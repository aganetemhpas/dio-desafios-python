class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def __str__(self):
        return self.placa
    
    def ligar_motor(self):
        print("Ligando Motor")

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado
    

    1
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")
    

#moto = Motocicleta("preta", "abc-1234", 2)
#print(moto)
#moto.ligar_motor()

#carro = Carro("branco", "xde-1234", 4)
#carro.ligar_motor()

caminhao = Caminhao("roxo", "gdd-1234", 8, True)
#caminhao.ligar_motor()
#caminhao.esta_carregado()
print(caminhao)