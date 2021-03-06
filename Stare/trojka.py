import numpy as np
import matplotlib.pyplot as pt
import pygame
import math

### METODY POMOCNICZE ###
def countSteps(start, stop, step):
    return int((stop - start)/step)

def createArray(start, stop, step):
    array = []
    for i in range(0, countSteps(start, stop, step)):
        array.append(step*i)
    return array

def drawPlot(times, xs, ys, zs):
    pt.figure(1)
    #gorny wykres
    pt.subplot(211)
    #wykres od czasu
    pt.plot(times, xs, times, ys)
    #dolny wykres
    pt.subplot(212)
    #wykres stanu
    pt.plot(ys, xs)
    #punkt początku
    pt.plot(ys[0], xs[0], "bo")
    #punkt końca
    pt.plot(ys[len(ys) - 1], xs[len(xs) - 1], "ro")
    pt.show()

def runAnimation(times, xs, ys):
    # Zmienne pomocnicze
    screenSize = (960, 640)

    screen = pygame.display.set_mode(screenSize)
    clock = pygame.time.Clock()
    arraySize = len(times) - 1

    counter = 0
    running = True

    # Parametry animacji
    SCALE = 200
    OFSET = (int(screenSize[0] / 2), int(screenSize[1] / 2))

    while running:
        # Wykrywanie zamknięcia okna
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = 0

        # Limitowanie fps do 60
        clock.tick(60)

        # Obliczanie pozycji skorygowanych o skalę i przesunięcie
        x = int(SCALE * xs[counter] + OFSET[0])
        y = int(SCALE * ys[counter] + OFSET[1])

        # Wypełnienie klatki kolorem
        screen.fill([0, 0, 0])

        # Narysowanie okręgu o wyliczonej pozycji (x)
        pygame.draw.circle(screen, (255,255,255),(x, OFSET[1]) , 20)
        # Narysowanie okręgu o wyliczonej pozycji (y)
        pygame.draw.circle(screen, (0,255,255), (y, OFSET[1] + 20) , 20)
        # Narysowanie okręgu ukazującego środek układu
        pygame.draw.circle(screen, (40, 40, 40), (OFSET), 5)
        # Wyświetlenie powyżej wypełnionej klatki
        pygame.display.flip()

        # Zapętlenie animacji po przejściu po całej tablicy
        if(counter >= arraySize):
            counter = 0
        else:
            counter += 1

### GŁÓWNE METODY ###
def model():
    # PARAMETRY SYMULACJI #
    T = 100
    h = 0.1
    x0 = 0.
    y0 = 0.
    z0 = 0.

    # INICJACJA TABLIC #
    times = createArray(0, T, h)
    xs = [x0]
    ys = [y0]
    zs = [z0]

    for i in range(0, len(times) - 1):
        xs.append(xs[i] + h * (  ys[i]  ))
        ys.append(ys[i] + h * (  zs[i]  ))
        zs.append(zs[i] + h * (  0.2 - ys[i + 1] - math.sin(xs[i + 1])  ))

    return times, xs, ys, zs

### WYWOŁANIE METOD ###
times, xs, ys, zs = model()
drawPlot(times, xs ,ys, zs)
runAnimation(times, xs, ys)