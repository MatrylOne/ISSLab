import helpers.animationHelper as ah
import helpers.modelHelper as mh
import helpers.issAnimation as anim
import helpers.issPlot as mpt
import pygame

from helpers import issPlot as pt


### METODY POMOCNICZE ###
def showPlot():
    pt.show()
    pass

### GŁÓWNE METODY ###
def model(T, h, x0, y0):
    # Inicjacja tablic
    times = mh.createArray(0, T, h)
    xs = [x0] #y
    ys = [y0] #u

    a = -1./2.
    d = 0.4
    treshhold = 0.05
    speed = 1

    lastRising = True


    # Symulacja wypełniająca tablice
    for i in range(0, len(times) - 1):
            # xs.append(xs[i] + h * (    ))
            # ys.append(ys[i] + h * (    ))
        if not lastRising and d - treshhold - xs[i] > 0:
            lastRising = True
            print("Treshold passed. Start rising")
        elif lastRising and d + treshhold - xs[i] <= 0:
            lastRising = False
            print("Treshold passed. Stop rising")

        if lastRising :
            ys.append(speed)
            print("Rising")
        else:
            ys.append(0)
            print("Falling")
            print(3)
        xs.append(xs[i] + h * (  a * xs[i] +  ys[i+1] ))
    return (times, xs, ys)

def generateModels(T, h, xRange, yRange, iterations):
    # Inicjacja tablicy wyników
    datas = []
    # Losowanie
    for i in range(0, iterations):
        datas.append(model(T, h, mh.randomRange(xRange), mh.randomRange(yRange)))
    return datas

### WYWOŁYWANIE METOD ###
print("generating data")
datas = generateModels(5, 0.001, (0, 0), (0, 0), 1)
plot = mpt.IssPlot(datas)
plot.pointPlot(1)
plot.pointSub(1)
plot.statePlot([0, 1], False, False)
plot.pointSub(2)
plot.statePlot([0, 2], False, False)
plot.show()
animation = anim.Animation(datas, 1000, (1200,600), 1)
animation.runAnimation()