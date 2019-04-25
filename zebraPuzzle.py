#!/usr/bin/env python3
import sys
from population import population

def run():
    populationSize = 100000
    p = population(populationSize)
    print('Genetic Algorithm to solving zebra puzzle')
    print('Population size: {size}' .format(size=populationSize))
    for i in range(100):
        p.reproduce()
        best = p.getBestFited()
        print('Generation: {generation}, best fitness: {fitnes}, average fitness: {avg}'.format(generation=(i + 1), fitnes=best.getFitnes(), avg=p.getAverageFitnes()))
        if(best.getFitnes() >= 100):
            print('Best solution')
            best.toString()
            sys.exit(0)

run()
