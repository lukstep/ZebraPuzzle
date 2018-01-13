#!/usr/bin/env python
import sys
from population import *

def run():
    p = population(100000)
    for i in range(1000000):
        p.reproduce()
        best = p.getBestFited()
        print('Generation: {generation} best fitnes: {fitnes}'.format(generation=i, fitnes=best.getFitnes()))
        if(best.getFitnes() > 90):
            print('---BEST SOLUTION---')
            best.toString()
            sys.exit(0)

run()
