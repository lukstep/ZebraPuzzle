from utils import *

key = ["nation", "color", "drink", "smoke", "pet"]

class solution(object):

    def __init__(self):
        self.solution = generateRandomSolution()
        self.fitnes = 0.0
        self.hasLivesJet = False
        self.mutationProbabily = 300
        self.numberOfMuation = 3

    def toString(self):
        printSolution(self.solution)
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
            for i in range(self.numberOfMuation):
                    self.mutate()

    def checkRule(self, key1, value1, key2, value2):
        for i in self.solution:
            if i[key1] == value1 and i[key2] == value2:
                return True
        return False

    def checkRule2(self, key1, value1, key2, value2):
        number = 0
        for i in range(0, 5):
            if self.solution[i][key1] == value1 :
                if (i + 1) % 5 :
                    if self.solution[(i + 1)][key2] == value2 :
                        return True
        return False

    def checkRule3(self, key):
        valueList = getList(key)
        for j in valueList:
            number = 0
            for i in range(5):
                if(self.solution[i][key] == j):
                    number += 1
            if (number > 1):
                return False
        return True

    def getFitnes(self):
        if self.hasLivesJet == False :
            self.test()
        return self.fitnes

    def test(self):
        sum = 0
        #The Englishman lives in the red house.
        if(self.checkRule('nation', 'Englishman', 'color', 'Red')):
            # print('The Englishman lives in the red house.')
            sum += 1
        else:
            sum -= 1
        #The Spaniard owns the dog.
        if(self.checkRule('nation', 'Spaniard', 'pet', 'Dog')):
            # print('The Spaniard owns the dog.')
            sum += 1
        else:
            sum -= 1
        #Coffee is drunk in the green house.
        if(self.checkRule('drink', 'Coffe', 'color', 'Green')):
            # print('Coffee is drunk in the green house.')
            sum += 1
        else:
            sum -= 1
        #The Ukrainian drinks tea.
        if(self.checkRule("nation", "Ukrainian", "drink", "Tea")):
            # print('The Ukrainian drinks tea.')
            sum += 1
        else:
            sum -= 1
        #The green house is immediately to the right of the ivory house
        if(self.checkRule2("color", "Ivory", "color", "Green")):
            # print('The green house is immediately to the right of the ivory house')
            sum += 1
        else:
            sum -= 1
        #The Old Gold smoker owns snails.
        if(self.checkRule("smoke", "Old Gold", "pet", "Snails")):
            # print('The Old Gold smoker owns snails')
            sum += 1
        else:
            sum -= 1
        #Kools are smoked in the yellow house.
        if(self.checkRule("smoke", "Kools", "color", "Yellow")):
            # print('Kools are smoked in the yellow house.')
            sum += 1
        else:
            sum -= 1
         #Milk is drunk in the middle house.
        if(self.solution[2]["drink"] == "Milk"):
            # print('Milk is drunk in the middle house.')
            sum += 1
        else:
            sum -=1
        #The Norwegian lives in the first house.
        if(self.solution[0]["nation"] == "Norwegian"):
            # print('The Norwegian lives in the first house.')
            sum += 1
        else:
            sum -= 1
        #The man who smokes Chesterfields lives in the house next to the man with the fox
        if(self.checkRule2("pet", "Fox", "smoke", "Chesterfield")):
            # print('The man who smokes Chesterfields lives in the house next to the man with the fox')
            sum += 1
        else:
            sum -=1
        #Kools are smoked in the house next to the house where the horse is kept.
        if(self.checkRule2("smoke", "Kools", "pet", "Horse")):
            # print('Kools are smoked in the house next to the house where the horse is kept.')
            sum += 1
        else:
            sum -= 1
        #The Lucky Strike smoker drinks orange juice
        if(self.checkRule("smoke", "Lucky Strike", "drink", "Orange juice")):
            # print('The Lucky Strike smoker drinks orange juice')
            sum += 1
        else:
            sum -= 1
        #The Japanese smokes Parliaments.
        if(self.checkRule("nation", "Japanese", "smoke", "Parliaments")):
            # print('The Japanese smokes Parliaments.')
            sum += 1
        else:
            sum -= 1
        #The Norwegian lives next to the blue house.
        if(self.checkRule2("nation", "Norwegian", "color", "Blue")):
            # print('The Norwegian lives next to the blue house.')
            sum += 1
        else:
            sum -= 1

        self.fitnes = round((sum / 14) * 100, 2)
        self.hasLivesJet = True

    def getSolutionTab(self):
        return self.solution

