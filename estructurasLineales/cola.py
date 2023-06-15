class Queue():
     """
     Class Cola Dinámica
     ---------
     Clase que contiene las funciones para manejar una cola:
     * `enqueue`: agregar dato
     * `dequeue`: eliminar dato
     * `is_empty`: comprobar si esta vacío
     * `display`: imprimir lista
     """
     
     # Crear cola_vacía
     def __init__(self):
          self.items = list()
          

     # Insertar (Encolar)
     def enqueue(self, x):
          """Insertar datos en la cola"""
          self.items.append(x)


     # Eliminar (Desencolar)
     def dequeue(self):
          """Eliminar datos de la cola"""
          return self.items.pop(0)                       # Eliminamos el primer elemento
          

     #Si esta vacía
     def is_empty(self):
          return True if self.items else False    # if Ternarios
     

     def tamaño(self):
          return len(self.items)


     def ubicacion(self, pos):
          # print(self.items[pos])
          return self.items[pos]

     def insertar(self, pos, dato):
          self.items.insert(pos, dato)

     def display(self):
          print(self.items)
          return self.items
     
     def ordenamiento(self):
          n = len(self.items)
          for i in range(n-1):
               for j in range(n-1):
                    if self.items[j] > self.items[j+1]:
                         tmp = self.items[j]
                         self.items[j] = self.items[j+1]
                         self.items[j+1] = tmp
          
          return self.items
