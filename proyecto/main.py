import sys
from qt import *
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QRect, QPoint
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow, QWidget):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Proyecto final Grafos | Iñigo Q D")
        
        self.vertexAdd = False


        #self.display.clicked.connect(self.button_clicked)
        self.cleanAll.clicked.connect(self.clear_graph)
        self.addVertex.clicked.connect(self.addButton_vertex)
        self.delVertex.clicked.connect(self.delButton_vertex)

        self.statusbar.showMessage("Ready!")

        self.listABC = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        self.listabc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        
        self.x = 0
        self.y = 0
        self.click = False

        self.circles = []
        self.hitBox = []



    def clear_graph(self):
        self.circles = []
        self.hitBox = []
        self.statusbar.showMessage("Graph clean!")
        print(self.circles)
        self.update()


    def delButton_vertex(self):
        self.vertexAdd = False


    def addButton_vertex(self):
        self.vertexAdd = True
        



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
            #print(self.canvas.rect())
            self.click = True
            self.search_vertex()

            self.update()
            
        elif event.button() == Qt.RightButton:
            print("Right button pressed")
            


    def search_vertex(self):
        if self.hitBox != []:
            for i in range(len(self.hitBox)):
                x1, y1, x2, y2 = self.hitBox[i]

                if self.x < x1 and self.x > x2 and self.y <= y1 and self.y >= y2:
                    try:
                        print(f"Nodo: {self.listABC[i]}") 
                        return i
                    
                    except:
                        print(f"Nodo: {self.listabc[i-len(self.listABC)]}")
                        return i



    def hitBox_area(self):
        if self.hitBox == []:
            print("Agregado")
            return True

        else:
            for hitBox in self.hitBox:
                x1, y1, x2, y2 = hitBox

                if self.x < x1 and self.x > x2 and self.y <= y1 and self.y >= y2:
                    #print("No agregar!") 
                    return False
                
                else:
                    seguro = True
            
            if seguro:
                return True
        
        
    def paintEvent(self, event):
        if self.click and self.vertexAdd:
            self.click = False
            #print("Painted")
            diameter = 40
            radius = int(diameter/2)
            
            painter = QtGui.QPainter(self)
            # Con esto pinta y quitando el background color
            #painter.fillRect(self.rect(), QColor(19, 19, 26))


            painter.setPen(QtGui.QPen(QtCore.Qt.white, 1, QtCore.Qt.SolidLine))
            painter.setBrush(QtGui.QBrush(QtCore.Qt.blue, QtCore.Qt.SolidPattern))
            collisionShape = radius*3
            
            if self.hitBox_area():
                painter.drawEllipse(self.x-radius, self.y-radius, diameter, diameter)
                self.circles.append((self.x-radius, self.y-radius))
                self.hitBox.append((self.x+(collisionShape), self.y+(collisionShape), self.x-(collisionShape), self.y-(collisionShape)))
        

            for i in range(len(self.circles)):
                x, y = self.circles[i]
                painter.drawEllipse(x, y, diameter, diameter)

                try:
                    painter.drawText(x+radius-3, y+radius+4, self.listABC[i])
                except:
                    painter.drawText(x+radius-3, y+radius+4, self.listabc[i-len(self.listABC)])
                
            painter.end()
    



    def del_vertex(self, event):
        print("Hola")
        if self.vertexAdd == False:
            x = self.search_vertex()
            self.hitBox.pop(x)
            self.circles.pop(x)

        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
    