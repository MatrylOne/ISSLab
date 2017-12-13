from random import random
from math import fabs
from math import floor

def calculateErrorDerivative(timeArray, errorArray):
    calka = 0
    if len(timeArray) > 2:
        h = timeArray[1] - timeArray[0]
        for error in errorArray:
            calka += fabs(error)*h
    return calka

def calculatePowerDerivative(timeArray, errorArray):
    calka = 0
    if len(timeArray) > 2:
        h = timeArray[1] - timeArray[0]
        for error in errorArray:
            calka += error*error*h
    return calka

def findMaxError(errorArray, stableIndex):
    return max(errorArray[stableIndex:len(errorArray)-1])

def valuesInRange(valueArray, minValue, maxValue):
    arrayLength = len(valueArray) - 1
    for i in range(0, arrayLength):
        if(max(valueArray[i:arrayLength]) <= maxValue and min(valueArray[i:arrayLength] >= minValue)):
            return i
    return -1

def countSteps(start, stop, step):
    return int((stop - start)/step)

def createArray(start, stop, step):
    # Inicjacja tablicy
    array = []
    for i in range(0, countSteps(start, stop, step)):
        array.append(step*i)
    return array

def createLineArray(timeArray, value):
    array = []
    for v in timeArray:
        array.append(value)
    return array

def randomRange(range):
    return range[0] + (random() * (range[1] - range[0]))

def delayToSteps(delay, h):
    stepsBack = floor(delay/h)
    return stepsBack