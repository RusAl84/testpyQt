import random
import sys
from PyQt5 import uic
#from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, qApp, QGridLayout, QLineEdit, QSizePolicy, \
    QHBoxLayout
import calc
import time
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pyqtgraph.examples

class canvas(QMainWindow):
    def __init__(self, parent=None):
        super(canvas, self).__init__(parent)
        self.setGeometry(100, 100, 1000, 700)

class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()

    def plot(self):
        data = [random.random() for i in range(25)]
        ax = self.figure.add_subplot(111)
        ax.plot(data, 'r-')
        ax.set_title('PyQt Matplotlib Example')
        self.draw()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = uic.loadUi('./main2UI.ui', self)
        self.ui.pushButton_3.clicked.connect(self.btn3_on_click)
        self.ui.pushButton_1.clicked.connect(self.btn1_on_click)
        self.ui.w = self.ui.widget1
        m = PlotCanvas(self.ui.widget1, width=5, height=4)
        m.move(0, 0)

    def btn3_on_click(self):
        line_edit = QLineEdit(self)
        value1 = self.ui.lineEdit_1.text()
        value2 = self.ui.lineEdit_2.text()
        self.ui.lineEdit_3.setText(value1+value2)
        window2 = calc.MainWindow()
        window2.show()
        window2.ui.lineEdit_3.setText("Dima")
        window2.ui.data="Petya"

    def btn1_on_click(self):

        pyqtgraph.examples.run()
        print("v")


    #



if __name__ == '__main__':
    app = QApplication(sys.argv)
    #app.setStyle("plastique")
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())