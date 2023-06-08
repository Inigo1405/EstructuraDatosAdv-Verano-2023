from nodo import Nodo

class ListaLigada():
    def __init__(self):
        self.cabeza = None 
        """Apuntador del inicio de la lista ligada"""


    def agregar(self, nodo):
        if self.cabeza:
            ultimo_nodo = self.cabeza

            while ultimo_nodo.siguiente != None:
                ultimo_nodo = ultimo_nodo.siguiente
            ultimo_nodo.siguiente = Nodo(nodo)

        else:
            self.cabeza = Nodo(nodo)



    def agregar_inicio(self, nodo):
        primer_nodo = self.cabeza
        self.cabeza = nodo
        nodo.siguiente = primer_nodo



    def agregar_pos(self, nodo, pos):
        if self.cabeza:
            if pos == 0:
                self.agregar_inicio(nodo)
        
            elif pos < 0:
                print("No acepto valores negativos :(")

            else:
                i = 1
                nodo_actual = self.cabeza
                while i < pos and nodo_actual.siguiente != None:
                    nodo_actual = nodo_actual.siguiente
                    i += 1
                
                Nodo(nodo).siguiente = nodo_actual.siguiente # En este caso el nodo anterior y el nuevo apuntan al siguiente,  3 → 5;  3  4 → 5
                nodo_actual.siguiente = Nodo(nodo)

        else:
           print("Aún no tengo datos :(")



    def display(self):
        nodo_actual = self.cabeza

        while nodo_actual != None:
            print(f'{nodo_actual.dato}', end=" → ")
            nodo_actual = nodo_actual.siguiente

        print('Null\n')
        return self.cabeza



    def eliminar_pos(self, pos):
        if self.cabeza:
            if pos == 0:
                self.cabeza = self.cabeza.siguiente
            
            elif pos > 0:
                i = 0
                actual_nodo = self.cabeza
                
                while i < pos:
                    nodo_anterior = actual_nodo
                    actual_nodo = actual_nodo.siguiente
                    i += 1

                print(F'Te encontre! pos: {i}, dato: {actual_nodo.dato}')
                siguiente_nodo = actual_nodo.siguiente
                nodo_anterior.siguiente = siguiente_nodo

        else:
            print("Aún no tengo datos :(")
          



ll = ListaLigada()



ll.agregar(5)
ll.agregar(6)
ll.agregar(7)


ll.agregar_inicio(Nodo(1))
ll.agregar_pos(8, 9)



ll.display()

ll.eliminar_pos(3)



ll.display()




