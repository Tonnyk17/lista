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
    _q=None
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
            nuevo_nodo._next =self._raiz 
            self._raiz = nuevo_nodo

    def imprimir(self):
        siguiente=self._raiz
        while siguiente != None:
            print(siguiente._dato)
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
        if posicion ==1:
            nuevo_nodo._next = self._raiz
            self._raiz = nuevo_nodo
        i = 1
        n = self._raiz
        while posicion - 1 > i and n != None:
            n = n._next
            i = i+1
        if n == None:
            return False
        else:
            nuevo_nodo._next = n._next
            n._next = nuevo_nodo
        
    def eliminarInicio(self):
        if self._raiz == None:
            return False
        else:
            self._raiz = self._raiz._next        
            self._longitud -= 1

    def invertir(self):
        if self._raiz == None:
            return False
        else:
            siguiente = anterior = None
            aux = self._raiz
            while aux:
                siguiente = aux._next
                aux._next = anterior
                anterior = aux
                aux = siguiente
            self._raiz = anterior

    def burbuja(self):
        if self._raiz == None:
            return False
        else:
           siguiente = self._raiz
           while siguiente._next != None:
               q = siguiente._next
               while q != None:
                   if siguiente._dato > q._dato:
                       aux = siguiente._dato
                       siguiente._dato = q._dato
                       q._dato= aux

    def buscar(self,valor):
        if self._raiz == None:
            return False
        else:
            siguiente = self._raiz
            while siguiente != None:
                if siguiente._dato == valor._dato:
                    print('Valor encontrado')
                    return True
                siguiente = siguiente._next
            print('Valor no encontrado')
           
    def reemplazar(self,valor,posicion):
        if self._raiz == None:
            return False
        else:
            if posicion >= 0 and self._longitud > posicion:
                siguiente = self._raiz

                for i in range(posicion):
                    siguiente = siguiente._next
                siguiente._dato =valor._dato

    def concatenar(self,lista):
        print(lista)
                
        
n1=nodo(5)
n2=nodo(6)
n3=nodo(29)
n4=nodo(123)

listaSimple = listaEnlazada()
listaSimple.insertar(n1)
listaSimple.insertar(n2)
listaSimple.insertar(n3)
#listaSimple.insertarInicio(n4)
#listaSimple.eliminarInicio()
#listaSimple.insertarPosicion(n4,2)
#listaSimple.eliminarSeleccion(n2)
#listaSimple.eliminarFinal()
#listaSimple.burbuja()
listaSimple.reemplazar(n4,1)
#listaSimple.invertir()
listaSimple.imprimir()
listaSimple.tamano()
lista2 = listaEnlazada()
listaSimple.concatenar(lista2)
