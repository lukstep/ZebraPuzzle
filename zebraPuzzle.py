#!/usr/bin/env python
import random

nation = [ "Norwegian", "Ukrainian", "Englishman", "Spaniard", "Japanese" ]
color  = [ "Red", "Blue", "Yellow", "Ivory", "Green" ]
drink  = [ "Tea", "Milk", "Coffe", "Orange juice", "Water" ]
smoke  = [ "Lucky Strike", "Old Gold", "Kools", "Chesterfield","Parliaments"]
pet    = [ "Zebra", "Fox", "Horse", "Snails", "Dog" ]


def generateRandomRecord():
    record = {"nation" : random.choice(nation), 
              "color" : random.choice(color), 
              "drink" : random.choice(drink), 
              "smoke" : random.choice(smoke), 
              "pet": random.choice(pet)}
    return record

def generateRandomSolution():
    dlist = []
    for i in range(5):
        dlist.append(generateRandomRecord())
    return dlist

class solution():

    def __init__(self):
        self.solutionTab = generateRandomSolution()
        self.fitnes = 0.0

    def getFitnes(self):
        self.live()
        return self.fitnes

    def getSolutionTab(self):
        return self.solutionTab

    def search(self, key, value, key2, value2):
        p = 0
        for p in self.solutionTab:
            if p[key] == value and p[key2] == value2:
                return True
        return False

    def live(self):
        if(self.solutionTab[0]["nation"] == "Norwegian"):
            self.fitnes += 1
        if(self.search("nation", "Englishman", "color", "Red")):
            self.fitnes += 1
        if(self.search("nation", "Spaniard", "pet", "Dog")):
            self.fitnes += 1
        if(self.search("drink", "Coffe", "color", "Green")):
            self.fitnes += 1
        if(self.search("nation", "Ukrainian", "drink", "Tea")):
            self.fitnes += 1
        #The green house is immediately to the right of the ivory house.
        if(self.search("smoke", "Old Gold", "pet", "Snails")):
            self.fitnes += 1
        if(self.search("smoke", "Kools", "color", "Yellow")):
            self.fitnes += 1
        if(self.solutionTab[2]["drink"] == "Milk"):
            self.fitnes += 1
        #The man who smokes Chesterfields lives in the house next to the man with the fox
        #Kools are smoked in the house next to the house where the horse is kept.
        if(self.search("smoke", "Lucky Strike", "drink", "Orange juice")):
            self.fitnes += 1
        if(self.search("nation", "Japanese", "smoke", "Parliaments")):
            self.fitnes += 1
        self.fitnes = self.fitnes / 10
        #print self.fitnes

def reproduce(solutionA, solutionB, pivot):
    newSolution = [];
    for i in range(5):
        newSolution.append(solutionA[i])
        if i < pivot:
            newSolution.append(solutionB[i])
    return newSolution

def createPopulation(size):
    population = []
    for i in range(size):
        s = solution()
        population.append(s)
        print s.getFitnes()
        print s.getSolutionTab()
    population.sort(key=lambda x: x.getFitnes(), reverse=True)
    return population

def run():
    newPopulation = createPopulation(4)
    oldPopulation = []

#print getFitnes(generateRandomSolution()
run()
