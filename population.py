import heapq
from utils import randomInt
from solution import solution

class population(object):

    def __init__(self, size):
        self.populationSize = size
        self.newPopulation = []
        self.oldPopulation = []
        self.livenes = 1000
        self.initPopulation()

    def initPopulation(self):
        for i in range(self.populationSize):
            s = solution()
            s.test()
            heapq.heappush(self.newPopulation, s)

    def reproduce(self):
        bestFited = []
        self.oldPopulation = []

        for i in range(self.livenes):
            self.oldPopulation.append(heapq.heappop(self.newPopulation))
        self.newPopulation = []

        for i in range(self.livenes):
            for j in range(int(self.oldPopulation[i].getFitnes())):
                bestFited.append(i)
    
        for i in range(0, self.populationSize):
            indexA = bestFited[randomInt(0, len(bestFited) - 1)]
            indexB = bestFited[randomInt(0, len(bestFited) - 1)]
            while indexA == indexB:
                indexB = bestFited[randomInt(0, len(bestFited) - 1)]
                pass
            s = solution()
            s.reproduce(self.oldPopulation[indexA], 
                        self.oldPopulation[indexB])
            heapq.heappush(self.newPopulation, s)

    def getBestFited(self):
        return self.newPopulation[0]

    def getAverageFitnes(self):
        sumFitnes = 0.0
        for i in self.newPopulation:
            sumFitnes += i.getFitnes()
        return round(sumFitnes / self.populationSize, 2)
