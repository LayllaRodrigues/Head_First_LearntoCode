#Replicando itens em uma lista

mistery = ['secret'] * 5
print (mistery)

#Replicando itens 

mistery1 = ' secret ' * 5
print (mistery1)

menu=[]
menu.append('burguer')
menu.append('sushi')
print(menu)

#EXCLUINDO ITENS DA LISTA

del menu[0]
print (menu)

#adicione uma lista a outra
menu.extend(['bbq', 'tacos'])
print (menu)

#insira itens em sua lista
# Digamos que você realmente precise adicionar um item no meio da sua lista.
# Use a insertfunção para fazer isso.

menu.insert([1, 'pizza'])
print (menu)

