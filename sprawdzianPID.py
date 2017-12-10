import helpers.animationHelper as ah
import helpers.modelHelper as mh
import helpers.issAnimation as anim
import helpers.issPlot as mpt
import pygame

# GŁÓWNE METODY
def model(T, h, y0, u0, d, kp, ki, kd):
    # Inicjacja tablic
    times = mh.createArray(0, T, h)

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

def generateModels(T, h, y0, u0, d, kpRange, kiRange, kdRange, iterations):
    # Inicjacja tablicy wyników
    datas = []
    # Losowanie
    for i in range(0, iterations):
        datas.append(model(T, h, y0, u0, d, mh.randomRange(kpRange), mh.randomRange(kiRange),  mh.randomRange(kdRange)))
    return datas

def countQuality(datas):
    derivaties = []

    for data in datas:
        derivaties.append(mh.calculateErrorDerivative(data[0], data[2]))

    return derivaties.index(min(derivaties))


# WYWOŁYWANIE METOD
print("generating data")
# datas = generateModels(8., 0.01, 0, 0, 1, (0.01, 1000), (0.01, 50), (0,0.9), 10000)
data = model(.1, 0.01, 0, 0, 1, 20,  5, 0.1)
# best = countQuality(datas)
# print(datas[best][4])

# print(data[0:3])

plot = mpt.IssPlot(data)
plot.pointPlot(1)
plot.pointSub(1)
plot.statePlot([0, 1], False, False)
plot.pointSub(2)
plot.statePlot([0, 2], False, False)
plot.pointSub(3)
plot.statePlot([0, 3], False, False)
plot.show()