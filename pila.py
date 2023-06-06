class Pila():
     """
     Class Pila Dinámica (stack)
     ---------
     Clase que contiene las funciones para manejar una pila:
     * `push`: agregar dato
     * `pop`: eliminar dato
     * `is_empty`: comprobar si esta vacío
     * `display`: imprimir lista
     """
     
     # Crear pila_vacía
     def __init__(self):
          self.items = []


     # Insertar dato al final de la lista (top)
     def push(self, x):
          """Agrega datos a la pila"""
          self.items.append(x)


     # Extraer el último dato
     def pop(self):
          """Elimina datos de la pila"""
          if self.is_empty():
               print("La pila ya esta vacía", self.items)
          else:
               return self.items.pop()
          

     # Pregunta si esta vacía la lista
     def is_empty(self):
          if self.items:
               return False
          else:
               return True
     

     # Imprime la pila
     def display(self):
          print(self.items)
          return self.items