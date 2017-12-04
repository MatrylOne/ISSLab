from random import random

def countSteps(start, stop, step):
    return int((stop - start)/step)

def createArray(start, stop, step):
    # Inicjacja tablicy
    array = []
    for i in range(0, countSteps(start, stop, step)):
        array.append(step*i)
    return array

def randomRange(range):
    return range[0] + (random() * (range[1] - range[0]))