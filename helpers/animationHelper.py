from random import random
import math


def convertDataToPoints(data):
    points = []
    for i in range(0, len(data[1])):
        points.append((data[1][i], data[2][i]))
    return points

def convertDatasToObjects(datas):
    objects = []
    for i in range(0, len(datas)):
        objects.append(convertDataToPoints(datas[i]))
    return objects

def generateColors(number, min, max):
    colors = []
    for i in range(0, number):
        colors.append((int(random()*(max-min) + min), int(random()*(max-min) + min), int(random()*(max-min) + min)))
    return colors

def randomColor():
    return (int(random() * 255), int(random() * 255), int(random() * 255))

def calculateTransform(objects, screenSize, additionalScale):
    # zwracamy SCALE i OFFSET

    ### to musimy obliczyć ###
        # minimalny x
        # maksymalny x
        # minimalny y
        # maksymalny y
    ##########################
    minWidth = 0
    minHeight = 0
    maxWidth = screenSize[0]
    maxHeight = screenSize[1]

    minX = objects[0][0][0]
    minY = objects[0][0][1]
    maxX = objects[0][0][0]
    maxY = objects[0][0][1]

    # Szukanie minimalnych i maksymalnych wartości
    for object in objects:
        for (currentX, currentY) in object:
            if(currentX < minX):
                minX = currentX
            if(currentX > maxX):
                maxX = currentX
            if (currentY < minY):
                minY = currentY
            if (currentY > maxY):
                maxY = currentY
    ##############################################
    # Obliczanie SCALE #
    trueWidth = (maxX - minX)
    trueHeight = (maxY - minY)

    scaleX = (maxWidth - minWidth)/trueWidth
    scaleY = (maxHeight - minHeight)/trueHeight

    SCALE = scaleX if scaleX < scaleY else scaleY

    SCALE *= additionalScale

    OFFSET = (int(-1*minX*SCALE + maxWidth/2 - trueWidth/2*SCALE),int(-1*minY*SCALE + maxHeight/2 - trueHeight/2*SCALE))

    print("min x : " + str(minX) + "max X : " + str(maxX))
    print("min y : " + str(minY) + "max Y : " + str(maxY))
    print("Scale X : " + str(scaleX) + "scale Y : " + str(scaleY))
    print("Scale : " + str(SCALE))

    return SCALE, OFFSET

def transformObjects(objects, SCALE, OFFSET):
    trensformed = []
    for object in objects:
        currentObject = []
        for (currentX, currentY) in object:
            currentObject.append((int(currentX * SCALE + OFFSET[0]), int(currentY * SCALE + OFFSET[1])))
        trensformed.append(currentObject)
    return trensformed
