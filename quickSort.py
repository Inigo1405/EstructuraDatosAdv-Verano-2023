import random

# Dividir 
# Conquistar


def partition(lista):
     if lista:

          mayores=list()
          iguales=list()
          menores=list()
          p =  random.randint(0, len(arr)-1)

          #! Dividir
          for i in lista:
               if i > lista[p]:
                    mayores.append(i)
                    
               elif i < lista[p]:
                    menores.append(i)

               elif i == lista[p]:
                    iguales.append(i)

          #print(menores)
          #print(iguales)
          #print(mayores)
          #print(lista)


          # p =  random.randint(0, len(lista)-1)
          # partition(menores, p)
         
         
          # partition(iguales)
          # partition(mayores)
         
          return menores, iguales, mayores

     else: 
          return []
     


def sort(lista):
     #! Ordenar
     if len(lista) <= 1:
          return lista
     
     menores, iguales, mayores = partition(lista)
     return partition(menores) + [iguales] + partition(mayores)


arr = list()
for i in range(10):
     num = random.randint(0, 50)
     arr.append(num)


#print(arr[p])
print(arr)

#partition(arr)
sort(arr)