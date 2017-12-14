#!/usr/bin/env python
import random
import sys

nation = [ "Norwegian", "Ukrainian", "Englishman", "Spaniard", "Japanese" ]
color  = [ "Red", "Blue", "Yellow", "Ivory", "Green" ]
drink  = [ "Tea", "Milk", "Coffe", "Orange juice", "Water" ]
smoke  = [ "Lucky Strike", "Old Gold", "Kools", "Chesterfield","Parliaments"]
pet    = [ "Zebra", "Fox", "Horse", "Snails", "Dog" ]

key = ["nation", "color", "drink", "smoke", "pet"]

def randomInt(min, max):
    return int(random.randint(min, max))

def lastIndex(array):
    return len(array) - 1


def getKeyTabelByName(name):
    if(name == "nation"):
        return nation
    elif(name == "color"):
        return color
    elif(name == "drink"):
        return drink
    elif(name == "smokes"):
        return smoke
    elif(name == "pet"):
        return pet

def generateRandomRecord():
    record = {"nation" : random.choice(nation), 
              "color" : random.choice(color), 
              "drink" : random.choice(drink), 
              "smoke" : random.choice(smoke), 
              "pet": random.choice(pet)}
    return record

def generateRandomSolution():
    lnation = [ "Norwegian", "Ukrainian", "Englishman", "Spaniard", "Japanese" ]
    lcolor  = [ "Red", "Blue", "Yellow", "Ivory", "Green" ]
    ldrink  = [ "Tea", "Milk", "Coffe", "Orange juice", "Water" ]
    lsmoke  = [ "Lucky Strike", "Old Gold", "Kools", "Chesterfield","Parliaments"]
    lpet    = [ "Zebra", "Fox", "Horse", "Snails", "Dog" ]
    random.shuffle(lnation)
    random.shuffle(lcolor)
    random.shuffle(ldrink)
    random.shuffle(lsmoke)
    random.shuffle(lpet)

    solution = []
    i = 0
    for i in range(5):
        sample = {"nation" : lnation[i], 
                  "color"  : lcolor[i], 
                  "drink"  : ldrink[i], 
                  "smoke"  : lsmoke[i], 
                  "pet"    : lpet[i] }
        solution.append(sample)
    return solution

class solution():

    def __init__(self):
        self.solutionTab = []
        self.fitnes = 0.0
        self.isLive = False
        self.number = 0

    def initSolution(self):
        self.solutionTab = generateRandomSolution()

    def mutate(self):
        keyToMutate = key[randomInt(0, lastIndex(key))]
        tempValueIndex = randomInt(0,4)
        tempValue = self.solutionTab[tempValueIndex][keyToMutate]
        newIndex = randomInt(0,4)
        self.solutionTab[tempValueIndex][keyToMutate] = self.solutionTab[newIndex][keyToMutate]
        self.solutionTab[newIndex][keyToMutate] = tempValue

    def reproduce(self, solutionA, solutionB):
        self.initSolution()
        for i in key:
            pivot = randomInt(0, 100)
            for j in range(5):
                if(pivot < 50):
                    tempSolution = solutionA.getSolutionTab()
                else:
                    tempSolution = solutionB.getSolutionTab()
                self.solutionTab[j][i] = tempSolution[j][i]
        if(randomInt(0,1000) < 10):
            self.mutate()

    def numberOfHouse(self, key, value):
        for i in range(5):
            if(self.solutionTab[i][key] == value):
                self.number = i
                return True
        return False

    def getFitnes(self):
        if(self.isLive == False):
            self.live()
        return self.fitnes

    def getSolutionTab(self):
        return self.solutionTab

    def checkRule(self, key, value, key2, value2):
        for i in self.solutionTab:
            if i[key] == value and i[key2] == value2:
                return True
        return False

    def live(self):
        #The Englishman lives in the red house.
        if(self.checkRule("nation", "Englishman", "color", "Red")):
            self.fitnes += 1
        #The Spaniard owns the dog.
        if(self.checkRule("nation", "Spaniard", "pet", "Dog")):
            self.fitnes += 1
        #Coffee is drunk in the green house.
        if(self.checkRule("drink", "Coffe", "color", "Green")):
            self.fitnes += 1
        #The Ukrainian drinks tea.
        if(self.checkRule("nation", "Ukrainian", "drink", "Tea")):
            self.fitnes += 1.
        #The green house is immediately to the right of the ivory house
        if(self.numberOfHouse("color", "Ivory")):
            if((self.number + 1 ) % 5):
                if(self.solutionTab[(self.number + 1)]["color"] == "Green"):
                    self.fitnes += 1
        #The Old Gold smoker owns snails.
        if(self.checkRule("smoke", "Old Gold", "pet", "Snails")):
            self.fitnes += 1
        #Kools are smoked in the yellow house.
        if(self.checkRule("smoke", "Kools", "color", "Yellow")):
            self.fitnes += 1
        #Milk is drunk in the middle house.
        if(self.solutionTab[2]["drink"] == "Milk"):
            self.fitnes += 1
        #The Norwegian lives in the first house.
        if(self.solutionTab[0]["nation"] == "Norwegian"):
            self.fitnes += 1
        #The man who smokes Chesterfields lives in the house next to the man with the fox
        if(self.numberOfHouse("pet", "Fox")):
            if((self.number + 1 ) % 5):
                if(self.solutionTab[(self.number + 1)]["smoke"] == "Chesterfield"):
                    self.fitnes += 1
        #Kools are smoked in the house next to the house where the horse is kept.
        if(self.numberOfHouse("smoke", "Kools")):
            if((self.number + 1 ) % 5):
                if(self.solutionTab[(self.number + 1)]["pet"] == "Horse"):
                    self.fitnes += 1
        #The Lucky Strike smoker drinks orange juice
        if(self.checkRule("smoke", "Lucky Strike", "drink", "Orange juice")):
            self.fitnes += 1
        #The Japanese smokes Parliaments.
        if(self.checkRule("nation", "Japanese", "smoke", "Parliaments")):
            self.fitnes += 1
        #The Norwegian lives next to the blue house.
        if(self.numberOfHouse("nation", "Norwegian")):
            if((self.number + 1 ) % 5):
                if(self.solutionTab[(self.number + 1)]["color"] == "Blue"):
                    self.fitnes += 1
        self.fitnes = self.fitnes / 14
        self.isLive = True

def makeSolution():
    temp = solution()
    temp.initSolution()
    return temp

def createPopulation(size , population):
    for i in range(size):
        population.append(makeSolution())
    population.sort(key=lambda x: x.getFitnes(), reverse=True)

def reproducePopulation(oldPopulation, newPopulation, size):
    for i in range((size/4)*3):
        s = solution()
        s.reproduce(oldPopulation[random.randint(0,((3*len(oldPopulation))/4))], oldPopulation[random.randint(0,((3*len(oldPopulation))/4))])
        newPopulation.append(s)
    newPopulation.sort(key=lambda x: x.getFitnes(), reverse=True)
    print newPopulation[0].getFitnes()

    if(newPopulation[0].getFitnes() > 0.92):
        print "Best solution"
        print newPopulation[0].getFitnes()
        print newPopulation[0].getSolutionTab()
        sys.exit(0)


def run():
    newPopulation = []
    npopulation = 500
    createPopulation(npopulation, newPopulation)
    oldPopulation = []
    for i in range(4000):
        reproducePopulation(newPopulation, oldPopulation, npopulation)
        newPopulation = []
        reproducePopulation(oldPopulation, newPopulation, npopulation)
        oldPopulation = []


run()
