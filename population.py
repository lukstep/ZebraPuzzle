from utils import randomInt
from solution import solution

class population(object):

    def __init__(self, size):
        super(population, self).__init__()
        self.populationSize = size
        self.newPopulation = []
        self.oldPopulation = []
        self.livenes = 200
        for i in range(self.populationSize):
            self.newPopulation.append(solution())
        self.newPopulation.sort(key=lambda x: x.getFitnes(), reverse=True)

    def toString(self):
        print('--NEW POPULATION--')
        for i in self.newPopulation:
            i.toString()
        print('--OLD POPULATION--')
        for i in self.oldPopulation:
            i.toString()

    def reproduce(self):
        bestFited = []
        self.oldPopulation = self.newPopulation
        self.newPopulation = []
        for i in range(self.livenes):
            for j in range(int(self.oldPopulation[i].getFitnes())):
                bestFited.append(i)
        for i in range(0, self.populationSize):
            s = solution()
            indexA = bestFited[randomInt(0, len(bestFited) - 1)]
            indexB = bestFited[randomInt(0, len(bestFited) - 1)]
            while indexA == indexB:
                indexB = bestFited[randomInt(0, len(bestFited) - 1)]
                pass
            s.reproduce(self.oldPopulation[indexA], 
                            self.oldPopulation[indexB])
            self.newPopulation.append(s)
        self.newPopulation.sort(key=lambda x: x.getFitnes(), reverse=True)

    def getBestFited(self):
        return self.newPopulation[0]

    def getAverageFitnes(self):
        sumFitnes = 0.0
        for i in self.newPopulation:
            sumFitnes += i.getFitnes()
        return round(sumFitnes / self.populationSize, 2)
