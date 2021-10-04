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
    _head=None
    _length=0
    def __init__(self):
        self._head=None
        self._length=0

    def add(self):
        nuevo_nodo =int(input('Ingresa el valor del nodo:'))
        newNode = nodo(nuevo_nodo)
        self._length+=1
        
        if self._head ==None:
            self._head=newNode
            
        else:
            p=self._head
            while p._next != None:
                p=p._next
            p._next=newNode
        

    def addStart(self):
            nuevo_nodo =int(input('Ingresa el valor del nodo:'))
            newNode = nodo(nuevo_nodo)
            newNode._next =self._head 
            self._head = newNode

    def deploy(self):
        p=self._head
        while p != None:
            print(p._dato)
            p=p._next
            

    def size(self):
        print("Longitud de la lista:",self._length)

    def deleteSelection(self):
        eliminar_nodo = int(input('Ingresa el elemento a eliminar:'))
        if self._length == 0:
            print('La lista esta vacia')
            return False
        else:
            p = self._head
            while p._next != eliminar_nodo:
                if p._next == None:
                    return False
                else:
                    p = p._next
            eliminar = p._next
            p._next = eliminar._next
            self._length -= 1
    
    def deleteLast(self):
        if self._length == 0:
            print('La lista esta vacia')
            return False
        else:
            p = self._head

            while p._next != None:
                
                eliminar = p
                p = p._next
            if p != None:
                eliminar._next = p._next
            self._length -=1

    def addPosition(self):
        position = int(input('Ingresa la posicion:'))
        nuevo_nodo = int(input('Ingresa el valor del elemento:'))
        newNode = nodo(nuevo_nodo)
        if position ==1:
            newNode._next = self._head
            self._head = newNode
        i = 1
        n = self._head
        while position - 1 > i and n != None:
            n = n._next
            i = i+1
        if n == None:
            return False
        else:
            newNode._next = n._next
            n._next = newNode
        
    def deleteStart(self):
        if self._length == 0:
            print('La lista esta vacia')
            return False
        else:
            self._head = self._head._next        
            self._length -= 1

    def reverse(self):
        if self._length == 0:
            print('La lista esta vacia')
            return False
        else:
            p = anterior = None
            aux = self._head
            while aux:
                p = aux._next
                aux._next = anterior
                anterior = aux
                aux = p
            self._head = anterior

    def search(self):
        value = int(input('Ingresa el valor a buscar:'))
        searchNode = nodo(value)
        if self._length == 0:
            print('La lista esta vacia')
            return False
        else:
            p = self._head
            while p != None:
                if p._dato == searchNode._dato:
                    print('Valor encontrado')
                    return True
                p = p._next
            print('Valor no encontrado')
           
    def replace(self):
        position = int(input('Ingresa la posicion:'))
        value = int(input('Ingresa el valor a agregar'))
        replaceNode = nodo(value)
        if self._length == 0:
            print('La lista esta vacia')
            return False
        else:
            if position >= 0 and self._length > position:
                p = self._head

                for i in range(position):
                    p = p._next
                p._dato =replaceNode._dato

    def concat(self,lista):
        p = self._head
        while p._next != None:
            p = p._next
        p._next = lista._head
        self._length += lista._length

    def inter(self,lista):
        if self._length == 0:
            print('La lista esta vacia')
            return False
        else:
            p = self._head
            q = lista._head
            while p._next != None and q._next != None:
                aux = q._next
                q._next = p._next
                p._next = q
                p = q._next
                q = aux
            if p._next == None:
                p._next =q
            elif p._next != None and  q._next == None:
                q._next = p._next
                p._next = q

    def deleteRepeats(self):
        value = int(input('Ingresa el valor repetido:'))
        deleteNode = nodo(value)
        if self._length == 0:
            print('La lista esta vacia')
            return False
        else:
            p = self._head
            q = self._head
            while p != None:
                if p._dato == deleteNode._dato:
                    self._length -= 1
                    if p == self._head:
                        self._head = self._next
                        p = self._head
                    else:
                        q._next = p._next
                        p = q._next
                else:
                    q = p
                    p = p._next

def main():
    lista = listaEnlazada()
    salir = False
    
    while not salir:
        options = ['Salir','Agregar nodo','Agregar nodo al inicio','Eliminar nodo al final','Eliminar nodo al inicio','Eliminar nodo especifico','Eliminar repetidos','Reemplazar elemento','Imprimir lista','Longitud de la lista','Buscar nodo','Invertir lista','Concatenar lista','Intercalar lista']
        for i in range(len(options)):
            print('[',i,']',options[i])
        
        optionSelected = int(input("Selecciona una opcion: "))
        os.system('clear')
        if optionSelected == 0:
            salir = True
        elif optionSelected == 1:
            lista.add()
        elif optionSelected == 2:
            lista.addStart()
        elif optionSelected == 3:
            lista.deleteLast()
        elif optionSelected == 4:
            lista.deleteStart()
        elif optionSelected == 5:
            lista.deleteSelection()
        elif optionSelected == 6:
            lista.deleteRepeats()
        elif optionSelected == 7:
            lista.replace()
        elif optionSelected == 8:
            lista.deploy()
        elif optionSelected == 9:
            lista.size()
        elif optionSelected == 10:
            lista.search()
        elif optionSelected == 11:
            lista.reverse()
            lista.deploy()
        elif optionSelected == 12:
            print('Ingresa 5 elementos para la segunda lista')
            lista_2 = listaEnlazada()
            for i in range(5):
                lista_2.add()
            lista.concat(lista_2)
            lista.deploy()
        elif optionSelected == 13:
            print('Ingresa 5 elementos para la segunda lista')
            lista_2 = listaEnlazada()
            for i in range(5):
                lista_2.add()
            lista.inter(lista_2)
            lista.deploy()
        else:
            print('Selecciona una opcion valida')
main()

