class Pessoa:

    def __init__(self, nome, idade, cpf, altura):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf
        self.__altura = altura

    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def get_idade(self):
        return self.__idade

    def set_idade(self, nova_idade):
        self.__idade = nova_idade

    def get_cpf(self):
        return self.cpf

    def set_cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    def get_altura(self):
        return self.__altura

    def set_altura(self, nova_altura):
        self.__altura = nova_altura