import pygame
from utils import *

class Charger:
    def __init__(self, drone, map, sensors):
        self.drone = drone
        self.map = map
        self.sensors = sensors
    
    def checkMap(self, sensor):
        offset = 1
        explored = 0
        while True:
            
            if sensor.x + offset < 20 and  self.map.surface[sensor.x + offset][sensor.y] == 0:
                explored += 1
            if sensor.y + offset < 20 and self.map.surface[sensor.x][sensor.y + offset] == 0:
                explored += 1
            if sensor.x - offset >= 0 and self.map.surface[sensor.x - offset][sensor.y] == 0:
                explored += 1
            if sensor.y - offset >= 0 and self.map.surface[sensor.x][sensor.y - offset] == 0:
                explored += 1

            if explored < 3:
                break
            explored = 0
            if self.drone.giveCharge():
                break
            offset += 1


        sensor.charge = offset
        return offset


    def checkCharge(self):
        for sensor in self.sensors:
            if sensor == self.drone.getPoint():
                self.checkMap(sensor)
                return True
        return False

    def mapWithSensors(self, image):
        for sensor in self.sensors:
            if sensor.charge > 0:
                brick = pygame.Surface((20,20))
                brick.fill(GREEN)
                for offset in range(1,sensor.charge+1):
                    if sensor.x + offset < 20 and self.map.surface[sensor.x + offset][sensor.y] == 0:
                        image.blit(brick, (sensor.y * 20, (sensor.x + offset) * 20))
                    else:
                        break
                for offset in range(1,sensor.charge+1):    
                    if sensor.y + offset < 20 and self.map.surface[sensor.x][sensor.y + offset] == 0:
                        image.blit(brick, ((sensor.y  + offset) * 20, (sensor.x) * 20))
                    else:
                        break
                for offset in range(1,sensor.charge+1):
                    if sensor.x - offset >= 0 and self.map.surface[sensor.x - offset][sensor.y] == 0:
                        image.blit(brick, (sensor.y * 20, (sensor.x - offset) * 20))
                    else:
                        break
                for offset in range(1,sensor.charge+1):
                    if sensor.y - offset >= 0 and self.map.surface[sensor.x][sensor.y - offset] == 0:
                       image.blit(brick, ((sensor.y - offset) * 20, (sensor.x) * 20))
                    else:
                        break
        return image
