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

  
  
  def binarioPerfecto(self, arbol, p, nivel=0):
    if arbol is None:
      return None
    
    if arbol.izq is None and arbol.der is None: # Hoja
      return (p == nivel + 1)

    if arbol.izq is None or arbol.der is None: 
      return False
    
    return self.binarioPerfecto(arbol.izq, p, nivel + 1) and self.binarioPerfecto(arbol.der, p, nivel+1)
  


  def profundidad(self, arbol):
    if arbol is None:
      return 0
    
    if arbol:

      prof_izq = self.profundidad(arbol.izq)
      prof_der = self.profundidad(arbol.der)

      #print("Izq ", prof_izq)
      #print("Der ", prof_der)

      if prof_izq > prof_der:
        return prof_izq + 1
      
      else:
        return prof_der + 1

    

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


  def sucesor(self, arbol):
    if arbol.izq:
      return self.sucesor(arbol.izq)
    
    elif arbol.izq is None: 
      return arbol


  
  def eliminar(self, arbol, dato):
    if arbol is None:
      return None


    # Busca el dato a eliminar
    if dato < arbol.dato:
      arbol.izq = self.eliminar(arbol.izq, dato)

    elif dato > arbol.dato:
      arbol.der = self.eliminar(arbol.der, dato)


    else:
      # Caso 0. Cuando no tiene hijos
      # Caso 1: Cuando solo tiene un hijo 
      # Caso 2: Cuando tiene dos hijos

      if arbol.izq is None:
        temp = arbol.der
        arbol = None
        #print(temp.dato)
        return temp

      elif arbol.der is None:
        temp = arbol.izq
        arbol = None
        #print(temp.dato)
        return temp
 
      temp = self.sucesor(arbol.der)
      arbol.dato = temp.dato
      arbol.der = self.eliminar(arbol.der, temp.dato)

      # encontrar el sucesor en inorden
     
    return arbol



arbolito = Arbol(9)

arbolito.insertar(arbolito.raiz, 5)
arbolito.insertar(arbolito.raiz, 10)
arbolito.insertar(arbolito.raiz, 1)
arbolito.insertar(arbolito.raiz, 7)
arbolito.insertar(arbolito.raiz, 6)
arbolito.insertar(arbolito.raiz, 8)
arbolito.insertar(arbolito.raiz, 12)



print("\nPreorden")
arbolito.preorden(arbolito.raiz)

print("\n\nInorden")
arbolito.inorden(arbolito.raiz)

print("\n\nPostorden")
arbolito.postorden(arbolito.raiz)

print("\n\nAnchura")
arbolito.anchura(arbolito.raiz)

print("\nNodo Raiz")
arbolito.nodoRaiz(arbolito.raiz)

print("\nNodos Hoja")
arbolito.nodosHoja(arbolito.raiz)

print("\n\nPeso arbol")
print(arbolito.pesoArbol(arbolito.raiz))

print("\nProfundidad arbol")
print(arbolito.profundidad(arbolito.raiz))

print("\nEliminar nodo del arbol")
arbolito.preorden(arbolito.raiz)
print()
arbolito.eliminar(arbolito.raiz, 7)
arbolito.preorden(arbolito.raiz)
