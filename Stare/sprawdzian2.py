import numpy as np
import matplotlib.pyplot as pt
import pygame


def countSteps(start, stop, step):
    return int((stop - start)/step)

def createArray(start, stop, step):
    array = []
    for i in range(0, countSteps(start, stop, step)):
        array.append(step*i)
    return array

def model():
    T = 60
    h = 0.001
    x0 = 0.0
    y0 = 0.5

    times = createArray(0, T, h)
    xs = [x0]
    ys = [y0]

    for i in range(0, len(times) - 1):
        # xs.append(xs[i] + h * (- xs[i]**3 + 4 * xs[i] - ys[i]))
        # ys.append(ys[i] + h * (xs[i] - 0.05))
        xs.append(xs[i] + h * (-1 * xs[i]**3 + 4 * xs[i] - ys[i]))
        ys.append(ys[i] + h * (xs[i] - 0.05))

    return times, xs, ys

def drawPlot(times, xs, ys):
    pt.figure(1)
    #gorny wykres
    pt.subplot(211)
    #wykres od czasu
    pt.plot(times, xs, times, ys)
    #dolny wykres
    pt.subplot(212)
    #wykres stanu
    pt.plot(xs, ys)
    #punkt początku
    pt.plot(xs[0], ys[0], "bo")
    #punkt końca
    pt.plot(xs[len(xs) - 1], ys[len(xs) - 1], "ro")
    pt.show()

def runAnimation(times, xs, ys):

    screenSize = (960, 640)

    SCALE = 20
    OFSET = (int(screenSize[0]/2), int(screenSize[1]/2))

    screen = pygame.display.set_mode(screenSize)
    clock = pygame.time.Clock()

    arraySize = times.shape[0] - 1
    counter = 0

    running = True
    while running:

        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = 0
        screen.fill([0, 0, 0])
        clock.tick(60)

        x = int(SCALE * xs[counter] + OFSET[0])
        y = int(SCALE * ys[counter] + OFSET[1])
        pygame.draw.circle(screen, (255,255,255),(OFSET[0],OFSET[1] ), round(x/2))
        # pygame.draw.circle(screen, (40, 40, 40), (OFSET), 5)
        pygame.display.flip()
        if(counter >= arraySize):
            counter = 0
        else:
            counter += 1
        print(xs[counter])

times, xs, ys = model()
drawPlot(times, xs ,ys)