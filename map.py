import numpy as np
import monster
import random
from collections import deque

def createMap(x, y):
    map = np.empty((x, y), dtype=object)
    return map

# Weight by level??
def populateMap(map, probability = 0.5):
    for i in range(map.shape[0]):
        for j in range(map.shape[1]):
            if random.random() < probability:
                map[i, j] = monster.testMonsters[random.randint(0, len(monster.testMonsters) - 1)]
    return map

def findFurthestCell(map):
    rows, cols = map.shape
    distances = np.full((rows, cols), np.inf)
    queue = deque()

    # Step 1: Identify all monster positions
    for i in range(rows):
        for j in range(cols):
            if map[i, j] == monster.testMonsters[0] or map[i, j] == monster.testMonsters[1] or map[i, j] == monster.testMonsters[2]:
                queue.append((i, j))
                distances[i, j] = 0

    # Step 2: BFS to calculate minimum distances
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and distances[nx, ny] == np.inf:
                distances[nx, ny] = distances[x, y] + 1
                queue.append((nx, ny))

    # Step 3: Find the cell with the maximum distance
    max_distance = -1
    player_position = (0, 0)
    for i in range(rows):
        for j in range(cols):
            if distances[i, j] > max_distance:
                max_distance = distances[i, j]
                player_position = (i, j)

    return player_position


def printMap(map):
    for i in range(map.shape[0]):
        for j in range(map.shape[1]):
            if map[i, j] == None:
                print("None", end = " ")
            else:
                print(map[i, j].name, end = " ")
        print("\n")
    return ""

def moveObject(map, position, new_position):
    map[new_position] = map[position]
    map[position] = None
    return map