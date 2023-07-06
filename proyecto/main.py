from qt import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QBrush

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.display.clicked.connect(self.button_clicked)
        self.statusbar.showMessage("Ready!")
        self.x = 0
        self.y = 0
        
        
    def button_clicked(self):
        print("Hola Mundo")



    def show_pos(self, click):
        print(f"Left button pressed: X:{click.x()}, Y:{click.y()}")
        self.statusbar.showMessage(f"X:{click.x()}, Y:{click.y()}")
        self.point = [click]
        self.x = click.x()
        self.y = click.y()
        self.update()



    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            clicked_pos = event.pos()
            self.show_pos(clicked_pos)
            self.update()
            
        elif event.button() == Qt.RightButton:
            print("Right button pressed")
            # clicked_pos = event.pos()
            # self.show_pos(clicked_pos)



    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setPen(QtGui.QPen(QtCore.Qt.blue, 1, QtCore.Qt.SolidLine))
        painter.setBrush(QtGui.QBrush(QtCore.Qt.blue, QtCore.Qt.SolidPattern))
        painter.drawEllipse(self.x, self.y, 40, 40)
        painter.end()
    
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
    