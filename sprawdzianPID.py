import helpers.animationHelper as ah
import helpers.modelHelper as mh
import helpers.issAnimation as anim
import helpers.issPlot as mpt
import pygame

# GŁÓWNE METODY
def model(T, h, y0, u0, d, kd):
    # Inicjacja tablic
    times = mh.createArray(0, T, h)

    kp = 30
    ki = 5
    kd = 0.2

    ys = [y0]
    es = [d - y0]
    us = [u0]

    a = -0.5

    calka = 0

    # Symulacja wypełniająca tablice
    for i in range(0, len(times) - 1):
        ys.append(ys[i] + h * (a * ys[i] + us[i]))
        es.append(d - ys[i + 1])
        calka += (es[i]) * h
        us.append(kp * es[i+1] + kd * ((es[i+1] - es[i])/h) + ki * calka)


    return (times, ys, es, us)

def generateModels(T, h, xRange, yRange, iterations):
    # Inicjacja tablicy wyników
    datas = []
    # Losowanie
    for i in range(0, iterations):
        datas.append(model(T, h, mh.randomRange(xRange), mh.randomRange(yRange)))
    return datas

# WYWOŁYWANIE METOD
print("generating data")
data = [model(2., 0.01, 0., 0., 1., 1.1)]
print(mh.calculateDerivative(data[0][0], data[0][2]))

plot = mpt.IssPlot(data)
plot.pointPlot(1)
plot.pointSub(1)
plot.drawLine(0, 1)
plot.statePlot([0, 1], False, False)
plot.pointSub(2)
plot.drawLine(0, 1)
plot.statePlot([0, 2], False, False)
plot.pointSub(3)
plot.drawLine(0, 1)
plot.statePlot([0, 3], False, False)
plot.show()