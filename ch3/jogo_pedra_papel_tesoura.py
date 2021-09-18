import random

escolhas = ['Pedra', 'Papel', 'Tesoura']
escolha_do_computador= random.choice(escolhas)

    
escolha_do_usuario = input('Pedra, Papel ou Tesoura?' )

print('Vc escolheu ', escolha_do_usuario, 'e o computador escolheu ', escolha_do_computador)
    

