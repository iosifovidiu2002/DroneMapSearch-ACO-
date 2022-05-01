from domain.map import Map
from domain.drone import Drone
from domain.point import Point
from domain.graph import Graph
import pygame
from pygame.locals import *
from utils import *
from ACO.aco import ACO
import time
from domain.sensor import Sensor
from Charger.charger import Charger

class GUI():
    def __init__(self):
        self.sensors = [Sensor(1,11),Sensor(6,16),Sensor(10,7),Sensor(10,16)]
        self.map = Map(sensors=self.sensors)
        self.map.loadMap("test.map")
        self.drone = Drone(6,10)
        self.graph = Graph(self.map, self.drone)
        self.charger = Charger(self.drone, self.map, self.sensors)


    def run(self):
        pygame.init()
        pygame.display.set_caption("ACO - Sensor recharge")

        screen = pygame.display.set_mode((400,400))
        screen.fill(WHITE)

        aco = ACO(self.graph, 2, 3, 0.5)
        aco.run()
        path = aco.buildPath()
        visited = []
        print("ACO is done")
        running = True
        speed = 200
        batteryDown = False
        start = Point(self.drone.x,self.drone.y)
        brick = pygame.Surface((20,20))
        brick.fill(BLUE)
        screen.blit(brick, ( self.drone.y * 20, self.drone.x * 20 ))
        pygame.time.set_timer(pygame.USEREVENT, speed)
        while running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.USEREVENT:
                    self.drone.movePoint(path[0])
                    visited.append(path[0])
                    path = path[1:]
                    if len(path) == 0:
                        running = False
                    self.charger.checkCharge()
                    if self.drone.isDown():
                        running = False
                        batteryDown = True
                    time.sleep(speed//1000)
            
            screen.blit(self.drone.mapWithDrone(self.charger.mapWithSensors(self.map.image(visited, start))), (0,0))
            if batteryDown:
                screen.blit(pygame.image.load("battery.png"), (start.y * 20, start.x * 20))
            pygame.display.flip()

        time.sleep(2)