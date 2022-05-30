from aluno import Aluno


class AlunoPosGraduacao(Aluno):
    def __init__(self, cpf: int, dias_de_emprestimo: int, matricula: int):
        self.__elaborando_tese = None
        super().__init__(cpf, dias_de_emprestimo, matricula)

    @property
    def elaborando_tese(self):
        return self.__elaborando_tese

    @elaborando_tese.setter
    def elaborando_tese(self, elaborando_tese: bool):
        self.__elaborando_tese = elaborando_tese
        if self.__elaborando_tese == True:
            self.dias_de_emprestimo *= 2

    def emprestar(self, titulo_livro: str):
        return "Aluno de matricula " + '"' + str(self.matricula) + '"' + " " + super().emprestar(titulo_livro)

