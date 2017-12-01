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

def extrema(xs, times):
    extremas = []
    eTimes = []

    if(len(xs) > 2):

        rising = xs[1] > xs[0]

        for i in range(0, len(xs) - 2):
            if((xs[i+1] > xs[i]) != rising):
                extremas.append(xs[i+1])
                eTimes.append(times[i+1])
                rising = xs[i+1] > xs[i]

    return (extremas, eTimes)

def drawPlot(times, xs, ys):
    pt.figure(1)
    #gorny wykres
    pt.subplot(311)
    #wykres od czasu
    xPlot, = pt.plot(times, xs, label='x')
    yPlot, = pt.plot(times, ys, label='y')
    pt.legend(handles=[xPlot, yPlot])
    pt.xlabel("stan")
    pt.ylabel("czas")
    # ePlot = pt.plot(extremas[1], extremas[0], 'bo')
    # cPlot = pt.plot(crossings[1], crossings[0], 'ro')
    #dolny wykres
    pt.subplot(313)
    #wykres stanu
    pt.plot(xs, ys)
    #punkt początku
    pt.plot(xs[0], ys[0], "bo")
    #punkt końca
    pt.plot(xs[len(xs) - 1], ys[len(xs) - 1], "ro")

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
    # Parametry symulacji
    T = 60
    h = 0.001

    # Parametry modelu
    x0 = 1.
    y0 = -2.

    # Inicjacja tablic
    times = createArray(0, T, h)
    xs = [x0]
    ys = [y0]

    # Symulacja wypełniająca tablice
    for i in range(0, len(times) - 1):
            xs.append(xs[i] + h * (  1/2 * xs[i] - ys[i] - 1/2*(xs[i]**3 + xs[i] * ys[i]**2)  ))
            ys.append(ys[i] + h * (  xs[i + 1] + 1/2 * ys[i] - 1/2*(ys[i] ** 3 + ys[i] * xs[i + 1]**2)  ))

    return times, xs, ys

### WYWOŁYWANIE METOD ###
times, xs, ys = model()
drawPlot(times, xs ,ys)
runAnimation(times, xs, ys)