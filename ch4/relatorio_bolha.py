from ast import Index


score = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69,
         34, 55, 51,52, 44, 51, 69, 64, 66, 55, 52, 61,
         46, 31, 57, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]


cost = [.25, .27, .25, .25,.25,.25,
        .33, .31, .25, .29, .27, .22,
        .31, .25, .25, .33, .21, .25,
        .25, .25, .28, .25, .24, .25,
        .25, .25, .27, .25, .26, .29,]

high_score = 0
length = len(score)
for i in range(length):
        print('Bubble solution #' + str(i), 'score:', score[i])
        if score[i] > high_score:
            high_score = score[i]
            
print('Bubble tests:', length)
print('highest bubble score:', high_score)

best_solutions = []
for i in range(length):
    if  high_score == score[i]:
        best_solutions.append(i)
        
print('solutions with the highest score:', best_solutions)

# costs = 100.0
# most_efective = 0

# for i in range(length):
#     if score[i] == high_score and cost[i] < costs:
#         most_efective = i
#         costs = cost[i]
        
# print('Solution', most_efective,
#       'is the most effective with cost of', cost[most_efective])


#uma maneira mais eficiente de calcula a eficieia x custo da formula, seria:

costs = 100.0
most_efective = 0

for i in range(len(best_solutions)):
    index = best_solutions[i]
    if  costs > cost[index]:
        most_efective = index
        costs = cost[index]
        
print('Solution', most_efective,
      'is the most effective with cost of', cost[most_efective])

# #Listas são uma estrutura de dados para dados ordenados.

# Uma lista contém um conjunto de itens, cada um com seu próprio índice .

# As listas usam um índice baseado em zero, onde o primeiro item está no índice 0.

# Você pode usar a lenfunção para obter o número de itens em uma lista.

# Você pode acessar qualquer item usando seu índice. Por exemplo, use my_list[1]para acessar o segundo item da lista.

# Você também pode usar índices negativos para identificar itens começando no final da lista.

# Tentar acessar um item além do final da lista resultará em um erro de índice de tempo de execução.

# Atribuir um valor a um item existente mudará seu valor.

# Atribuir um valor a um item que não existe na lista resulta em um erro de tempo de execução de índice “fora dos limites”.

# Os itens da lista podem conter valores de qualquer tipo.

# Nem todos os valores em uma lista precisam ser do mesmo tipo.

# Listas que contêm valores de diferentes tipos são chamadas de heterogêneas.

# Você pode criar uma lista vazia com my_list = [ ].

# Você pode adicionar um novo valor a uma lista usando append.

# Você pode estender uma lista com os itens de outra lista com extend.

# Você pode criar uma nova lista a partir de duas listas existentes simplesmente adicionando-as com +.

# Use insertpara adicionar um novo item a um índice em uma lista existente.

# O forloop é comumente usado para iterar por meio de sequências, como listas.

# O whileloop é usado com mais frequência quando você não sabe quantas vezes precisa fazer o loop e está efetuando o loop até que uma condição seja atendida. O forloop é mais frequentemente usado quando você sabe o número de vezes que o loop precisa ser executado.

# A rangefunção cria um intervalo de inteiros.

# Você pode iterar em intervalos com o forloop.

# A strfunção converte um número em uma string.
