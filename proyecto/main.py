from qt import *
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QRect, QPoint
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor, QIcon

import math
from lista_adyacencia import Graph
from cola import Queue
import img_rc

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow, QWidget):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Proyecto final Grafos | Iñigo Q D")
        self.setWindowIcon( QIcon(":/cct/grafosback.png"))
        
        self.vertexAdd = False
        self.edgeAdd = False

        self.g = Graph(0)

        #self.display.clicked.connect(self.button_clicked)
        self.cleanAll.clicked.connect(self.clear_graph)
        
        self.addVertex.clicked.connect(self.addButton_vertex)
        self.delVertex.clicked.connect(self.delButton_vertex)
        
        self.addEdge.clicked.connect(self.addButton_edge)
        self.delEdge.clicked.connect(self.delButton_edge)

        self.statusbar.showMessage("Ready!")

        self.listABC = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

        
        self.x = 0
        self.y = 0
        self.click = False

        self.circles = []
        self.hitBox = []

        self.edges = []
        self.nodeEdges = []

        self.coordsLine = []
        self.vertexes = []
        
        #Para pintar en el widget canvas
        self.canvas.mousePressEvent = self._mousePressEvent
        self.canvas.paintEvent = self.paintEvent


    def clear_graph(self):
        self.circles = []
        self.hitBox = []
        self.edges = []
        self.coordsLine = []
        self.nodeEdges = []
        self.g.graph = {}
        
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

            clicked_pos = event.pos()
            self.x = clicked_pos.x()
            self.y = clicked_pos.y()
            self.click = True

            v = self.search_vertex()
            self.coordsLine.append(v)

            self.del_vertex()
            self.del_edge()
            
            #self.statusbar.showMessage(f'{self.x} , {self.y}')
            self.canvas.update()
            


    def paintEvent(self, event):
        self.graph()

        diameter = 50
        radius = int(diameter/2)
        
        painter = QPainter(self.canvas)
        painter.setPen(QPen(QtCore.Qt.black, 3, QtCore.Qt.SolidLine))
        painter.setBrush(QBrush(QtCore.Qt.blue, QtCore.Qt.SolidPattern))
        
        
        collisionShape = radius*3
        print(self.canvas.rect())
        
        #Agregar nodos
        if self.click and self.hitBox_area() and self.vertexAdd:
            #painter.drawEllipse(self.x-radius, self.y-radius, diameter, diameter)
            self.circles.append((self.x-radius, self.y-radius))
            self.hitBox.append((self.x+(collisionShape), self.y+(collisionShape), self.x-(collisionShape), self.y-(collisionShape)))
        

        #Agregar conexiones
        if self.edgeAdd and self.click and len(self.coordsLine) == 2:
            node1 = self.coordsLine[0]
            node2 = self.coordsLine[1]
            
            if node1 != None and node2 != None:
                x1, y1 = self.circles[node1]
                x2, y2 = self.circles[node2]
                
                self.edges.append((x1+radius, y1+radius, x2+radius, y2+radius, node1, node2))

                
                v = self.listABC[node1]
                w = self.listABC[node2]


                #ToDo Elaborar una función que saque el peso entre puntos
                #ToDo para que funcione el recorrido dijkstra. 

                #self.edgeWeight(x1, y1, x2, y2)


                if self.listABC.index(v) < self.listABC.index(w):
                    if (v, w) not in self.nodeEdges:
                        self.nodeEdges.append((v, w))

                else:
                    if (w, v) not in self.nodeEdges:
                        self.nodeEdges.append((w, v))

            print(self.nodeEdges)
            self.coordsLine = []
            


        self.click = False
        for i in range(len(self.edges)):
            x1, y1, x2, y2, v, w = self.edges[i]
            painter.drawLine(x1, y1, x2, y2)
        

        for i in range(len(self.circles)):
            x, y = self.circles[i]
            painter.drawEllipse(x, y, diameter, diameter)

            painter.drawText(x+radius-5, y+radius+5, self.listABC[i])
        
        painter.end()
            

    
    def edgeWeight(self, v, w):
        i = self.listABC.index(v)
        j = self.listABC.index(w)

        #ToDo Elaborar una función que saque el peso entre puntos
        #ToDo para que funcione el recorrido dijkstra.
         
        x1, y1 = self.circles[i]
        x2, y2 = self.circles[j]
        
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        
    

    #Identifica el nodo seleccionado
    def search_vertex(self):
        if self.hitBox != []:
            for i in range(len(self.hitBox)):
                x1, y1, x2, y2 = self.hitBox[i]

                if self.x < x1 and self.x > x2 and self.y <= y1 and self.y >= y2:
                    print(f"Nodo: {self.listABC[i]}") 
                    return i
                    
                    

    #Identifica las hitBox de los nodos 
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
        

        
    #Elimina los nodos
    def del_vertex(self):
        if self.circles != [] and self.vertexAdd == False:
            x = self.search_vertex()
            if x != None:
                self.hitBox.pop(x)
                self.circles.pop(x)
                
            self.update()



    #Elimina los vertices
    def del_edge(self):
        if self.edges != [] and self.edgeAdd == False:
            x = self.search_vertex()
            if x != None:
                lista = []
                for i in range(len(self.edges)):
                    if x == self.edges[i][4] or x == self.edges[i][5]:
                        lista.append(i)

                lista = sorted(lista, reverse=True)
                for i in range(len(lista)):
                    self.edges.pop(lista[i])

            self.update()

    

    def graph(self):
        if len(self.circles) > 1 and self.nodeEdges != []:
            self.g = Graph(len(self.circles))
            self.g.graph = {}

            for i in range(len(self.circles)):
                if i < len(self.listABC):
                    self.g.add_vertex(self.listABC[i])
                

           
            self.ABC_order()


            for i in self.g.keys:
                self.g.display(i)

            empty = []
            emptyQueue = Queue()
            print("\nRecorrido BFS")
            self.g.recorrido('A', empty, emptyQueue)


            empty = []
            print("\n\nRecorrido DFS")
            self.g.recorridoRecursivo('A', empty)

            
            print()
            self.g.displayMatrix()

    
    def ABC_order(self):
        index = []
        for i in range(len(self.circles)):
            index = []
            for edge in self.nodeEdges:
                v, w = edge

                if self.listABC[i] == v:
                    index.append(self.listABC.index(w))
                    index = sorted(index)
            
            self.vertexes.append(index)
            
            for j in range(len(self.vertexes[i])):
                p = self.edgeWeight(self.listABC[i], self.listABC[self.vertexes[i][j]])
                
                self.g.add_edge(self.listABC[i], self.listABC[self.vertexes[i][j]], p)


        self.vertexes = []

            
                    
                
                

                
        


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
    