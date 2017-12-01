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
        datas.append(model(T, h, mh.randomRange(xRange), mh.randomRange(yRange)))
    return datas

### WYWOŁYWANIE METOD ###
print("generating data")
datas = generateModels(10, 0.001, (-5, 5), (-1, 2), 500)
# plot = mpt.IssPlot(datas)
# plot.statePlot([1,2], False, False)
# plot.show()
animation = anim.Animation(datas, 100, (1200,600), 1)
animation.runAnimation()