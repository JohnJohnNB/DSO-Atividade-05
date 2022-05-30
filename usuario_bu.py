from abc import ABC, abstractmethod


class UsuarioBU(ABC):
    @abstractmethod
    def __init__(self, cpf: int, dias_de_emprestimo: int):
        if isinstance(cpf, int):
            self.__cpf = cpf
        if isinstance(dias_de_emprestimo, int):
            self.__dias_de_emprestimo = dias_de_emprestimo

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: int):
        self.__cpf = cpf

    @property
    def dias_de_emprestimo(self):
        return self.__dias_de_emprestimo

    @dias_de_emprestimo.setter
    def dias_de_emprestimo(self, dias_de_emprestimo: int):
        self.__dias_de_emprestimo = dias_de_emprestimo

    def emprestar(self, titulo_livro: str):
        return "pegou emprestado o livro: " +  titulo_livro + " com " + str(self.__dias_de_emprestimo) + " dias de prazo"

    def devolver(self, titulo_livro: str):
        return "devolveu o livro: "+titulo_livro

