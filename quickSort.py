import random

# Dividir 
# Conquistar


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

         #! Ordena con recursión
          return partition(menores) + iguales + partition(mayores) 


     else: 
          return lista
     






# -- Main --
arr = list()
for i in range(10):
     num = random.randint(0, 50)
     arr.append(num)


print(arr)
print(partition(arr))

