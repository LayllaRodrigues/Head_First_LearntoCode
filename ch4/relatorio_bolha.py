score = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69,
         34, 55, 51,52, 44, 51, 69, 64, 66, 55, 52, 61,
         46, 31, 57, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]


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

