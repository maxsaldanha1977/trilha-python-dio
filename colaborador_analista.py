from abc import ABC, abstractmethod

# Classe abstrata para padronizar colaboradores
class Colaborador(ABC):
    @abstractmethod
    def exibir_info(self):
        pass

# Classe concreta para Analista
class Analista(Colaborador):
    def __init__(self, nome):
        self.nome = nome

    def exibir_info(self):
        return f"Analista: {self.nome}"

nome_analista = input()
analista = Analista(nome_analista)
print(analista.exibir_info())
