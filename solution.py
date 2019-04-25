from utils import generateRandomSolution
from utils import lastIndex
from utils import randomInt

key = ["nation", "color", "drink", "smoke", "pet"]

class solution(object):

    def __init__(self):
        self.solution = generateRandomSolution()
        self.fitnes = 0.0
        self.hasTestYet = False
        self.mutationProbabily = 300

    def toString(self):
        for row in self.solution:
            print(row)
        print('Fitnes {fitnes}'.format(fitnes=self.fitnes))

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

    def reproduce(self, solutionA, solutionB):
        for i in key:
            pivot = randomInt(0, 100)
            for j in range(0, 5):
                if(pivot < 50):
                    tempSolution = solutionA.getSolutionTab()
                else:
                    tempSolution = solutionB.getSolutionTab()
                self.solution[j][i] = tempSolution[j][i]
        if(randomInt(1, 1000) <= self.mutationProbabily):
             self.mutate()

    def checkRule(self, key1, value1, key2, value2):
        for i in self.solution:
            if(i[key1] == value1 and i[key2] == value2):
                return True
        return False

    def checkNeighborhoodRules(self, House1_key, House1_value, House2_key, House2_value):
        for i in range(0, 5):
            if(self.solution[i][House1_key] == House1_value):
                if(i + 1) % 5 :
                    if(self.solution[(i + 1)][House2_key] == House2_value):
                        return True
        return False

    def checkRuleForExactHouse(self, house, key, value):
        return self.solution[house][key] == value

    def getFitnes(self):
        if(self.hasTestYet == False):
            self.test()
        return self.fitnes

    def test(self):
        sum = 0
        if(self.checkRule('nation', 'Englishman', 'color', 'Red')):
            # print('The Englishman lives in the red house.')
            sum += 1
        else:
            sum -= 1
        if(self.checkRule('nation', 'Spaniard', 'pet', 'Dog')):
            # print('The Spaniard owns the dog.')
            sum += 1
        else:
            sum -= 1
        if(self.checkRule('drink', 'Coffe', 'color', 'Green')):
            # print('Coffee is drunk in the green house.')
            sum += 1
        else:
            sum -= 1
        if(self.checkRule("nation", "Ukrainian", "drink", "Tea")):
            # print('The Ukrainian drinks tea.')
            sum += 1
        else:
            sum -= 1
        if(self.checkNeighborhoodRules("color", "Ivory", "color", "Green")):
            # print('The green house is immediately to the right of the ivory house')
            sum += 1
        else:
            sum -= 1
        if(self.checkRule("smoke", "Old Gold", "pet", "Snails")):
            # print('The Old Gold smoker owns snails')
            sum += 1
        else:
            sum -= 1
        if(self.checkRule("smoke", "Kools", "color", "Yellow")):
            # print('Kools are smoked in the yellow house.')
            sum += 1
        else:
            sum -= 1
        if(self.checkRuleForExactHouse(2, "drink", "Milk")):
            # print('Milk is drunk in the middle house.')
            sum += 1
        else:
            sum -=1
        if(self.checkRuleForExactHouse(0, "nation", "Norwegian")):
            # print('The Norwegian lives in the first house.')
            sum += 1
        else:
            sum -= 1
        if(self.checkNeighborhoodRules("pet", "Fox", "smoke", "Chesterfield")):
            # print('The man who smokes Chesterfields lives in the house next to the man with the fox')
            sum += 1
        else:
            sum -=1
        if(self.checkNeighborhoodRules("smoke", "Kools", "pet", "Horse")):
            # print('Kools are smoked in the house next to the house where the horse is kept.')
            sum += 1
        else:
            sum -= 1
        if(self.checkRule("smoke", "Lucky Strike", "drink", "Orange juice")):
            # print('The Lucky Strike smoker drinks orange juice')
            sum += 1
        else:
            sum -= 1
        if(self.checkRule("nation", "Japanese", "smoke", "Parliaments")):
            # print('The Japanese smokes Parliaments.')
            sum += 1
        else:
            sum -= 1
        if(self.checkNeighborhoodRules("nation", "Norwegian", "color", "Blue")):
            # print('The Norwegian lives next to the blue house.')
            sum += 1
        else:
            sum -= 1

        self.fitnes = round((sum / 14) * 100, 3)
        self.hasTestYet = True

    def getSolutionTab(self):
        return self.solution

