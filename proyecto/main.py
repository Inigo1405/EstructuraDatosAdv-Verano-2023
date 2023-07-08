from qt import *
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QRect, QPoint
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor, QIcon
import img_rc

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow, QWidget):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Proyecto final Grafos | Iñigo Q D")
        self.setWindowIcon( QIcon(":/cct/grafosback.png"))
        
        self.vertexAdd = False
        self.edgeAdd = False


        #self.display.clicked.connect(self.button_clicked)
        self.cleanAll.clicked.connect(self.clear_graph)
        
        self.addVertex.clicked.connect(self.addButton_vertex)
        self.delVertex.clicked.connect(self.delButton_vertex)
        
        self.addEdge.clicked.connect(self.addButton_edge)
        self.delEdge.clicked.connect(self.delButton_edge)


        self.statusbar.showMessage("Ready!")

        self.listABC = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        self.listabc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        
        self.x = 0
        self.y = 0
        self.click = False

        self.circles = []
        self.hitBox = []
        self.edges = []
        
        self.coordsLine = []
        
        #Para pintar en el widget canvas
        self.canvas.mousePressEvent = self._mousePressEvent
        self.canvas.paintEvent = self.paintEvent



    def clear_graph(self):
        self.circles = []
        self.hitBox = []
        self.edges = []
        self.coordsLine = []
        
        self.statusbar.showMessage("Graph clean!")
        print(self.circles)
        self.update()



    def addButton_vertex(self):
        self.vertexAdd = True
        self.edgeAdd = None
        self.coordsLine = []
        

    def delButton_vertex(self):
        self.vertexAdd = False
        self.edgeAdd = None
        self.coordsLine = []


    def addButton_edge(self):
        if len(self.circles) > 1:
            self.edgeAdd = True
            self.vertexAdd = None
            self.coordsLine = []
        
        else:
            self.statusbar.showMessage("Deben existir dos nodos mínimo!")
        
        
    def delButton_edge(self):
        self.edgeAdd = False
        self.vertexAdd = None
        self.coordsLine = []


    def show_pos(self, click):
        print(f"Left button pressed: X:{click.x()}, Y:{click.y()}")
        self.statusbar.showMessage(f"X:{click.x()}, Y:{click.y()}")
        self.point = [click]
        self.x = click.x()
        self.y = click.y()
        self.update()



    def _mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            print("left button pressed")
            clicked_pos = event.pos()
            print(f"{clicked_pos}")
            self.x = clicked_pos.x()
            self.y = clicked_pos.y()
            self.click = True
            v = self.search_vertex()
            self.del_vertex()
            self.coordsLine.append(v)
            
            self.statusbar.showMessage(f'{self.x} , {self.y}')
            self.canvas.update()
            
        elif event.button() == Qt.RightButton:
            print("\nright button pressed")
            


    def paintEvent(self, event):
        diameter = 50
        radius = int(diameter/2)
        
        painter = QPainter(self.canvas)
        
        painter.setPen(QPen(QtCore.Qt.black, 3, QtCore.Qt.SolidLine))
        painter.setBrush(QBrush(QtCore.Qt.blue, QtCore.Qt.SolidPattern))
        
        
        collisionShape = radius*3
        print(self.canvas.rect())
        
        if self.click and self.hitBox_area() and self.vertexAdd:
            #painter.drawEllipse(self.x-radius, self.y-radius, diameter, diameter)
            
            self.circles.append((self.x-radius, self.y-radius))
            self.hitBox.append((self.x+(collisionShape), self.y+(collisionShape), self.x-(collisionShape), self.y-(collisionShape)))


        if self.edgeAdd and self.click and len(self.coordsLine) == 2:
            
            node1 = self.coordsLine[0]
            node2 = self.coordsLine[1]
            
            if node1 != None and node2 != None:
            
                x1, y1 = self.circles[node1]
                x2, y2 = self.circles[node2]
                
                self.edges.append((x1+radius, y1+radius, x2+radius, y2+radius))
            
            
            self.coordsLine = []
            

        self.click = False
        for i in range(len(self.edges)):
            x1, y1, x2, y2 = self.edges[i]
            painter.drawLine(x1, y1, x2, y2)
        
        

        for i in range(len(self.circles)):
            x, y = self.circles[i]
        
            painter.drawEllipse(x, y, diameter, diameter)
            try:
                painter.drawText(x+radius-5, y+radius+5, self.listABC[i])
            except:
                painter.drawText(x+radius-5, y+radius+5, self.listabc[i-len(self.listABC)])
        
        
        painter.end()
            


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

                if self.x <= x1 and self.x >= x2 and self.y <= y1 and self.y >= y2:
                    #print("No agregar!") 
                    return False
                
                else:
                    seguro = True
            
            if seguro:
                return True
        
        
        
    def del_vertex(self):
        if self.circles != [] and self.vertexAdd == False:
            x = self.search_vertex()
            print(x)
            if x != None:
                self.hitBox.pop(x)
                self.circles.pop(x)
                
            print(self.circles)
            print(self.circles)
            self.update()

        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
    