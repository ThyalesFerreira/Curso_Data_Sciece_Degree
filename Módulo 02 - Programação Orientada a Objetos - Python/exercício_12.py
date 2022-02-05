# 12.	Enunciado
# Crie uma classe Data cujos atributos são dia, mês e ano. Implemente métodos _ repr _ e para comparação:
# igualdade (==) e desigualdades (!=, <=, >=, < e >).

class Data:
    def __init__(self, dia, mes, ano):
        '''
        Cria uma data
        '''
        self.dia = dia
        self.mes = mes
        self.ano = ano


    def data(self):
        '''
        Método criado para agrupar dia, mês e ano para comparar as datas.

        '''
        return self.dia+self.mes+self.ano

    def __repr__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'

    def __lt__(self, other):
        '''
        Verifica se a data é menor que a outra data passada por parâmetro
        '''
        return self.data() < other.data()

    def __le__(self, other):
        '''
        Verifica se a data é menor ou igual a outra passada por parâmetro
        '''

        return self.data() <= other.data()

    def __gt__(self, other):
        '''
        Verifica se a data é maior que a outra passada por parâmetro
        '''
        return self.data() > other.data()

    def __ge__(self, other):
        '''
        Verifica se a data é maior ou igual a outra passada por parâmetro
        '''
        return self.data() >= other.data()

    def __lt__(self, other):
        return self.data() < other.data()


    def __eq__(self, other):
        return self.data() == other.data()


data1 = Data(dia='12', mes='01', ano='2005')
data2 = Data(dia='12', mes='01', ano='2005')

print(data1.data())

print(data1 == data2)