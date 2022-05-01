from collections import defaultdict
import random

class Ant:
    def __init__(self, graph):
        self.pheromones = defaultdict(int)
        self.graph = graph
        self.currentNode = random.choice(self.graph.getNodes())
        self.start = self.currentNode
        self.allowed = set(self.graph.getNodes())
        # possible change here -V
        self.allowed.remove(self.currentNode)
        self.path = [self.currentNode]
        self.pathLen = 0
        self.pheromones = defaultdict(lambda : defaultdict(bool))

    def move(self, alpha, beta, graphpheromones):
        sum = 0

        if len(self.allowed) == 0:
            self.allowed.add(self.path[0])

        for z in self.allowed:
            sum += (graphpheromones[self.currentNode][z] ** alpha) * ( (1/self.graph.getCost(self.currentNode,z)) ** beta)

        probability = {}

        for y in self.allowed:
            probability[y] = ((graphpheromones[self.currentNode][y] ** alpha) * ( (1/self.graph.getCost(self.currentNode,y)) ** beta)) / sum    

        nextNode = random.choices(list(probability.keys()),weights=list(probability.values()))[0]
        self.pheromones[self.currentNode][nextNode] = True
        self.currentNode = nextNode
        self.path.append(self.currentNode)
        self.allowed.remove(self.currentNode)

    def computeLen(self):
        for i in range(0,len(self.path)-1):
            self.pathLen += self.graph.getCost(self.path[i],self.path[i+1])
        