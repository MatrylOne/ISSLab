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

    d = 1

    xs = [x0] #y
    ys = [y0] #u
    es = [d - xs[0]]
    całka = es[0]*h
    kp = 1
    ki = 0.9
    kd = 0.5

    a = -1./2.

    # Symulacja wypełniająca tablice
    for i in range(0, len(times) - 1):
        es.append(d - xs[i])
        xs.append(xs[i] + h * (  a * xs[i] +  ys[i] ))
        całka += es[i + 1]*h

        ys.append(kp * (es[i+1]) + ki * (całka) + kd * ((es[i+1] - es[i])/h))
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
# animation = anim.Animation(datas, 1000, (1200,600), 1)
# animation.runAnimation()