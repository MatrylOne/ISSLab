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
    a = 5

    calka = 0

    # Symulacja wypełniająca tablice
    for i in range(0, len(times) - 1):
        ys.append(ys[i] + h * (a * ys[i] + us[i]))
        es.append(d - ys[i + 1])
        calka += (es[i]) * h
        us.append(kp * es[i+1] + kd * ((es[i+1] - es[i])/h) + ki * calka)

    return (times, ys, es, us, (kp, ki, kd))

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
        error = mh.calculatePowerDerivative(data[0], data[2])
        print(error)
        derivaties.append(error)

    choosen = min(derivaties)
    print(choosen)
    return derivaties.index(min(derivaties))


# WYWOŁYWANIE METOD
print("generating data")
datas = generateModels(8., 0.01, 0, 0, 1, (0, 300), (0, 50), (0,0.8), 10000)
best = countQuality(datas)

bestDatas = [datas[best]]
print(bestDatas[0][4])

plot = mpt.IssPlot(bestDatas)
plot.pointPlot(1)
plot.pointSub(1)
plot.statePlot([0, 1], False, False, "y")
plot.drawLine(0, 1)
plot.pointSub(2)
plot.statePlot([0, 2], False, False, "e")
plot.pointSub(3)
plot.statePlot([0, 3], False, False, "u")
plot.show()