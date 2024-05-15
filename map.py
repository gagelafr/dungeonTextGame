import numpy as np
from monster import Monster
import monster
import random

def createMap(x, y):
    map = np.empty((x, y), dtype=object)
    return map


def populateMap(map, probability = 0.5):
    for i in range(map.shape[0]):
        for j in range(map.shape[1]):
            if random.random() < probability:
                map[i, j] = monster.testMon
    return map

def printMap(map):
    for i in range(map.shape[0]):
        for j in range(map.shape[1]):
            if map[i, j] == None:
                print("None", end = " ")
            else:
                print(map[i, j].name, end = " ")
        print("\n")
    return ""
    