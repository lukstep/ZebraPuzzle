from utils import generateRandomSolution
from utils import lastIndex
from utils import randomInt

MUTATION_PROBABILITY = 19#  %
NUMBER_OF_RULES = 14
NUMBER_OF_HOUSES = 5
MAX_MUTATION_PROBABILITY = 100

key = ["nation", "color", "drink", "smoke", "pet"]


class Solution(object):
    def __init__(self):
        self.solution = generateRandomSolution()
        self.fitness = 0.0
        self.hasTestYet = False

    def __lt__(self, other):
        return self.getFitness() > other.getFitness()

    def __int__(self):
        return int(self.getFitness())

    def __float__(self):
        return self.getFitness()

    def __str__(self):
        string = str('Fitness:{fitness} \n'.format(fitness=self.getFitness()))
        for row in self.solution:
            string += str('{}\n'.format(row))
        return string

    def __call__(self, partnerA, partnerB):
        for i in key:
            pivot = randomInt(0, 100)
            for j in range(0, NUMBER_OF_HOUSES):
                if(pivot < 50):
                    tempSolution = partnerA.solution
                else:
                    tempSolution = partnerB.solution
                self.solution[j][i] = tempSolution[j][i]
        if(self.isMutationPossible()):
             self.mutate()
        self.test()

    def isMutationPossible(self):
        return randomInt(0, MAX_MUTATION_PROBABILITY) <= MUTATION_PROBABILITY

    def mutate(self):
        tempValueIndex = randomInt(0, lastIndex(key))
        newIndex = randomInt(0, lastIndex(key))
        while tempValueIndex == newIndex:
            newIndex = randomInt(0, lastIndex(key))
            pass
        if(newIndex != tempValueIndex):
            keyToMutate = key[randomInt(0, lastIndex(key))]
            tempValue = self.solution[tempValueIndex][keyToMutate]
            self.solution[tempValueIndex][keyToMutate] = self.solution[newIndex][keyToMutate]
            self.solution[newIndex][keyToMutate] = tempValue
            return True

    def getFitness(self):
        if not self.hasTestYet:
            self.test()
        return self.fitness

    def test(self):
        sum = 0
        if(self.checkSingleHouseRule('nation', 'Englishman', 'color', 'Red')):
            sum += 1
        else:
            sum -= 1
        if(self.checkSingleHouseRule('nation', 'Spaniard', 'pet', 'Dog')):
            sum += 1
        else:
            sum -= 1
        if(self.checkSingleHouseRule('drink', 'Coffe', 'color', 'Green')):
            sum += 1
        else:
            sum -= 1
        if(self.checkSingleHouseRule("nation", "Ukrainian", "drink", "Tea")):
            sum += 1
        else:
            sum -= 1
        if(self.checkNeighborhoodRules("color", "Ivory", "color", "Green")):
            sum += 1
        else:
            sum -= 1
        if(self.checkSingleHouseRule("smoke", "Old Gold", "pet", "Snails")):
            sum += 1
        else:
            sum -= 1
        if(self.checkSingleHouseRule("smoke", "Kools", "color", "Yellow")):
            sum += 1
        else:
            sum -= 1
        if(self.checkRuleForExactHouse(2, "drink", "Milk")):
            sum += 1
        else:
            sum -= 1
        if(self.checkRuleForExactHouse(0, "nation", "Norwegian")):
            sum += 1
        else:
            sum -= 1
        if(self.checkNeighborhoodRules("pet", "Fox", "smoke", "Chesterfield")):
            sum += 1
        else:
            sum -= 1
        if(self.checkNeighborhoodRules("smoke", "Kools", "pet", "Horse")):
            sum += 1
        else:
            sum -= 1
        if(self.checkSingleHouseRule("smoke", "Lucky Strike", "drink", "Orange juice")):
            sum += 1
        else:
            sum -= 1
        if(self.checkSingleHouseRule("nation", "Japanese", "smoke", "Parliaments")):
            sum += 1
        else:
            sum -= 1
        if(self.checkNeighborhoodRules("nation", "Norwegian", "color", "Blue")):
            sum += 1
        else:
            sum -= 1

        self.fitness = round((sum / NUMBER_OF_RULES) * 100, 3)
        self.hasTestYet = True

    def checkSingleHouseRule(self, key1, value1, key2, value2):
        for i in self.solution:
            if(i[key1] == value1 and i[key2] == value2):
                return True
        return False

    def checkNeighborhoodRules(self, House1_key, House1_value, House2_key, House2_value):
        for i in range(0, NUMBER_OF_HOUSES):
            if(self.solution[i][House1_key] == House1_value):
                if(i + 1) % NUMBER_OF_HOUSES:
                    if(self.solution[(i + 1)][House2_key] == House2_value):
                        return True
        return False

    def checkRuleForExactHouse(self, house, key, value):
        return self.solution[house][key] == value
