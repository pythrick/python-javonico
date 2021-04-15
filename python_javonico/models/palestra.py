

class Palestra:
    __codigo: str = None
    __tema: str = None
    __descricao: str = None

    def __init__(self, codigo: str, tema: str, descricao: str):
        self.set_codigo(codigo)
        self.set_tema(tema)
        self.set_descricao(descricao)

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, valor: str):
        self.__codigo = valor

    def get_tema(self):
        return self.__tema

    def set_tema(self, valor: str):
        self.__tema = valor

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, valor: str):
        self.__descricao = valor

    def imprimir(self):
        print("----------------------------")
        print("Imprimindo Palestra")
        print("----------------------------")
        print(f"Código: {self.__codigo}")
        print(f"Tema: {self.__tema}")
        print(f"Descrição: {self.__descricao}")

