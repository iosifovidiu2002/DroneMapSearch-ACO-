import pygame
from pygame.locals import *
from .point import Point

class Drone():
    def __init__(self, x, y, battery=100):
        self.x = x
        self.y = y
        self.battery = battery
    
    def move(self, detectedMap):
        pressed_keys = pygame.key.get_pressed()
        if self.x > 0:
            if pressed_keys[K_UP] and detectedMap.surface[self.x-1][self.y]!=1:
                self.x = self.x - 1
        if self.x < 19:
            if pressed_keys[K_DOWN] and detectedMap.surface[self.x+1][self.y]!=1:
                self.x = self.x + 1
        
        if self.y > 0:
            if pressed_keys[K_LEFT] and detectedMap.surface[self.x][self.y-1]!=1:
                self.y = self.y - 1
        if self.y < 19:        
            if pressed_keys[K_RIGHT] and detectedMap.surface[self.x][self.y+1]!=1:
                 self.y = self.y + 1

    def moveCoords(self, x, y):
        self.x = x
        self.y = y

    def movePoint(self, point):
        self.x = point.x
        self.y = point.y
        self.battery -= 1

    def getPoint(self):
        return Point(self.x,self.y)

    def isDown(self):
        return self.battery < 1
        
    def giveCharge(self, charge=1):
        self.battery -= charge
        return self.battery == 0

    def mapWithDrone(self, mapImage):
        drona = pygame.image.load("drona-modified.png")
        mapImage.blit(drona, (self.y * 20, self.x * 20))
        
        return mapImage