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




arr2 = [1,3,5,6,7,8,9,10]
print(arr2)
busquedaBinaria(arr2, 9)