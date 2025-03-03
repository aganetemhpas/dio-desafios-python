class Cachorro:
    
    # Construtor __init__
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    # Destrutor __del__
    def __del__(self):
        print("Destruindo a instância")
    
    def falar(self):
        print("Auau")



c = Cachorro("Chappie", "amarelo")

c.falar()

print("Ola mundo")

del c # força a remoção da classe

print("Ola mundo")
print("Ola mundo")
print("Ola mundo")