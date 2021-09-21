def make_greeting(name):
    return 'Hi' + name + '!'


def computer (x , y):
    total = x+y
    if(total > 10): 
      total = 10
    return total 


def allow_access(person):
    if person == 'Dr Evil':
        answer = False
        return answer
    
make_greeting('Speedy')
computer(2,3)
computer(11,3)
allow_access('codie')
allow_access('Dr Evil')


print(make_greeting)



