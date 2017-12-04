import numpy as np
import matplotlib.pyplot as pyplot
import pygame

#kulka która zmienia rozmiar
#x wielkość serca

def model(initPosition, initAcceleration, attentionValue, accelerationValue, step, totalTime):

    times = np.arange(0.0, totalTime, step)
    positions = np.zeros(times.shape[0])
    accelerations = np.zeros(times.shape[0])

    positions[0] = initPosition
    accelerations[0] = initAcceleration

    for i in range(0, times.shape[0] - 1):
        positions[i + 1] = positions[i] + step * accelerations[i]
        accelerations[i + 1] = accelerations[i] + step * (- accelerationValue * np.sin(positions[i + 1]) - attentionValue * accelerations[i])

    return times, positions, accelerations

def drawChart(times, positions, accelerations):
    pyplot.plot(positions, accelerations)
    pyplot.show()

def runAnimation(times, xs, ys):

    screenSize = (960, 640)

    SCALE = 300
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
        pygame.draw.circle(screen, (255,255,255),(x, 0 + OFSET[1]), 20)
        pygame.draw.circle(screen, (40, 40, 40), (OFSET), 5)
        pygame.display.flip()
        if(counter >= arraySize):
            counter = 0
        else:
            counter += 1
        print(xs[counter])

times, positions, accelerations = model(1, 0, 0.5, 1, 0.1, 30)
drawChart(times, positions, accelerations)
runAnimation(times, positions ,accelerations)