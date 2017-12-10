import helpers.animationHelper as ah
import helpers.modelHelper as mh
import helpers.issAnimation as anim
import pygame

from helpers import issPlot as pt


### METODY POMOCNICZE ###
def showPlot():
    pt.show()
    pass

### GŁÓWNE METODY ###
def model(T, h, x0, y0, z0):
    # Inicjacja tablic
    times = mh.createArray(0, T, h)
    xs = [x0]
    ys = [y0]
    zs = [z0]

    s = 10
    r = 28
    b = 8/3

    # Symulacja wypełniająca tablice
    for i in range(0, len(times) - 1):
            # xs.append(xs[i] + h * (    ))
            # ys.append(ys[i] + h * (    ))
        xs.append(xs[i] + h * (s * (ys[i] - xs[i])))
        ys.append(ys[i] + h * (r * xs[i+1] - ys[i] - xs[i+1] * zs[i]))
        zs.append(zs[i] + h * (-1 * b * zs[i] + xs[i+1] * ys[i+1]))
    return (times, xs, ys, zs)

def generateModels(T, h, xRange, yRange, zRange, iterations):
    # Inicjacja tablicy wyników
    datas = []
    # Losowanie
    for i in range(0, iterations):
        datas.append(model(T, h, mh.randomRange(xRange), mh.randomRange(yRange), mh.randomRange(zRange)))
    return datas

### WYWOŁYWANIE METOD ###
print("generating data")
datas = generateModels(5, 0.001, (-20, -10), (-10, 10), (-10, 10), 1000)
animation = anim.Animation(datas, 100, (1200,600), 1)
animation.runAnimation()