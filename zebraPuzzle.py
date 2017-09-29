#!/usr/bin/env python
import random

nation = [ "Norwegian", "Ukrainian", "Englishman", "Spaniard", "Japanese" ]
color  = [ "Red", "Blue", "Yellow", "Ivory", "Green" ]
drink  = [ "Tea", "Milk", "Coffe", "Orange juice", "Water" ]
smoke  = [ "Lucky Strike", "Old Gold", "Kools", "Chesterfield" ]
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
	for i in xrange(0,5):
		dlist.append(generateRandomRecord())
	return dlist
	
print generateRandomSolution()
