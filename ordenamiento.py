from estructurasLineales.cola import Queue
import random

# Ordenamiento de datos de menor a mayor
# 14/06/2023



def burbuja(lista):
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


arr = Queue()

for i in range(15):
    num = random.randint(1, 100)
    arr.enqueue(num)


arr.display()
#Burbuja(arr)
#burbuja(arr)
arr.ordenamiento()
arr.display()

