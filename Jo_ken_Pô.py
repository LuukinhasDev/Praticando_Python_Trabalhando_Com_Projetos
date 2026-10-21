import random

def restart():
    resposta = ['s', 'n']
    while True:
        escolha = input('Deseja jogar mais uma vez?[s/n] ').lower().strip()

        if escolha not in resposta:
            print('\nErro! Digite [s] para SIM ou [N] para NÃO.')
            print('-'*40)
            continue

        return escolha

def pedra_papel_tesoura():
    print('============ JO-KEN-PÔ ============')
    opcoes = ['pedra', 'papel', 'tesoura']

    while True:
        print('''
        \nQual será a sua jogada: 
        \n-> Pedra <-
        \n-> Papel <-
        \n-> Tesoura <-''')

        jogador = input('\nDigite sua escolha: ')
        computador = random.choice(opcoes)

        if jogador not in opcoes:
            print('\nErro! Escolha apenas: Pedra, Papel ou Tesoura')
            continue

        break


    print('='*30)
    print(f'Você escolheu: {jogador}:')
    print(f'O computador escolheu: {computador}')
    print('='*30)
    if computador == jogador:
        print('\nEMPATE!')

    elif (jogador == 'pedra' and computador == 'tesoura') or \
        (jogador == 'tesoura' and computador == 'papel') or \
        (jogador == 'papel' and computador == 'pedra'):
        
        print('\nVOCÊ VENCEU!')

    else:
        print('\nVOCÊ PERDEU!')

    print()

while True:
    pedra_papel_tesoura()
    recomeçar = restart()

    if recomeçar == 'n':
        break

print('Jogo Encerrado!')    


        