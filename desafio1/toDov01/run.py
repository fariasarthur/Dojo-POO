from equipamento.elevador import Elevador

while (True):
    andar_desejado = int(input('Pense em um andar desejado: '))
    andar_atual = int(input('Qual seu andar atual: '))

    elevador = Elevador(andar_atual, andar_desejado)
    elevador.chamar()
    elevador.transitar()
    
    
    #print()
