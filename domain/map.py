import pickle
from random import random, randint
import numpy as np
from utils import  *
import pygame

class Map():
    def __init__(self, n = 20, m = 20, sensors=[]):
        self.n = n
        self.m = m
        self.surface = np.zeros((self.n, self.m))
        self.explored = set()
        self.sensors = sensors
        self.setSensors()
    
    def setSensors(self):
        for sensor in self.sensors:
            self.surface[sensor.x][sensor.y] = 2

    def randomMap(self, fill = 0.2):
        for i in range(self.n):
            for j in range(self.m):
                if random() <= fill :
                    self.surface[i][j] = 1

    def saveMap(self, numFile = "test.map"):
        with open(numFile,'wb') as f:
            pickle.dump(self, f)
            f.close()
        
    def loadMap(self, numfile):
        with open(numfile, "rb") as f:
            dummy = pickle.load(f)
            self.n = dummy.n
            self.m = dummy.m
            self.surface = dummy.surface
            for i in range(self.n):
                for j in range(self.m):
                    if self.surface[i][j] == 2:
                        self.surface[i][j] = 0
            f.close()
        self.setSensors()

    def resetExplored(self):
        self.explored = set()

    def __str__(self):
        string=""
        for i in range(self.n):
            for j in range(self.m):
                string = string + str(int(self.surface[i][j]))
            string = string + "\n"
        return string
    
    def image(self, path, drone, colour = BLUE, background = WHITE):
        imagine = pygame.Surface((400,400))
        brick = pygame.Surface((20,20))
        brick.fill(BLUE)
        imagine.fill(WHITE)
        for i in range(self.n):
            for j in range(self.m):
                if (self.surface[i][j] == 1):
                    imagine.blit(brick, ( j * 20, i * 20))
                if (self.surface[i][j] == 2):
                    imagine.blit(pygame.image.load("sensor.png"), ( j * 20, i * 20))

        brick.fill(GREEN)

        for p in path:
            if self.surface[p.x][p.y] != 2:
                imagine.blit(brick, ( p.y * 20, p.x * 20))

        brick.fill(PURPLE)
        imagine.blit(brick, (drone.y * 20, drone.x * 20))

        return imagine
                
    