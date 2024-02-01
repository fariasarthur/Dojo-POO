
class Elevador:

    def __init__(self, andar_atual:int, andar_desejado:int):
        self.andar_atual = andar_atual
        self.andar_desejado = andar_desejado
        self.pavimentos = [1,2,3,4,5,6,8,9,10,11,12,13,14]

    def chamar(self):
        print('Aguarde um momento')
        print('..................')
        print('  Porta Fechada'   )
        print('       -||-       ')
        print('  Porta Aberta    ')
        print('-|              -|')

        if self.andar_desejado not in self.pavimentos:
            print('Esse andar não existe no prédio')
        
        else:
            print('Andar escolhido: ' + str(self.andar_desejado))

    def transitar(self):

        if self.andar_atual > self.andar_desejado:
            print('Elevador descendo para o ' + str(self.andar_desejado) + 'º andar')

        else:
            print('Elevador subindo para o ' + str(self.andar_desejado) + 'º andar')
    
        