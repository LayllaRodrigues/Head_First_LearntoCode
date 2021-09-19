#listar elementos em array

smoothies = ['coconut', 'strawberry', 'banana', 'pineapple', 'açai berry']


#Como acessar elementos da lista
#Cada elemento da lista possui um indice, e essa é a chave para acessar os valores em uma lista.

#EXEMPLO:

favorites = smoothies[4]

#Tambem é possivel alterar o valor de um item na lista usando o indice

smoothies[3] = 'tropical'


#QUÃO GRANDE É ESSA LISTA?

    #Digamos que alguem lhe entregue uma lista grande com dados, vc sabe como obter o tamanho dela? 
    #O python fornece uma função integrada oara informa-lo, ela é chamada de LEN 
    
#EXEMPLO DE COMO USAR FUNCAO LEN:

length = len (smoothies)

#Imprimindo valores

print   (length)
print   (smoothies)
print   (favorites)

#Acessando ultimo item da lista: as listas geralmente têm dados organizados com 
# os valores mais recentes, e geralmente os mais importantes, no final (ou seja, 
# no maior índice), portanto, acessar o último item da lista é uma tarefa comum.

#Para obter o último item de nossa lista de smoothies, fazemos o seguinte:

length = len(smoothies)
last = smoothies[length-1]
print(last)

#Python oferece outra forma de acessar o ultimo item da lista:
#você pode usar um índice negativo, começando em –1, para especificar os itens 
# em uma lista na ordem inversa. Portanto, um índice de –1é o último item da lista,
# um índice de –2é o penúltimo e assim por diante.

#EXEMPLO:
last = smoothies[-1]
second_last = smoothies[-2]
third_last = smoothies[-3]
print(last)
print(second_last)
print(third_last)









