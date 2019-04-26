#!/usr/bin/env python3
from population import population

def run():
    populationSize = 100000
    p = population(populationSize)
    print('Genetic Algorithm to solving zebra puzzle')
    print('Population size: {size}' .format(size=populationSize))
    for i in range(5):
        p.reproduce()
        best = p.getBestFited()
        print('Generation: {generation}, best fitness: {fitnes}, average fitness: {avg}' \
            .format(generation=(i + 1), fitnes=best.getFitnes(), avg=p.getAverageFitnes()))
        if(best.getFitnes() >= 100):
            print('Best solution')
            best.toString()
            return 0
    return 1

if __name__ == '__main__':
   run()

