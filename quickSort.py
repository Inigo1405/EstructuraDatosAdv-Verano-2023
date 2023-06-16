import random

# Dividir y conquistar

mayores=list()
iguales=list()
menores=list()

def partition(lista):
     if lista:
          for i in lista:
               if i > lista[p]:
                    mayores.append(i)

               elif i < lista[p]:
                    menores.append(i)

               elif i == lista[p]:
                    iguales.append(i)

          print(menores)
          print(iguales)
          print(mayores)

          #p =  random.randint(0, len(lista)-1)
          #partition(menores, p)
     # partition(iguales)
     # partition(mayores)



arr = list()
for i in range(10):
     num = random.randint(0, 50)
     arr.append(num)

p =  random.randint(0, len(arr)-1)
#print(arr[p])
print(arr)

partition(arr)
