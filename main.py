import sys
from PyQt5 import uic
#from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, qApp, QLineEdit
import calc

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = uic.loadUi('./main2UI.ui', self)
        self.pushButton_3.clicked.connect(self.btn3_on_click)

    def btn3_on_click(self):
        line_edit = QLineEdit(self)
        value1 = self.ui.lineEdit_1.text()
        value2 = self.ui.lineEdit_2.text()
        self.ui.lineEdit_3.setText(value1+value2)

        window2 = calc.MainWindow()
        window2.show()
        window2.ui.lineEdit_3.setText("Dima")

    #



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("plastique")
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())