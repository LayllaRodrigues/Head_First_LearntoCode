import random

escolhas = ['Pedra', 'Papel', 'Tesoura']
escolha_do_computador= random.choice(escolhas)

escolha_do_usuario = ''

while (escolha_do_usuario != 'Pedra' and  
            escolha_do_usuario != 'Papel' and
            escolha_do_usuario != 'Tesoura'):
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
    
    
    
    
 #-----------------------------------------------------------------------------------------------   
    
    #Sobre o conteudo da aula

#Muitos programas usam números aleatórios.
# Praticamente todas as línguas fornecem um meio de gerar números aleatórios.
# Python fornece um módulo aleatório para gerar números aleatórios.
# Use a instrução import para incluir a funcionalidade aleatória do Python em seu código.
# O tipo de dados booleano possui dois valores, True e False .
# Expressões booleanas ou condicionais são avaliadas como True ou False .
# Operadores relacionais, como ==, > e < , comparam dois valores.
# Operadores relacionais são fornecidos para números e strings.

# As expressões booleanas fornecem a base da instrução if .
# A instrução if avalia uma expressão booleana e, se True , executa um bloco de código.
# Um bloco de código é um conjunto de instruções Python que são executadas juntas.
# Os blocos de código são seções recuadas de código.
# A palavra-chave elif pode ser usada para testar condicionais adicionais em uma instrução if .
# A palavra-chave elif é uma contração de "else if".
# A palavra-chave else pode ser usada para fornecer uma alternativa final ou abrangente para uma instrução if .
# As expressões booleanas podem ser combinadas com os operadores booleanos e e ou .
# O operador booleano não pode ser usado para negar uma expressão ou valor booleano.
# A instrução while avalia uma expressão booleana e executa um bloco de código enquanto a expressão permanece True .
# Chamamos uma string sem caracteres de uma string vazia .
# Você usa = para atribuição e == para teste de igualdade.
# Você pode adicionar comentários ao seu código usando o caractere hash (#) seguido por um texto arbitrário.
# É uma boa ideia usar comentários para adicionar documentação ao seu código para que você possa se lembrar de suas decisões de design posteriormente (ou para que outros possam entender seu código).
# Antecipar o erro do usuário é uma parte importante do projeto de um programa centrado no usuário, como um jogo.
# Erros de lógica podem levar a loops infinitos.