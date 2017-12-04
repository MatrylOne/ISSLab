import pygame
import helpers.animationHelper as ah

class Animation(object):
    def __init__(self, datas, undoSteps, screenSize, adjustScale):
        self.screenSize = screenSize
        self.undoSteps = undoSteps

        objects = ah.convertDatasToObjects(datas)
        SCALE, OFFSET = ah.calculateTransform(objects, self.screenSize, adjustScale)

        self.objects = ah.transformObjects(objects, SCALE, OFFSET)
        pass

    def runAnimation(self):
        screen = pygame.display.set_mode(self.screenSize)
        clock = pygame.time.Clock()

        stepCounter = 0
        running = True

        colors = ah.generateColors(len(self.objects) + 1, 127, 255)

        # tutaj trzeba transformować
        # pozycje = ah.convertModelsToPoints(self.objects, SCALE, OFSET)

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
            for object in self.objects:

                startStepper = 0
                if(stepCounter > self.undoSteps):
                    startStepper = stepCounter - self.undoSteps

                # Rysowanie strokeów
                if (stepCounter > 2):
                    pygame.draw.aalines(screen, (100,100,100), False, object[startStepper:stepCounter])
                # Rysowanie punktów
                pygame.draw.circle(screen, (0, 0, 0), object[stepCounter], 1)

            # Wyświetlenie powyżej wypełnionej klatki
            pygame.display.flip()

            # Zapętlenie animacji po przejściu po całej tablicy
            if(stepCounter >= len(self.objects[0]) - 1):
                stepCounter = 0
            else:
                stepCounter += 1
        pass