# hair = input ("what color hair [brown]? ")
# if hair == '':
#     hair = 'brown'
# print('you chose', hair)


# hair_lenght = input(" what hair lenght [short]? ")
# if hair_lenght == '':
#     hair_lenght = 'short'
# print('you chose, ', hair_lenght)


# eyes = input("what eye color [blue]?")
# if eyes == '':
#     eyes = 'blue'
# print('you chose', eyes)

# gender = input ("what gender [female]?")
# if gender == '':
#     gender = 'female'
# print('you chose', gender)

# has_glasses = input("Has glasses [no]?")
# if has_glasses == '':
#     has_glasses = 'no'
# print('you chose', has_glasses)

# has_beard = input("Has beard [no]?")
# if has_beard == '':
#     has_beard = 'no'
# print('You chose', has_beard)

##Temos duas coisas que variam em cada bit de codio: a pergunta e o valor padrao. Esses serao nossos parametros porque cada bez que chamamos nossa funcao, eles sao diferentes, vamos comecar por ai: 
#1. definindo a funcao com 2 parametros
#2. criar string que atue como pergunta, para que possamos solicitar e obter a entrada do usuario
#3. verificar se o usuario escolheu o valor padrao (nesse caso a string retorna vazia) Em seguida, precisamos imprimir a escolha
#4. obter a resposta de volta para o código que chamava  get_attribute com return 
#5. para cada atributo precisamos escrever a chamada apropriada para a funcao 

def get_attribute(query, default):
    question = query + ' [' + default + ']? '
    answer = input(question)
    if (answer == ''):
        answer = default
    print('You chose', answer)
    return answer

hair = get_attribute('what hair color', 'brown')
hair_lenght = get_attribute('what hair length', 'short')
eyes = get_attribute('what eye color', 'blue')
gender = get_attribute('what gender', 'female')
has_glasses = get_attribute('has_glasses', 'no')
has_beard = get_attribute('has beard', 'no')
