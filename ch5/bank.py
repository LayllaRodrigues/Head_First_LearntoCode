#Esse é o codigo de um hacker, quais sao os bugs dele?


balance = 10500
camera_on = True

def steal(balance, amount):
    global camera_on
    camera_on = False
    if(amount < balance):
        balance = balance - amount
        
        return amount
        camera_on = True
        
proceeds = steal (balance, 1250) #
print('Criminal: you stole', proceeds)

#BUGS:
#1. balance é uma variavel global, mas é sombreado pelo parâmetro
#2. por isso, quando se altera o saldo na funcao, não está alterando o saldo bancário real
#3. no return, estamos a devolver a quantia roubada
#4.  na linha 16,  não atualizamos  o saldo real da conta, por que que o saldo da conta bancária 
# é o mesmo que era originalmente 
#5. e, além de não roubar dinheiro, o criminoso esquece de ligar a câmera de volta, o que é uma doação 
# para a polícia de que algo nefasto está acontecendo. 
# lembre-se, quando você retorna de uma função a função deixa de executar para que quaisquer 
# linhas de código após o retorno sejam ignoradas

