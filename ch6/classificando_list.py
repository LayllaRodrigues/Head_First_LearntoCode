# O loop externo representa cada passagem no algoritmo. 
# O loop interno passa por cada item da lista e executa as comparações (e qualquer troca necessária). 
# Com isso em mente, vamos dar uma olhada:

# PSEUDOCODIGO - classifica a lista em ordem crescente:

# # define a function 
# def bubble_sort(list):
#     # declare a variable 
#     swapped and set to True
#     while swapped to False.
#     # For variable i in range(0, len(list)- I)
            # IF list[i] > list[i+I]:
            #         DECLARE  a variable temp and set to list[i].
            #         SET list[i] to list[i+I]
            #         SET list[i + I] to temp
            #         SET swapped to True.
            
            # bug:
for i in range(0, 4):
    for j in range(0,4):
        print(i * j)
        
# bug:

                     
for word in ['ox', 'cat', 'lion', 'tiger', 'bobcat']:
    for i in range(2,7):
        letters = len(word)
        if(letters % i) == 0:
            print(i, word)
            
full = False

donations = []
full_load = 45

toys = ['robot', 'doll', 'ball', 'slinky']

while not full:
    for toy in toys:
        donations.append(toy)
        size = len(donations)
        if (size >= full_load):
            full = True 
            
print('Full with', len(donations), 'toys')
print(donations)

                    
    
    
    
