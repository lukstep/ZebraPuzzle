from utils import generateRandomSolution
from solution import *

class population(object):
    """docstring for population"""
    def __init__(self, size):
        super(population, self).__init__()
        self.populationSize = size
        self.newPopulation = []
        self.oldPopulation = []
        for i in range(self.populationSize):
            s = solution()
            self.newPopulation.append(solution())
        self.newPopulation.sort(key=lambda x: x.getFitnes(), reverse=True)

    def toString(self):
        print('--NEW POPULATION--')
        for i in self.newPopulation:
            i.toString()
        # print('--OLD POPULATION--')
        # for i in self.oldPopulation:
        #     i.toString()

    def reproduce(self):
        populationPivot = round((self.populationSize / 4) * 3)
        self.oldPopulation = self.newPopulation
        self.newPopulation = []
        for i in range(0, self.populationSize):
            # if(i < populationPivot):
            s = solution()
            indexA = randomInt(0, populationPivot)
            indexB = randomInt(0, populationPivot)
            # if(indexA != indexB):
            s.reproduce(self.oldPopulation[indexA], 
                            self.oldPopulation[indexB])
            self.newPopulation.append(s)
            # else:
            #     s = solution()
            #     self.newPopulation.append(s)
        self.newPopulation.sort(key=lambda x: x.getFitnes(), reverse=True)

    def getBestFited(self):
        return self.newPopulation[0]
