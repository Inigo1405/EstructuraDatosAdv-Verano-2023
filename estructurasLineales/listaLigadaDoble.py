from nodo import Nodo

class ListaLigadaDoble():
    def __init__(self):
        self.cabeza = None 
        """Apuntador del inicio de la lista ligada"""

        self.cola = None
        """Apuntador del final de la lista ligada"""


    def displayCabeza(self):
        if self.cabeza:
            nodo_actual = self.cabeza
            print(f'{nodo_actual.anterior}', end=" ↔ ")

            while nodo_actual != None:
                print(f'{nodo_actual.dato}', end=" ↔ ")
                nodo_actual = nodo_actual.siguiente

            print(f'{nodo_actual}')
            return self.cabeza
    
    
    
    def displayCola(self):
        if self.cabeza:
            nodo_actual = self.cola
            print(f'{nodo_actual.siguiente}', end=" ↔ ")

            while nodo_actual != None:
                print(f'{nodo_actual.dato}', end=" ↔ ")
                nodo_actual = nodo_actual.anterior

            print(f'{nodo_actual}')
            return self.cola



    def agregar(self, nodo):
        nodo = Nodo(nodo)

        if self.cabeza:
            anterior_nodo = ultimo_nodo = self.cabeza
            
            while ultimo_nodo.siguiente != None:
                ultimo_nodo = ultimo_nodo.siguiente
                anterior_nodo = ultimo_nodo
            
            ultimo_nodo.siguiente = nodo
            ultimo_nodo = ultimo_nodo.siguiente

            self.cola = ultimo_nodo
            ultimo_nodo.anterior = anterior_nodo

            # print(ultimo_nodo.anterior.dato)
            # print(ultimo_nodo.dato)
            # print(ultimo_nodo.siguiente)
            
        else:
            self.cabeza = nodo



    def agregar_inicio(self, nodo, dir):
        if dir == 'der':
            primer_nodo = self.cabeza
            siguiente_nodo = primer_nodo.siguiente
            primer_nodo.siguiente = nodo
            nodo.siguiente = siguiente_nodo
            nodo.anterior = primer_nodo
            siguiente_nodo.anterior = nodo
            


        elif dir == 'izq':
            primer_nodo = self.cabeza
            self.cabeza = nodo
            nodo.siguiente = primer_nodo
            primer_nodo.anterior = nodo


        else: 
            print("Dirección no encontrada :(")



    def agregar_pos(self, nodo, dir, pos):
        nodo = Nodo(nodo)

        if self.cabeza:
            if pos == 0:
                self.agregar_inicio(nodo, dir)
            

            elif pos < 0:
                print("No acepto valores negativos :(")


            elif pos > 0:
                nodo_actual = self.cabeza
                i = 1
                while i <= pos and nodo_actual.siguiente != None:
                    nodo_actual = nodo_actual.siguiente
                    i += 1
                
                
                if nodo_actual.siguiente:
                    if dir == 'der':
                        nodo_siguiente = nodo_actual.siguiente
                        nodo_anterior = nodo_actual
                        
                        # print(nodo_actual.dato)
                        # print(nodo_actual.siguiente.dato)

                        nodo_actual.siguiente = nodo
                        nodo_actual = nodo_actual.siguiente

                        nodo_actual.siguiente = nodo_siguiente
                        nodo_actual.anterior = nodo_anterior
                        
                        
                        nodo_actual.siguiente.anterior = nodo_actual
                        


                    elif dir == 'izq':
                        nodo_anterior = nodo_actual.anterior
                        nodo_siguiente = nodo_actual

                        # print(nodo_actual.dato)
                        # print(nodo_actual.anterior.dato)

                        nodo_actual.anterior = nodo
                        nodo_actual = nodo_actual.anterior

                        nodo_actual.anterior = nodo_anterior
                        nodo_actual.siguiente = nodo_siguiente

                        nodo_actual.anterior.siguiente = nodo_actual
                        

                    else: 
                        print("Dirección no encontrada :(")


                elif dir == 'der' and nodo_actual.siguiente == None: 
                        nodo_actual.siguiente = nodo
                        nodo.anterior = nodo_actual
                        self.cola = nodo
                    

        else:
           print("Aún no tengo datos :(")

            


lld = ListaLigadaDoble()

lld.agregar(1)
lld.agregar(3)
lld.agregar(5)
lld.agregar(7)
lld.agregar(9)


lld.agregar_pos(20, 'izq', 1)   
lld.agregar_pos(15, 'der', 5)   

lld.displayCabeza()
lld.displayCola()



