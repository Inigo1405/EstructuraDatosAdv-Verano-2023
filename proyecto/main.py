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
        # alert = QMessageBox()
        # alert.setText("Click DFS")
        # alert.exec_()
        print("Hola Mundo")

    def show_pos(self, click):
        print(f"Button pressed: X:{click.x()}, Y:{click.y()}")
        self.point = [click]
        self.x = click.x()
        self.y = click.y()

    def mousePressEvent(self, event):

        if event.button() == Qt.LeftButton:
            clicked_pos = event.pos()
            self.show_pos(clicked_pos)
            self.update()
            

        elif event.button() == Qt.RightButton:
            clicked_pos = event.pos()
            self.show_pos(clicked_pos)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.blue, 1, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
        painter.drawEllipse(self.x, self.y, 40,40)
        painter.end()
    
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
    