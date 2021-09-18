import random

escolhas = ['Pedra', 'Papel', 'Tesoura']
escolha_do_computador= random.choice(escolhas)

    
escolha_do_usuario = input('Pedra, Papel ou Tesoura? ' )

if escolha_do_computador == escolha_do_usuario:
    vencedor = 'Empate'
elif escolha_do_computador == 'Papel' and escolha_do_usuario == 'Pedra':
    vencedor = 'Computer'
elif escolha_do_computador == 'Pedra' and escolha_do_usuario == 'Tesoura':
    vencedor = 'Computer'
elif escolha_do_computador == 'Tesoura' and escolha_do_usuario == 'Papel':
    vencedor = 'Computer'
else:
    vencedor = 'Usuario'

if vencedor == 'Empate':
    print('Escolhemos igual !', escolha_do_computador + ', Jogue novamente.')
else:
    print('O ' + vencedor , 'venceu!', ' o computador escolheu ' + escolha_do_computador)

