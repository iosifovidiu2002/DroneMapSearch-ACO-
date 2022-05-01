from collections import defaultdict
from ACO.ant import Ant

class ACO:
    def __init__(self, graph, alpha, beta, rho, iterations = 100, antPopulationSize = 5):
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.graph = graph
        self.antPopulationSize = antPopulationSize
        self.ants = [Ant(self.graph) for _ in range(self.antPopulationSize)]
        self.Q = 69
        self.iterations = iterations
        self.pheromones = defaultdict(lambda : defaultdict(lambda : 1))

    def run(self):
        for i in range(self.iterations):
            for ant in self.ants:
                for _ in range(self.graph.getNodeCount()):
                    ant.move(self.alpha, self.beta, self.pheromones)
                ant.computeLen()
            self.updatePheromones()
            if i != self.iterations - 1: 
                self.ants = [Ant(self.graph) for _ in range(self.antPopulationSize)]
    
    def selectBest(self):
        min = self.ants[0]
        for ant in self.ants:
            if ant.pathLen < min.pathLen:
                min = ant
        return min

    def buildPath(self):
        ant = self.selectBest()
        
        while ant.path[0] != self.graph.droneNode:
            ant.path = ant.path[1:]
            ant.path.append(ant.path[0])

        path = ant.path

        mappath = []
        for i in range(len(path)-1):
            mappath.append(path[i])
            mappath += self.graph.nodePaths[path[i]][path[i+1]]
        mappath.append(path[-1])

        return mappath

    def updatePheromones(self):
        for x in self.graph.getNodes():
            for y in self.graph.getNodes():
                self.pheromones[x][y] = (1 - self.rho) * self.pheromones[x][y]
                for ant in self.ants:
                    if ant.pheromones[x][y]:
                        self.pheromones[x][y] += self.Q / ant.pathLen