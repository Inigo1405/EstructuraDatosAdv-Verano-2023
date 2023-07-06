from qt import *
from PyQt5 import Qt

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.display.clicked.connect(self.button_clicked)
        self.statusbar.showMessage("Ready!")
        self.x = 0
        self.y = 0
        
        
    def button_clicked(self):
        print("Hola Mundo!")
        
        
    def show_pos(self, click):
        print(f"Left button pressed")
        
        
    def mouseEvent():
        pass
    
    
    def paintEvent(self, event):
        pass
    
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
    