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

#Model 2 zmiennych
# def model():
#     T = 60
#     h = 0.001
#     x0 = -65
#     y0 = 0
#     P = 30
#     a = 0.02
#     b = 0.2
#     c = -65
#     d = 2
#
#     times = createArray(0, T, h)
#     xs = [x0]
#     ys = [y0]
#
#     for i in range(0, len(times) - 1):
#         if(xs[i] >= 30):
#             xs.append(c)
#             ys.append(ys[i] + d)
#         else:
#             xs.append(xs[i] + h * (0.04 * xs[i] ** 2 + 5 * xs[i] + 140 - ys[i] + P))
#             ys.append(ys[i] + h * (a * (b * xs[i] - ys[i])))
#
#     return times, xs, ys


# Model 3 zmiennych
def model():
    T = 20
    h = 0.01
    x0 = 1.
    y0 = 0.3
    z0 = 2.


    times = createArray(0, T, h)
    xs = [x0]
    ys = [y0]
    zs = [z0]

    s = 10
    r = 28
    b = 8/3


    for i in range(0, len(times) - 1):
        xs.append(xs[i] + h * (s * (ys[i] - xs[i])))
        ys.append(ys[i] + h * (r * xs[i+1] - ys[i] - xs[i+1] * zs[i]))
        zs.append(zs[i] + h * (-1 * b * zs[i] + xs[i+1] * ys[i+1]))

    return times, xs, ys, zs


# def drawPlot(times, xs, ys):
#     pt.figure(1)
#     #gorny wykres
#     pt.subplot(211)
#     #wykres od czasu
#     pt.plot(times, xs, times, ys)
#     #dolny wykres
#     pt.subplot(212)
#     #wykres stanu
#     pt.plot(xs, ys)
#     #punkt początku
#     pt.plot(xs[0], ys[0], "bo")
#     #punkt końca
#     pt.plot(xs[len(xs) - 1], ys[len(xs) - 1], "ro")
#     pt.show()

def drawPlot(times, xs, ys, zs):
    pt.figure(1)
    #gorny wykres
    pt.subplot(211)
    #wykres od czasu
    pt.plot(times, xs, times, ys, times, zs)
    #dolny wykres
    pt.subplot(212)
    #wykres stanu
    pt.plot(xs, ys)
    #punkt początku
    # pt.plot(xs[0], ys[0], "bo")
    #punkt końca
    # pt.plot(xs[len(xs) - 1], ys[len(xs) - 1], "ro")
    pt.show()

def runAnimation(times, xs, ys):

    screenSize = (960, 640)

    SCALE = 200
    OFSET = (int(screenSize[0]/2), int(screenSize[1]/2))

    screen = pygame.display.set_mode(screenSize)
    clock = pygame.time.Clock()

    arraySize = len(times) - 1
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
        #ś
        pygame.draw.circle(screen, (255,255,255),(OFSET[0] + int(SCALE * xs[counter]),OFSET[1] ), 20)
        pygame.draw.circle(screen, (0,255,255),(OFSET[0] + int(SCALE * ys[counter]),OFSET[1] + 20 ), 20)

        pygame.draw.circle(screen, (40, 40, 40), (OFSET), 5)
        pygame.display.flip()
        if(counter >= arraySize):
            counter = 0
        else:
            counter += 1
        print(xs[counter])

times, xs, ys, zs = model()
drawPlot(times, xs ,ys, zs)
runAnimation(times, xs, ys)