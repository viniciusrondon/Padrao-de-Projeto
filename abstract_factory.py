from abc import ABC, abstractmethod

class Interior:
    def tipo_interior(self):
        pass

class InteriorEsportivo(Interior):
    def tipo_interior(self):
        return "Estofado de couro esportivo."
    
class InteriorPopular(Interior):
    def tipo_interior(self):
        return "Estofado de tecido."
    
class CarroFactory(ABC):
    @abstractmethod
    def criar_interior(self):
        pass

    def criar_rodas(self):
        return "Rodas esportivas"

class CarroEsportivoFactory(CarroFactory):
    def criar_interior(self):
        return InteriorEsportivo()

    def criar_rodas(self):
        return "Rodas esportivas"


class CarroPopularFactory(CarroFactory):
    def criar_interior(self):
        return InteriorPopular()

    def criar_rodas(self):
        return "Rodas comuns"

esportivo_factory = CarroEsportivoFactory()
popular_factory = CarroPopularFactory()

# Teste
def cliente(factory: CarroFactory):
    interior = factory.criar_interior()
    rodas = factory.criar_rodas()
    print(f"Interior: {interior.tipo_interior()} | Rodas: {rodas}")


cliente(esportivo_factory)
cliente(popular_factory)