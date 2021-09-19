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


#uma maneira mais eficiente de resolver isso, seria:

costs = 100.0
most_efective = 0

for i in range(len(best_solutions)):
    index = best_solutions[i]
    if  costs > cost[index]:
        most_efective = index
        costs = cost[index]
        
print('Solution', most_efective,
      'is the most effective with cost of', cost[most_efective])


