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
            siguiente=siguiente._next
            print(siguiente._dato)

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
    
    def eliminarFinal(self):
        if self._longitud == 0:
            return False
        else:
            siguiente = self._raiz

            while siguiente._next != None:
                
                eliminar = siguiente
                siguiente = siguiente._next
            if siguiente != None:
                eliminar._next = siguiente._next
            self._longitud -=1

    def insertarPosicion(self,nuevo_nodo,posicion):
        if self._raiz ==None:
            self._raiz=nuevo_nodo
        else:
            siguiente = self._raiz
            while siguiente._next == posicion:
                siguiente = siguiente._next
                siguiente._next = nuevo_nodo

        

        
            

n1=nodo(5)
n2=nodo(6)
n3=nodo(29)
n4=nodo(19)

listaSimple = listaEnlazada()
listaSimple.insertar(n1)
listaSimple.insertar(n2)
listaSimple.insertar(n3)
#listaSimple.insertarPosicion(n4,n2)
#listaSimple.eliminarSeleccion(n2)
#listaSimple.eliminarFinal()
listaSimple.imprimir()
listaSimple.tamano()
