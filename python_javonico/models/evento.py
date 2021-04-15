from typing import List
from .palestra import Palestra
from .palestrante import Palestrante


class Evento:
    __palestras: List[Palestra] = None
    __palestrantes: List[Palestrante] = None

    def __init__(self, palestras=None, palestrantes=None):
        if palestras:
            self.__palestras = palestras
        if palestrantes:
            self.__palestrantes = palestrantes

    def get_palestras(self):
        return self.__palestras

    def set_palestras(self, palestras: List[Palestra]):
        self.__palestras = palestras

    def get_palestrantes(self):
        return self.__palestrantes

    def set_palestrantes(self, palestrantes: List[Palestrante]):
        self.__palestrantes = palestrantes

    def add_palestra(self, palestra: Palestra) -> None:
        if not self.__palestras:
            self.__palestras = []
        self.__palestras.append(palestra)

    def obter_palestra(self, codigo: str) -> Palestra:
        for palestra in self.__palestras:
            if palestra.get_codigo() == codigo:
                return palestra
        raise Exception("Palestra não encontrada")

    def add_palestrante(self, palestrante: Palestrante) -> None:
        if not self.__palestrantes:
            self.__palestrantes = []
        self.__palestrantes.append(palestrante)

    def obter_palestrante(self, codigo: str) -> Palestrante:
        for palestrante in self.__palestrantes:
            if palestrante.get_codigo() == codigo:
                return palestrante
        raise Exception("Palesntrante não encontrado")

    def imprimir(self):
        print("----------------------------")
        print("Imprimindo Evento")
        print("----------------------------")

        for i, palestra in enumerate(self.__palestras, start=1):
            print(f"Imprimindo palestra #{i} do evento")
            palestra.imprimir()

        for i, palestrante in enumerate(self.__palestrantes, start=1):
            print(f"Imprimindo palestrante #{i} do evento")
            palestrante.imprimir()
