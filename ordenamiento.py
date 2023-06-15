from estructurasLineales.cola import Queue
import random

# Ordenamiento de datos de menor a mayor
# 14/06/2023



def _burbuja(lista):
    n = lista.tamaño()
    for i in range(n-1):
        for j in range(n-1):
            #print(lista(0))
            if lista.ubicacion(j) > lista.ubicacion(j+1):
                tmp = lista.ubicacion(j)
                #print(tmp)
                lista.insertar(j, lista.ubicacion(j+1))
                lista.insertar(j+1, tmp)

    return tmp


def burbuja(lista):
    if lista:
        #lista = Queue()

        # 57, 77, 53, 23, 92, 13, 34, 83, 48, 6, 41, 3, 39, 18, 100
        # 48, 18, 41, 23, 39, 13, 100, 6, 53, 3, 92
        n = lista.tamaño()
        for i in range(n-1):
            for j in range(n-1):
                tmp1 = lista.dequeue()
                tmp2 = lista.dequeue()

                #print(tmp1)
                #print(tmp2)
                if tmp1 >= tmp2:
                    #print(tmp2)
                    lista.enqueue(tmp2)
                    lista.enqueue(tmp1)
                    
                
                else: 
                    lista.enqueue(tmp1)
                    lista.enqueue(tmp2)

        lista.display()
        return lista
    



arr = Queue()

for i in range(15):
    num = random.randint(1, 100)
    arr.enqueue(num)


arr.display()
#Burbuja(arr)


burbuja(arr)
arr.display()

#arr.ordenamiento()
#arr.display()


