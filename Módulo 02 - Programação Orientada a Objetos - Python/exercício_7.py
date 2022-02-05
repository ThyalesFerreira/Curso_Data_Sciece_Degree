# 7.	Crie uma modelagem de classes para uma agenda capaz de armazenar contatos.
# Através dessa agenda é possível incluir, remover, buscar e listar contatos já cadastrados.

class Agenda:
    def __init__(self):
        '''
        Cria uma agenda
        '''
        self.lista_contatos = []

    def incluir_contato(self, contato):
        '''
        Inclui um novo contato na agenda
        '''
        self.lista_contatos.append(contato)

    def remover_contato(self,contato):
        '''
        Remove um contato da agenda
        '''
        self.lista_contatos.remove(contato)

    def listar_contato(self):
        '''
        Exibe os contatos da agenda
        '''
        for contato in self.lista_contatos:
            print(contato.nome,",", contato.telefone)

class Contato:
    def __init__(self, nome, telefone):
        '''
        Cria um contato
        :param nome: str
        :param telefone: str
        '''
        self.nome = nome
        self.telefone = telefone

agenda = Agenda()

contato1 = Contato(nome='Thyales Ferreira', telefone='(31) 9-8661-3333')
contato2 = Contato(nome='Karina Soares', telefone='(31) 9-8661-5555')
contato3 = Contato(nome='Karina Silva', telefone='(31) 9-8661-4444')

agenda.incluir_contato(contato1)
agenda.incluir_contato(contato2)
agenda.incluir_contato(contato3)

agenda.remover_contato(contato1)

agenda.listar_contato()