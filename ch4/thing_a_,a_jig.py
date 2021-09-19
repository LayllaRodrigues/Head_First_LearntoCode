characters = ['t','a', 'c', 'o']

output = ''
length = len(characters)
i = 0
while (i < length):
    output = output + characters[i]
    i = i + 1
    
length = length * -1
i = -2

while (i >= length):
    output = output + characters[i]
    i = i - 1
    
print(output)


#EXEMPLO DE LISTA VAZIA

empty_list = []

# Chamamos listas com itens de diferentes tipos de listas heterogêneas . Aqui está um:

heterogêneo = ['azul',verdadeiro, 13,5]


