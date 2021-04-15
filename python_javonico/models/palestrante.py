from typing import List
from .palestra import Palestra


class Palestrante:
    __codigo: str = None
    __nome: str = None
    __palestras: List[Palestra] = None

    def __init__(self, codigo, nome, palestras):
        self.__codigo = codigo
        self.__nome = nome
        self.__palestras = palestras

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, value):
        self.__codigo = value

    def get_nome(self):
        return self.__nome

    def set_nome(self, value):
        self.__nome = value

    def get_palestras(self):
        return self.__palestras

    def set_palestras(self, value):
        self.__palestras = value

    def imprimir(self):
        print("----------------------------")
        print("Imprimindo Palestrante")
        print("----------------------------")
        print(f"Código: {self.__codigo}")
        print(f"Nome: {self.__nome}")
        for palestra in self.__palestras:
            print(f"Palestra:")
            palestra.imprimir()
