from abc import abstractmethod
from usuario_bu import UsuarioBU


class Aluno(UsuarioBU):
    @abstractmethod
    def __init__(self, cpf: int, dias_de_emprestimo: int, matricula: int):
        super().__init__(cpf, dias_de_emprestimo)
        if isinstance(matricula, int):
            self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula: int):
        self.__matricula = matricula

    def emprestar(self, titulo_livro: str):
        return super().emprestar(titulo_livro)

    def devolver(self, titulo_livro: str):
        return "Aluno de matricula " + '"' + str(self.__matricula) + '"' + " " + super().devolver(titulo_livro)

