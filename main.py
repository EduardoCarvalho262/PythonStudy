from Pessoa import Pessoa
from Veterinario import Veterinario

eduardo = Pessoa("Eduardo", 19, "49891369874", 1.80)
marcelo = Veterinario("Celin", 19, "99999999989", 1.86, 15468, "Clinico Geral")


print(f'Olá meu nome {eduardo.get_nome()}')
print(f'Olá meu nome {marcelo.get_nome()} e sou {marcelo.get_cargo()} com RM: {marcelo.get_rm()}')

