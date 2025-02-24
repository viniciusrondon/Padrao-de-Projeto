class Carro:
    def dirigir(self):  
        pass

class CarroEsportivo(Carro):
    def dirigir(self):
        return "Dirigindo um carro esportivo!"
    
class CarroPopular(Carro):
    def dirigir(self):
        return 'Dirigindo um carro popular!'
    
class CarroFactory:
    def criar_carro(self,tipo):
        if tipo == 'esportivo':
            return CarroEsportivo()
        elif tipo == 'popular':
            return CarroPopular()
        else:
            raise ValueError("Tipo de carro não reconhecido.")
        
# Teste
factory = CarroFactory() 

carro = factory.criar_carro('esportivo') 
print(carro.dirigir()) 

carro = factory.criar_carro('popular') 
print(carro.dirigir())

mustang = factory.criar_carro(tipo = 'esportivo')
mustang.dirigir()