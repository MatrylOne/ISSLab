import matplotlib.pyplot as pt
import helpers.modelHelper as mh

class IssPlot(object):
    def __init__(self, datas):
        self.datas = datas
        pass

    def pointPlot(self, num):
        pt.figure(num)
        pass

    def pointSub(self, Index):
        pt.subplot(31*10 + Index)
        pass
    def timePlot(self):
        # Wykres wartości od czasu
        plots = []
        for i in range(1, len(self.datas[0])):
            newHandle, = pt.plot(self.datas[0][0], self.datas[0][i], label=i)
            plots.append(newHandle)
        pt.legend(handles=plots)
        pt.xlabel("czas")
        pt.ylabel("stan")
        pass

    def statePlot(self, indexes, showBegining, showEnd):
        for i in range(0, len(self.datas)):
            # Wykres stanu
            pt.plot(self.datas[i][indexes[0]], self.datas[i][indexes[1]])
            # Punkt początku
            if showBegining:
                pt.plot(self.datas[i][indexes[0]][0], self.datas[i][indexes[1]][0], "bo")
            # # Punkt końca
            if showEnd:
                pt.plot(self.datas[i][indexes[0]][len(self.datas[i][indexes[0]]) - 1], self.datas[i][indexes[1]][len(self.datas[i][indexes[1]]) - 1], "ro")
            # pt.plot(self.datas[i][1][len(self.datas[i][1]) - 1], self.datas[i][2][len(self.datas[i][2]) - 1], "ro")
        pass

    def drawLine(self, timeIndex, value):
        for i in range(0, len(self.datas)):
            valueArray = mh.createLineArray(self.datas[i][timeIndex], value)

            pt.plot(self.datas[i][timeIndex], valueArray)

    def show(self):
        pt.show()
        pass
