import random

random_choice = random.randint(0 , 2)

if random_choice == 0:
    escolha_do_computador = 'Pedra'
elif random_choice == 1:
    escolha_do_computador = 'Papel'
else:
    escolha_do_computador = 'Tesoura'
    
    
escolha_do_usuario = input('Pedra, Papel ou Tesoura?' )

print('Vc escolheu ', escolha_do_usuario, 'e o computador escolheu ', escolha_do_computador)
    

