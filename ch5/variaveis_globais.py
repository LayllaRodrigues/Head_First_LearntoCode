# #variaveis globais sao visiveis tanto dentro, quanto fora das funcoes. Para usar uma variavel no python, primeiro preciso informar que usarei com a palavra chave GLOBAL

# #Lets Go!

# greeting = 'Greetings'

# def greet(name, message):
#     global greeting
#     print(greeting, name + ' . ', message)
    
# greet('June', 'See you soon!')

#Tbm é possivel alterar o valor de uma variável global em sua funcao se quiser 
#exemplo:

greeting = 'Greetings'

def greet(name, message):
    global greeting
    print(greeting, name + '. ', message)
    greeting = 'hi'
    
greet('June', 'See you soon!')
print(greeting)