import random

def generateRandomSolution():
    nation = [ 'Norwegian', 'Ukrainian', 'Englishman', 'Spaniard', 'Japanese' ]
    color  = [ 'Red', 'Blue', 'Yellow', 'Ivory', 'Green' ]
    drink  = [ 'Tea', 'Milk', 'Coffe', 'Orange juice', 'Water' ]
    smoke  = [ 'Lucky Strike', 'Old Gold', 'Kools', 'Chesterfield', 'Parliaments']
    pet    = [ 'Zebra', 'Fox', 'Horse', 'Snails', 'Dog' ]
    random.shuffle(nation)
    random.shuffle(color)
    random.shuffle(drink)
    random.shuffle(smoke)
    random.shuffle(pet)

    solution = []
    for i in range(5):
        sample = {'nation' : nation[i], 
                  'color'  : color[i], 
                  'drink'  : drink[i], 
                  'smoke'  : smoke[i], 
                  'pet'    : pet[i] }
        solution.append(sample)
    return solution

def randomInt(min, max):
    return int(random.randint(min, max))

def lastIndex(array):
    return len(array) - 1