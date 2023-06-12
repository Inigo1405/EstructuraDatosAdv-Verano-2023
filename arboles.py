from nodoArbol import Nodo


class Arbol():

  def __init__(self, dato):
    self.raiz = Nodo(dato)


  
  def insertar(self, arbol, dato):
    # Agregar al inicio
    if arbol is None:
      return Nodo(dato)

    # Agregar a la izq del arbol el dato menor
    elif dato < arbol.dato:
      arbol.izq = self.insertar(arbol.izq, dato)

    # Agregar a la der del arbol el dato mayor
    elif dato > arbol.dato:
      arbol.der = self.insertar(arbol.der, dato)

    return arbol


  
  def preorden(self, arbol):
    if arbol:
      print(f'{arbol.dato}', end='→')
      self.preorden(arbol.izq)
      self.preorden(arbol.der)


  
  def inorden(self, arbol):
    if arbol:
      self.preorden(arbol.izq)
      print(f'{arbol.dato}', end='→')
      self.preorden(arbol.der)


  
  def postorden(self, arbol):
    if arbol:
      self.preorden(arbol.izq)
      self.preorden(arbol.der)
      print(f'{arbol.dato}', end='→')

  
  
  def anchura(self, arbol):
    fila = [arbol]
    
    while fila:
      nodo_actual = fila.pop(0)
      print(nodo_actual.dato)
      
      if nodo_actual.izq:
        fila.append(nodo_actual.izq)

      if nodo_actual.der:
        fila.append(nodo_actual.der)

  
  
  def binarioPerfecto(self, arbol):
    pass


  
  def binarioLleno(self, arbol):
    pass


  
  def nodosHoja(self, arbol):
    if arbol is None:
      return

    elif arbol.izq is None and arbol.der is None:
      print(f'{arbol.dato}', end=', ')

    self.nodosHoja(arbol.izq)
    self.nodosHoja(arbol.der)
      

  
  
  def pesoArbol(self, arbol):
    if arbol is None:
      return 0

    else: 
      return 1 + self.pesoArbol(arbol.izq) + self.pesoArbol(arbol.der)

  
  
  def nodoRaiz(self, arbol):
    if arbol:
      print(arbol.dato)
      return arbol.dato


  
  def eliminar(self, arbol, dato):
    if arbol is None:
      return None

    # Busca el dato a eliminar
    if dato < arbol.dato:
      arbol.izq = self.eliminar(arbol.izq, dato)

    elif dato > arbol.dato:
       arbol.der = self.eliminar(arbol.der, dato)

    else:
      # Caso 1: Cuando solo tiene un hijo 
      if arbol.izq is None:
        temp = arbol.der
        arbol = None
        return temp

      elif arbol.der is None:
        temp = arbol.izq
        arbol = None
        return temp
 
      else:
        # Caso 2: Cuando tiene dos hijos
        # encontrar el sucesor en inorden
        temp = self.sucesor(arbol.der)
        arbol.dato = temp.dato

          
        arbol.der = self.eliminar(arbol.der, temp.dato)
     
    return arbol



arbolito = Arbol(20)

arbolito.insertar(arbolito.raiz, 15)
arbolito.insertar(arbolito.raiz, 9)
arbolito.insertar(arbolito.raiz, 16)
arbolito.insertar(arbolito.raiz, 24)
arbolito.insertar(arbolito.raiz, 30)


print("\n\nPreorden")
arbolito.preorden(arbolito.raiz)

print("\n\nInorden")
arbolito.inorden(arbolito.raiz)

print("\n\nPostorden")
arbolito.postorden(arbolito.raiz)

print("\n\nAnchura")
arbolito.anchura(arbolito.raiz)

print("\n\nNodo Raiz")
arbolito.nodoRaiz(arbolito.raiz)

print("\n\nNodos Hoja")
arbolito.nodosHoja(arbolito.raiz)

print("\n\nPeso arbol")
print(arbolito.pesoArbol(arbolito.raiz))




