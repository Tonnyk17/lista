import os

class nodo:
    _dato=0
    _next=None
    _inicio=None
    def __init__(self,dato):
        self._dato=dato
        self._next=None
        self._inicio=None
class listaEnlazada:
    _raiz=None
    _longitud=0
    def __init__(self):
        self._raiz=None
        self._longitud=0

    def insertar(self,nuevo_nodo):
        self._longitud+=1
        
        if self._raiz ==None:
            self._raiz=nuevo_nodo
            
        else:
            siguiente=self._raiz
            while siguiente._next != None:
                siguiente=siguiente._next
            siguiente._next=nuevo_nodo

    def insertarInicio(self,nuevo_nodo):
            self._raiz=nuevo_nodo 

    def imprimir(self):
        siguiente=self._raiz
        while siguiente != None:
            print(siguiente._dato,siguiente._inicio)
            siguiente=siguiente._next
    def tamano(self):
        print("Longitud de la lista:",self._longitud)

    def eliminarSeleccion(self,eliminar_nodo):
        if self._longitud == 0:
            return False
        else:
            siguiente = self._raiz
            while siguiente._next != eliminar_nodo:
                if siguiente._next == None:
                    return False
                else:
                    siguiente = siguiente._next
            eliminar = siguiente._next
            siguiente._next = eliminar._next
            self._longitud -= 1
    
    def eliminarInicio(self):
        if self._raiz ==None:
            return False
            

n1=nodo(5)
n2=nodo(6)
n3=nodo(29)
n4=nodo(19)

listaSimple = listaEnlazada()
listaSimple.insertar(n1)
listaSimple.insertar(n2)
listaSimple.insertar(n3)

#listaSimple.eliminarSeleccion(n3)
listaSimple.eliminarInicio()
listaSimple.imprimir()
