from astar import searchAStar 
from collections import defaultdict
import pygame
from .point import Point
from utils import *
import copy

class Graph:
    def __init__(self, map, drone):
        self.map = map
        self.drone = drone
        self.nodePaths = defaultdict(lambda : defaultdict(list))
        self.computeNodeDistances()

    def getNodes(self):
        return list(self.nodePaths.keys())

    def getNodeCount(self):
        return len(self.nodePaths)

    def getCost(self, x, y):
        return len(self.nodePaths[x][y])

    def computeNodeDistances(self):
        sensors = self.map.sensors
        self.droneNode = Point(self.drone.x, self.drone.y)
        nodes = sensors + [self.droneNode]
        for i in range(len(nodes)):
            for j in range(i+1, len(nodes)):
                path = searchAStar(self.map, nodes[i], nodes[j])
                self.nodePaths[nodes[i]][nodes[j]] = path
                revpath = copy.deepcopy(path)
                revpath.reverse()
                self.nodePaths[nodes[j]][nodes[i]] = revpath
    
    def displayWithPaths(self):
        screen = self.map.image()
        sensors = self.map.sensors
        for i in range(len(sensors)):
            for j in range(i+1, len(sensors)):
                path = self.nodePaths[sensors[i]][sensors[j]]
                mark = pygame.Surface((20,20))
                mark.fill(GREEN)
                for move in path:
                    screen.blit(mark, (move.y *20, move.x * 20))
        
        return screen