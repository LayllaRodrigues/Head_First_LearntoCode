def get_bark(weight):
    if weight > 20: 
        return 'WOOF WOOF'
    
    else:
        return 'woof woof'

codie_bark = get_bark(40)
print("codie bark is", codie_bark)