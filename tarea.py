# Iñigo Quintana Delgadillo
# 18/06/2023


# Modificar gran parte del código para que tenga un menu para que el usuario 
# diga cuantos datos quiere, que se ordene la lista, 
# y pedirle al usuario el dato que quiere encontrar

import random

def busquedaBinaria(lista, dato):
     i = 0
     primero = 0
     ultimo = len(lista)-1
     encontrado = False

     while primero <= ultimo and not encontrado:
          central = (primero + ultimo) // 2  # Nos quedamos con la part entera de la division
          #print(central)
          i += 1
          
          if lista[central] == dato:
               encontrado = True

          else:
               if dato < lista[central]:
                    ultimo = central -1
               else:
                    primero = central +1

     print(f"Pasos: {i}")
     return central if encontrado else None



def partition(lista):
     if lista:

          mayores=list()
          iguales=list()
          menores=list()
          p =  random.randint(0, len(lista)-1)

          #! Dividir
          for i in lista:
               if i > lista[p]:
                    mayores.append(i)
                    
               elif i < lista[p]:
                    menores.append(i)

               else:
                    iguales.append(i)


          # print(menores)
          # print(iguales)
          # print(mayores)
          # print(lista)

         #! Ordena con recursion
          return partition(menores) + [iguales] + partition(mayores) 


     else: 
          return lista


def menu():
     print("\n1. Número de datos en el arreglo")
     print("2. Ordenar datos del arreglo")
     print("3. Buscar dato deseado")
     print("4. Fin del programa")


def crearLista():
     arr = list()
     tam = None

     while type(tam) != int:
          try: 
               tam = int(input("Ingresa el tamaño del arreglo: "))
          except:
               print("Ingrese un número")


     for i in range(tam):
          num = random.randint(0, 50)
          arr.append(num)


     p =  random.randint(0, len(arr)-1)
     #print(arr[p])
     print(arr)
     #partition(arr)
     return arr



# -- Menu -- 
fin = False
opc = None
arr = None

while fin == False:
     menu()

     try:
          opc = int(input("Ingresa la opción deseada: "))
     except:
          print("Ingresa un número")
     
     #Crear lista
     if opc == 1:
          arr = crearLista()
     
     #Ordenar lista
     elif opc == 2:
          if arr:
               arr = partition(arr)
               print(arr)

          else:
               print("La lista no existe!")

     #Buscar dato
     elif opc == 3:
          if arr:
               print(arr)
               dato = int(input("Ingresa el dato a buscar: "))
               busquedaBinaria(arr, dato)

          else:
               print("La lista no existe!")

     #Terminar programa
     elif opc == 4:
          fin = True




