#!/usr/bin/env python3
from population import Population

def run():
    population = Population(100000)
    print('Genetic Algorithm to solving zebra puzzle')
    print('Population size: {size}' .format(size=len(population)))
    for _ in range(10):
        population()
        print(population)
        if(population.getBestFited().fitness >= 100):
            print(population.getBestFited())
            return 0
    return 1

if __name__ == '__main__':
   run()

