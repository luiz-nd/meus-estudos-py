class Carro:
    def __init__(self, marca, modelo, ano):
      
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0  

    def acelerar(self, velocidade):
        
        self.velocidade += velocidade
        print(f"O carro acelerou para {self.velocidade} km/h.")

    def frear(self, velocidade):
       
        self.velocidade -= velocidade
        if self.velocidade < 0:
            self.velocidade = 0  
        print(f"O carro freou para {self.velocidade} km/h.")

    def parar(self):
       
        self.velocidade = 0
        print("O carro parou. Velocidade atual: 0 km/h.")

    def mostrar_velocidade(self):
        
        print(f"A velocidade atual do carro é {self.velocidade} km/h.")

    def __str__(self):
        return f"Carro: {self.marca} {self.modelo} ({self.ano})"


meu_carro = Carro("Fiat", "Uno", 2015)


print(meu_carro)


meu_carro.acelerar(50)
meu_carro.mostrar_velocidade()
meu_carro.frear(20)
meu_carro.parar()