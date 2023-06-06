from pila import Pila
from cola import Queue



cola = Queue()
pila = Pila()


def palindromo(cadena):
     for c in cadena:
          cola.enqueue(c)
          pila.push(c)

     # cola.display()
     # pila.display()

     if not pila.is_empty():
          for i in range(len(cadena)):
               if pila.pop() != cola.dequeue():
                    return False
               
               cola.display()
               pila.display()
          return True


print(palindromo("ana"))

