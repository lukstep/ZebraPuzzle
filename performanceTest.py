#!/usr/bin/env python3
import time
from population import Population

NUMBER_OF_GENERATIONS = 5
NUMBER_OF_ALGORITM_EXECUTION = 10
POPULATION_SIZE = 100000

def runAlgorithm(populationSize):
    population = Population(populationSize)
    for _ in range(NUMBER_OF_GENERATIONS):
        population()
        best = population.getBestFited()
        if(best.getFitness() >= 100):
            return 1
    return 0

def benchmark():
    print("Start performance and stability test")
    NumberOfSucess = 0
    startTime = time.process_time()
    startPerfTime = time.perf_counter()

    for _ in range(NUMBER_OF_ALGORITM_EXECUTION):
        if(runAlgorithm(POPULATION_SIZE)):
            NumberOfSucess += 1

    elapsedTime = time.process_time() - startTime
    elapsedPerfTime = time.perf_counter() - startPerfTime
    stability = round((NumberOfSucess / NUMBER_OF_ALGORITM_EXECUTION * 100), 1)
    print('Test results: time: {time}s, perfTime: {perf}s, stability: {stability}%'\
        .format(time=elapsedTime, perf=elapsedPerfTime, stability=stability))

if __name__ == '__main__':
   benchmark()