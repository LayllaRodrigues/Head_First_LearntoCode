import random

number_of_scoops = random.randint(0,3)

if number_of_scoops == 0:
    print("you didn't want any ice cream?")
    print ('We have lots of flavors.')
elif number_of_scoops == 1:
    print('A single scoop for you, coming up.')
elif number_of_scoops == 2:
    print('Oh, two scoops for you')
elif number_of_scoops >=3:
    print("Wow, that's a lot of scoops!")
else:
    print("I'm sorry I can't give you negative scoops.")
    