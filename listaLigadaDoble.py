from nodo import Nodo

class ListaLigadaDoble():
    def __init__(self):
        self.cabeza = None 
        """Apuntador del inicio de la lista ligada"""


    def agregar_inicio_der(self, nodo):
        primer_nodo = self.cabeza
        self.cabeza = nodo
        nodo.siguiente = primer_nodo
    
    
    def agregar_inicio_izq(self, nodo):
        primer_nodo = self.cabeza
        self.cabeza = nodo
        nodo.anterior = primer_nodo


    def agregar_pos(self, nodo, dir, pos):
        if self.cabeza:
            if dir == 'der':
                if pos == 0:
                    self.agregar_inicio_der(nodo)
            
                elif pos < 0:
                    print("No acepto valores negativos :(")

                else:
                    i = 1
                    nodo_actual = self.cabeza
                    while i < pos and nodo_actual.siguiente != None:
                        nodo_actual = nodo_actual.siguiente
                        i += 1
                    
                    nodo.siguiente = nodo_actual.siguiente 
                    nodo_actual.siguiente = nodo


            if dir == 'izq':
                pass

        else:
           print("Aún no tengo datos :(")


    def display(self):
        nodo_actual = self.cabeza

        while nodo_actual != None:
            print(f'{nodo_actual.dato}', end=" → ")
            nodo_actual = nodo_actual.siguiente

        print('Null\n')
        return self.cabeza
            




lld = ListaLigadaDoble()

lld.agregar_inicio_izq(Nodo(1))
lld.agregar_inicio_izq(Nodo(7))

lld.agregar_inicio_der(Nodo(2))
lld.agregar_inicio_der(Nodo(3))
    

lld.display()