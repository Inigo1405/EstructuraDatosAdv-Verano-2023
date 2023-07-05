from qt import *
from PyQt5 import Qt

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.Display.clicked.connect(self.button_clicked)
        #self.statusbar.showMessage("Ready!")
        
    def button_clicked(self):
        print("Hola Mundo!")
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
    