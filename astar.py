from domain.point import Point
import heapq

def h(current, goal):
    return abs(current.x-goal.x) + abs(current.y-goal.y)

def getValidNeighbours(map, point):
    n = []

    if point.x+1 < 20 and map.surface[point.x + 1][point.y] != 1:
        n.append(Point(point.x + 1,point.y))

    if point.y + 1 < 20 and map.surface[point.x][point.y + 1] != 1:
        n.append(Point(point.x,point.y+1))

    if point.x - 1 >= 0 and  map.surface[point.x - 1][point.y] != 1:
        n.append(Point(point.x - 1,point.y))

    if point.y - 1 >= 0 and map.surface[point.x][point.y-1] != 1:
        n.append(Point(point.x,point.y-1))

    return n

def getPath(start, final, prev):
    path = []
    current = final

    while current != start:
        path = [current] + path
        current = prev[current]
    
    return path[:-1]

def searchAStar(mapM, initial, final):
    pq = [[h(initial,final),initial]]
    prev = {}
    dist = {}
    dist[initial] = 0
    found = False

    while len(pq) != 0:
        x = heapq.heappop(pq)[1]
        validNeighbours = getValidNeighbours(mapM, x)

        for y in validNeighbours:
            if y not in dist or dist[x] + 1 < dist[y]:
                dist[y] = dist[x] + 1
                heapq.heappush(pq, [dist[y] + h(y, final),y])
                prev[y] = x
        
            if x == final:
                found = True
    return getPath(initial, final, prev)