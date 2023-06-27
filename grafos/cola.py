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
          if self.items:
               return self.items.pop(0)                       # Eliminamos el primer elemento
          

     #Si esta vacía
     def is_empty(self):
          return True if self.items else False    # if Ternarios
     

     def display(self):
          print(self.items)
          return self.items

     def datos(self):
          return self.items

     def tamaño(self):
          return len(self.items)


     def ubicacion(self, pos):
          # print(self.items[pos])
          return self.items[pos]

     def insertar(self, pos, dato):
          self.items.pop(pos)
          self.items.insert(pos, dato)

     
     def ordenamiento(self):
          n = len(self.items)
          for i in range(n-1):
               for j in range(n-1):
                    if self.items[j] > self.items[j+1]:
                         tmp = self.items[j]
                         self.items[j] = self.items[j+1]
                         self.items[j+1] = tmp
          
          return self.items

     

     def buscarDato(self, lista, dato):
          if lista:
               for i in range(len(self.items)):
                    if self.items[i] == dato:
                         print(f"El dato en la posición: {i} en el ciclo {i+1}")
                         
          else:
               return None