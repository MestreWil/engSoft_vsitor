from abc import ABC, abstractmethod
from typing import List

class TaxaVisitorProtocolo(ABC):
    @abstractmethod
    def calcular_imposto_flex(self, carro):
        pass

    @abstractmethod
    def calcular_imposto_gasolina(self, carro):
        pass

class Tributacaobrazil(TaxaVisitorProtocolo):
    def calcular_imposto_flex(self, carro):
        return carro.preco + carro.preco * 0.07

    def calcular_imposto_gasolina(self, carro):
        return carro.preco + carro.preco * 0.13

class Carro(ABC):
    def __init__(self, nome="", preco=0.0):
        self.nome = nome
        self.preco = preco
    
    @property
    def nome(self):
        return self._nome
  
    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def preco(self):
        return self._preco
  
    @preco.setter
    def preco(self, value):
        self._preco = value

    @abstractmethod
    def preco_com_imposto(self, visitor: TaxaVisitorProtocolo):
        pass

class Carroflex(Carro):
    def __init__(self, nome='Carro Flex', preco=24500.00):
        super().__init__(nome, preco)

    def preco_com_imposto(self, visitor: TaxaVisitorProtocolo):
        return visitor.calcular_imposto_flex(self)

class Carrogasolina(Carro):
    def __init__(self, nome='Carro a Gasolina', preco=20000.00):
        super().__init__(nome, preco)

    def preco_com_imposto(self, visitor: TaxaVisitorProtocolo):
        return visitor.calcular_imposto_gasolina(self)

  


carroflex = Carroflex()
carroGas = Carrogasolina()
taxabrazil = Tributacaobrazil()
print(carroflex.nome)
print(carroflex.preco)
print(carroflex.preco_com_imposto(taxabrazil))
print(carroGas.nome)
print(carroGas.preco)
print(carroGas.preco_com_imposto(taxabrazil))