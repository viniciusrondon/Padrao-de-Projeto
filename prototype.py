import copy


class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor

    def __str__(self):
        return f"Carro modelo {self.modelo}, cor {self.cor}"

    def clonar(self):
        return copy.deepcopy(self)


# Teste
carro_original = Carro("Fusca", "azul")
carro_clonado = carro_original.clonar()
carro_clonado.cor = "preto"
print(carro_original)
print(carro_clonado)
