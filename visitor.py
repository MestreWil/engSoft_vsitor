from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class InterfaceVisitor(ABC):

    @abstractmethod
    def aceita(self, visitor: Visitor) -> None:
        pass


class Componente_concreto_a(InterfaceVisitor):
    
    def aceita(self, visitor: Visitor) -> None:
        
        visitor.visita_a_objeto_a(self)

    def metodo_exclusivo_do_componente_a(self) -> str:
        

        return "Carro Flex"


class Componente_concreto_b(InterfaceVisitor):
    

    def aceita(self, visitor: Visitor):
        visitor.visita_o_objeto_b(self)

    def metodo_exclusivo_do_componente_b(self) -> str:
        return "Carro somente a Gasolina"

class Visitor(ABC):
    
    @abstractmethod
    def visita_a_objeto_a(self, element: Componente_concreto_a) -> None:
        pass

    @abstractmethod
    def visita_o_objeto_b(self, element: Componente_concreto_b) -> None:
        pass

class Componente_visitor_1(Visitor):
    def visita_a_objeto_a(self, element) -> None:
        print(f"{element.metodo_exclusivo_do_componente_a()} + Componente_visitor_1")

    def visita_o_objeto_b(self, element) -> None:
        print(f"{element.metodo_exclusivo_do_componente_b()} + Componente_visitor_1")


class Componente_visitor_2(Visitor):
    def visita_a_objeto_a(self, element) -> None:
        print(f"{element.metodo_exclusivo_do_componente_a()} + Componente_visitor_2")

    def visita_o_objeto_b(self, element) -> None:
        print(f"{element.metodo_exclusivo_do_componente_b()} + Componente_visitor_2")


def codigo_cliente(componentes: List[InterfaceVisitor], visitor: Visitor) -> None:
  
    for componente in componentes:
        componente.aceita(visitor)

if __name__ == "__main__":
    componentes = [Componente_concreto_a(), Componente_concreto_b()]

    print("O código do cliente funciona com todos os visitors por meio da interface base do Visitor:")
    visitor1 = Componente_visitor_1()
    codigo_cliente(componentes, visitor1)

    print("Permite que o mesmo código do cliente funcione com diferentes tipos de visitors:")
    visitor2 = Componente_visitor_2()
    codigo_cliente(componentes, visitor2)