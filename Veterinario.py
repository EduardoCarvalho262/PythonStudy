from Pessoa import Pessoa


class Veterinario(Pessoa):

    def __init__(self, nome, idade, cpf, altura, rm, cargo):
        super().__init__(nome, idade, cpf, altura)
        self.__rm = rm
        self.__cargo = cargo

    def get_rm(self):
        return self.__rm

    def set_rm(self, novo_rm):
        self.__rm = novo_rm

    def get_cargo(self):
        return self.__cargo

    def set_rm(self, novo_cargo):
        self.__cargo = novo_cargo



