class Carro:
    def __init__(self, tipo_motor, cor, tipo_rodas):
        self.tipo_motor = tipo_motor
        self.cor = cor
        self.tipo_rodas = tipo_rodas

    def __str__(self):
        return f"Carro com motor{self.tipo_motor}, cor {self.cor}, e rodas {self.tipo_rodas}"
    
class CarroBuilder:
    def __init__(self):
        self.tipo_motor = None
        self.cor = None
        self.tipo_rodas = None

    def com_motor(self, tipo_motor):
        self.tipo_motor = tipo_motor
        return self
    
    def com_cor(self, cor):
        self.cor = cor
        return self
    
    def com_rodas(self, tipo_rodas):
        self.tipo_rodas = tipo_rodas
        return self
    
    def construir(self):
        return Carro(self.tipo_motor, self.cor, self.tipo_rodas)
    
# Teste
builder = CarroBuilder()

carro = builder.com_motor('1.4 TSI')
carro = builder.com_cor('Prata')
carro = builder.com_rodas('aro 16')

carro = builder.construir()

carro
