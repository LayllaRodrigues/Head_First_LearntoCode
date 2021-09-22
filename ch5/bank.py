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

#####RESUMO DA AULA###

# As funções nos fornecem uma maneira de empacotar, abstrair e reutilizar o código.
# Uma função tem um nome, zero ou mais parâmetros e um corpo.
# Você chama ou invoca uma função e passa zero ou mais argumentos.
# Você pode transmitir a uma função Python qualquer valor Python válido.
# O número e a ordem dos argumentos em uma chamada de função precisam corresponder aos parâmetros da função. Você pode usar argumentos de palavra-chave para especificar um subconjunto de argumentos em uma ordem arbitrária.
# Quando uma função é chamada, ela atribui os argumentos às variáveis ​​de parâmetro e, em seguida, executa seu bloco de código.
# O bloco de código de uma função também é conhecido como corpo da função.
# As funções podem retornar valores usando a instrução return.
# Para capturar o valor retornado de uma função, simplesmente atribua o resultado da chamada a uma variável.
# As funções podem chamar funções integradas ou outras funções que você definiu.
# Você pode declarar funções em qualquer ordem, desde que sejam definidas antes de serem chamadas.
# Você pode criar variáveis ​​locais dentro de uma função.
# Variáveis ​​locais existem apenas enquanto a execução da função existe.
# Os locais em seu código onde uma variável é visível definem seu escopo.
# Variáveis ​​que não são criadas dentro de funções são chamadas de variáveis ​​globais.
# Os parâmetros de uma função são tratados como variáveis ​​locais no corpo da função.
# Quando nomeamos um parâmetro com o mesmo nome de uma variável global, dizemos que esse parâmetro está ocultando a variável global.
# A palavra-chave global é usada dentro de uma função para indicar que você gostaria de se referir a uma variável global no corpo da função.
# A abstração do código geralmente torna seu código mais legível, bem estruturado e de fácil manutenção.
# A abstração do código também permite que você se concentre em um nível superior e esqueça os detalhes de baixo nível que uma função implementa.
# O retrabalho do código costuma ser chamado de refatoração.
# Você pode usar padrões de parâmetro para fornecer valores padrão para argumentos ausentes.
# Você pode usar nomes de parâmetro como argumentos de palavra-chave ao chamar uma função.