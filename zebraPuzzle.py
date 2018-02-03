#!/usr/bin/env python3
import sys
from population import *

def run():
    p = population(100000)
    for i in range(100):
        p.reproduce()
        best = p.getBestFited()
        print('Generation: {generation}, best fitnes: {fitnes}, average fitnes: {avg}'.format(generation=(i + 1), fitnes=best.getFitnes(), avg=p.getAverageFitnes()))
        if(best.getFitnes() >= 100):
            print('---BEST SOLUTION---')
            best.toString()
            sys.exit(0)

run()
