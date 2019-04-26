#!/usr/bin/env python3
import time
from population import population

NUMBER_OF_GENERATIONS = 5
NUMBER_OF_ALGORITM_EXECUTION = 10
POPULATION_SIZE = 100000

def runAlgorithm(populationSize):
    p = population(populationSize)
    for i in range(NUMBER_OF_GENERATIONS):
        p.reproduce()
        best = p.getBestFited()
        if(best.getFitnes() >= 100):
            return 1
    return 0

def benchmark():
    print("Start performance and stability test")
    NumberOfSucess = 0
    startTime = time.process_time()
    startPerfTime = time.perf_counter()

    for i in range(NUMBER_OF_ALGORITM_EXECUTION):
        if(runAlgorithm(POPULATION_SIZE)):
            NumberOfSucess += 1

    elapsedTime = time.process_time() - startTime
    elapsedPerfTime = time.perf_counter() - startPerfTime
    stabilty = round((NumberOfSucess / NUMBER_OF_ALGORITM_EXECUTION * 100), 1)
    print('Test results: time: {time}s, perfTime: {perf}s, stability: {stabilty}%'\
        .format(time=elapsedTime, perf=elapsedPerfTime, stabilty=stabilty))

if __name__ == '__main__':
   benchmark()