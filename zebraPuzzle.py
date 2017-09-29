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

def search(key, value, key2, value2, ilist):
    p = 0
    for p in ilist:
        if p[key] == value and p[key2] == value2:
            return p

def getFitnes(solution):
    fitnes = 0.00
    if(solution[0]["nation"] == "Norwegian"):
        fitnes = fitnes + 1
    if(search("nation", "Englishman", "color", "Red", solution) != None):
        fitnes = fitnes + 1
    if(search("nation", "Spaniard", "pet", "Dog", solution) != None):
        fitnes = fitnes + 1
    if(search("drink", "Coffe", "color", "Green", solution) != None):
        fitnes = fitnes + 1
    if(search("nation", "Ukrainian", "drink", "Tea", solution) != None):
        fitnes = fitnes + 1
    #The green house is immediately to the right of the ivory house.
    if(search("smoke", "Old Gold", "pet", "Snails", solution) != None):
        fitnes = fitnes + 1
    if(search("smoke", "Kools", "color", "Yellow", solution) != None):
        fitnes = fitnes + 1
    if(solution[2]["drink"] == "Milk"):
        fitnes = fitnes + 1
    #The man who smokes Chesterfields lives in the house next to the man with the fox
    #Kools are smoked in the house next to the house where the horse is kept.
    if(search("smoke", "Lucky Strike", "drink", "Orange juice", solution) != None):
        fitnes = fitnes + 1
    if(search("nation", "Japanese", "smoke", "Parliaments", solution) != None):
        fitnes = fitnes + 1
    fitnes = fitnes / 10
    return fitnes

print getFitnes(generateRandomSolution())
#print search("drink", "Tea", generateRandomSolution())
