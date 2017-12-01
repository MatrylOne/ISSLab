import numpy as np
import matplotlib.pyplot as pt
import pygame
import random
import math
from itertools import product

### METODY POMOCNICZE ###
def countSteps(start, stop, step):
    return int((stop - start)/step)

def createArray(start, stop, step):
    # Inicjacja tablicy
    array = []
    for i in range(0, countSteps(start, stop, step)):
        array.append(step*i)
    return array

def extrema(xs, times):
    # Inicjacja tablic
    extremas = []
    eTimes = []
    # Sprawdzenie czy ilość danych jest wystarczajca
    if(len(xs) > 2):
        # Zapamiętanie obecnej monotoniczności funkcji
        rising = xs[1] > xs[0]
        for i in range(0, len(xs) - 2):
            # Jeśli funkcja zmienia monotoniczność = ekstremum lokalne
            if((xs[i+1] > xs[i]) != rising):
                # Dodaję punkt do tablicy
                extremas.append(xs[i+1])
                eTimes.append(times[i+1])
                # Zapamiętanie obecnego stanu funkcji
                rising = xs[i+1] > xs[i]
    return (extremas, eTimes)

def statePlot(datas):
    # Dolny wykres
    pt.figure(2)
    # pt.subplot(313)
    for i in range(0, len(datas)):
        # Wykres stanu
        pt.plot(datas[i][1], datas[i][2])
        # Punkt początku
        # pt.plot(datas[i][0], datas[i][0], "bo")
        # # Punkt końca
        # pt.plot(datas[i][1][len(datas[i][1]) - 1], datas[i][2][len(datas[i][2]) - 1], "ro")

def timePlot(datas):
    # Wykres 1
    pt.figure(1)
    # Górny wykres
    # pt.subplot(311)
    # Wykres od czasu
    xPlot, = pt.plot(datas[0][0], datas[0][1], label='x')
    yPlot, = pt.plot(datas[0][0], datas[0][2], label='y')
    pt.legend(handles=[xPlot, yPlot])
    pt.xlabel("stan")
    pt.ylabel("czas")
    pass

def showPlot():
    pt.show()
    pass

def convertPositionsToPoints(xList, yList, SCALE, OFSET):
    positions = []
    for i in range(0, len(xList)):
        positions.append((int(xList[i] * SCALE + OFSET[0]), int(yList[i] * SCALE + OFSET[1])))
    return positions

def convertModelsToPoints(datas, SCALE, OFSET):
    models = []
    for i in range(0, len(datas)):
        points = convertPositionsToPoints(datas[i][1], datas[i][2], SCALE, OFSET)
        models.append(points)
    return models

def generateColors(number, min, max):
    colors = []
    for i in range(0, number):
        colors.append((int(random.random()*(max-min) + min), int(random.random()*(max-min) + min), int(random.random()*(max-min) + min)))
    return colors

def randomColor():
    return (int(random.random() * 255), int(random.random() * 255), int(random.random() * 255))

def runAnimation(datas):
    # Zmienne pomocnicze
    screenSize = (960, 640)

    # Parametry animacji
    SCALE = 10
    OFSET = (int(screenSize[0] / 2), int(screenSize[1] / 2))

    screen = pygame.display.set_mode(screenSize)
    clock = pygame.time.Clock()

    stepCounter = 0
    running = True

    colors = generateColors(len(datas) + 1, 127, 255)

    pozycje = convertModelsToPoints(datas, SCALE, OFSET)

    # Iterowanie po krokach
    while running:
        # Wykrywanie zamknięcia okna
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = 0

        # Limitowanie fps do 60
        clock.tick(60)

        # Wypełnienie klatki kolorem
        screen.fill([255, 255, 255])

        # Iterowanie po punktach
        for i in range(0, len(datas)):
            # currentX = pozycje[i][0][stepCounter]
            # currentY = pozycje[i][1][stepCounter]

            # Rysowanie strokeów
            if (stepCounter > 2):
                pygame.draw.aalines(screen, colors[i], False, pozycje[i][0:stepCounter])
            # Rysowanie punktów
            pygame.draw.circle(screen, (0, 0, 0), pozycje[i][stepCounter], 1)

        # Wyświetlenie powyżej wypełnionej klatki
        pygame.display.flip()

        # Zapętlenie animacji po przejściu po całej tablicy
        if(stepCounter >= len(datas[0][1]) - 1):
            stepCounter = 0
        else:
            stepCounter += 1

def randomRange(range):
    return range[0] + (random.random() * (range[1] - range[0]))

### GŁÓWNE METODY ###
def model(T, h, x0, y0):
    # Inicjacja tablic
    times = createArray(0, T, h)
    xs = [x0]
    ys = [y0]

    # Symulacja wypełniająca tablice
    for i in range(0, len(times) - 1):
            # xs.append(xs[i] + h * (    ))
            # ys.append(ys[i] + h * (    ))
         xs.append(xs[i] + h * (1 / 2 * xs[i] - ys[i] - 1 / 2 * (xs[i] ** 3 + xs[i] * ys[i] ** 2)))
         ys.append(ys[i] + h * (xs[i + 1] + 1 / 2 * ys[i] - 1 / 2 * (ys[i] ** 3 + ys[i] * xs[i + 1] ** 2)))
    return (times, xs, ys)

def generateModels(T, h, xRange, yRange, iterations):
    # Inicjacja tablicy wyników
    datas = []
    # Losowanie
    for i in range(0, iterations):
        datas.append(model(T, h, randomRange(xRange), randomRange(yRange)))
    return datas

### WYWOŁYWANIE METOD ###
datas = generateModels(20, 0.005, (-10, 10), (-10, 10), 1000)
statePlot(datas)
showPlot()
runAnimation(datas)