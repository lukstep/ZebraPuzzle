import heapq
from utils import randomInt
from solution import Solution

class Population(object):
    def __init__(self, size):
        self.populationSize = size
        self.newPopulation = []
        self.oldPopulation = []
        self.livenes = 1000
        self.genration = 0
        self.initPopulation()

    def __len__(self):
        return self.populationSize

    def __str__(self):
        return str('Generation:{generation}, best fitness:{fitnes}, average fitness:{avg}' \
            .format(generation=self.genration, fitnes=float(self.newPopulation[0]), avg=self.getAverageFitnes()))

    def initPopulation(self):
        for _ in range(self.populationSize):
            heapq.heappush(self.newPopulation, Solution())

    def __call__(self):
        bestFited = []
        self.oldPopulation = []

        for i in range(self.livenes):
            self.oldPopulation.append(heapq.heappop(self.newPopulation))
        self.newPopulation = []

        for i in range(self.livenes):
            for _ in range(int(self.oldPopulation[i])):
                bestFited.append(i)
    
        for i in range(0, self.populationSize):
            indexA = bestFited[randomInt(0, len(bestFited) - 1)]
            indexB = bestFited[randomInt(0, len(bestFited) - 1)]
            while indexA == indexB:
                indexB = bestFited[randomInt(0, len(bestFited) - 1)]
                pass
            s = Solution()
            s(self.oldPopulation[indexA], self.oldPopulation[indexB])
            heapq.heappush(self.newPopulation, s)
        self.genration += 1

    def getBestFited(self):
        return self.newPopulation[0]

    def getAverageFitnes(self):
        sumFitnes = 0.0
        for solution in self.newPopulation:
            sumFitnes += float(solution)
        return round(sumFitnes / self.populationSize, 2)
