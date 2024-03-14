from os import system, startfile #importo os para utilizar funcionalidades dependientes del sistema operativo, en este caso el system("cls")
import graphviz

class NodoA:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

class ABB:
    def __init__(self):
        self.raiz = None
    
    def insert(self, valor):
        self.raiz = self.inserta2(valor, self.raiz)
    def inserta2(self, valor, nodo):
        if(nodo == None):
            print(f"Valor: {valor} insertado correctamente")
            return NodoA(valor)
        if(valor < nodo.valor):
            nodo.izq = self.inserta2(valor, nodo.izq)
        if(valor > nodo.valor):
            nodo.der = self.inserta2(valor, nodo.der)
        return nodo
    
    def insertArchi(self, valores):
        if(  isinstance(valores, list)  ):
            for valor in valores:
                self.raiz = self.insertArchiva2(self.raiz, valor)
        else:
            self.raiz = self.insertArchiva2(self.raiz, valor)
    def insertArchiva2(self, nodo, valor):
        if(nodo is None):
            return NodoA(valor)
        if(valor < nodo.valor):
            nodo.izq = self.insertArchiva2(nodo.izq, valor)
        elif(valor > nodo.valor):
            nodo.der = self.insertArchiva2(nodo.der, valor)
        return nodo

#    def leerArchivo(direArch):#archivo contiene valores separados por lineas
#        with open(direArch, 'r') as file:
#            valores = file.readlines()
#        valores = [  int(  val.strip()  )  for val in valores]
#        return valores


    def buscar(self, valor):
        return self.busca2(valor, self.raiz)
    def busca2(self, valor, nodo):
        if(nodo == None):
            print("No se encontro el valor")
            return None
        if(nodo.valor == valor):
            print("Encontrado: "+str(nodo.valor))
            return nodo
        if(valor < nodo.valor):
            return self.busca2(valor, nodo.izq)
        else:
            return self.busca2(valor, nodo.der)
        
    def eliminar(self, valor):
        self.raiz = self.elimina2(self.raiz, valor)################
    def elimina2(self, nodo, valor):
        if(nodo is None):
            return nodo

        if(valor < nodo.valor):
            nodo.izq = self.elimina2(nodo.izq, valor)
        elif(valor > nodo.valor):
            nodo.der = self.elimina2(nodo.der, valor)
        
        else:
            if(nodo.izq is None):#nodo con solo un hijo o sin hijos
                temp = nodo.der
                nodo = None
                return temp
            elif(nodo.der is None):
                temp = nodo.izq
                nodo = None
                return temp

            temp = self.valorMin(nodo.der)#nodo con dos hijos, agarro el sucesor en modo inOrder
            nodo.valor = temp.valor##Copio el valor del sucesor para el nodo
            nodo.der = self.elimina2(nodo.der, temp.valor)#elimino el sucesor
        return nodo
    
    def valorMin(self, nodo):
        actual = nodo
        while actual.izq:
            actual = actual.izq
        return actual

    def preOrderGrap(self, nodo):
        #dot = graphviz.Digraph(comment='Arbol_B_B')

        if(nodo != None):
            #dot.node(  str(  id(nodo)  ), str(nodo.valor)  )
            print(nodo.valor)

            if(nodo.izq != None):
             #   dot.edge(  str(  id(nodo)  ), str(  id(nodo.izq)  ), label='izq'  )
                self.preOrderGrap(nodo.izq)
            if(nodo.der != None):
                self.preOrderGrap(nodo.der)
              #  dot.edge(  str(  id(nodo)  ), str(  id(nodo.der)  ), label='der'  )
            #return dot
    numeroDeNodos=0
    def generate_graph(self):
        dot = graphviz.Digraph(comment='Arbo_B_B')
        
        def add_edges(nodo):
            if(nodo != None):
                if(nodo.izq):
                    dot.edge(  str(nodo.valor), str(nodo.izq.valor), label='izq')
                    add_edges(nodo.izq)
                    self.numeroDeNodos +=1
                if(nodo.der):
                    dot.edge(  str(nodo.valor), str(nodo.der.valor), label='der')
                    add_edges(nodo.der)
                    self.numeroDeNodos +=1
                elif(self.numeroDeNodos == 0):
                    dot.node(  str(  id(nodo)  ), str(nodo.valor)  )
                    self.numeroDeNodos +=1
        add_edges(self.raiz)
        return dot

    
def menu():
    print("__________________Menu__________________")
    print("1. Insertar.")
    print("2. Buscar.")
    print("3. Eliminar.")
    print("4. Cargar desde txt.")
    print("5. Salir.")

arbol = ABB()
while True:

    menu()
    try:
        opc = int(input("Ingrese una opcion: "))
    except ValueError as e:
        print("Error: Porfavor ingrese un valor valido")
        print(f"Error: {e}")

    if(opc == 1):#Opcion insertar
        system("cls")
        try:
            valorIn = int(input("Ingresa un numero entero para agregar al arbol: "))
            arbol.insert(valorIn)

            graph = arbol.generate_graph()
            graph.render('Arbol_B_B', format='png', cleanup=True)
            startfile('Arbol_B_B.png')

        except ValueError as e:
            print("Error: Porfavor ingrese un valor valido")
            print(f"Error: {e}")

    elif(opc == 2):#Opcion buscar
        system("cls")
        try:
            valorBus = int(input("Introdusca el valor que desea buscar: "))
            arbol.buscar(valorBus)

            graph = arbol.generate_graph()
            graph.render('Arbol_B_B', format='png', cleanup=True)
            startfile('Arbol_B_B.png')

        except ValueError as e:
            print("Error: Porfavor ingrese un valor valido.")
            print(f"Error: {e}")

    elif(opc == 3):#Opcion Eliminar
        system("cls")
        try:
            valorElim = int(  input("Introdusca el valor que desea eliminar: ")  )
            arbol.eliminar(valorElim)

            print("Valor eliminado!!!!")
            graph = arbol.generate_graph()
            graph.render('Arbol_B_B', format='png', cleanup=True)
            startfile('Arbol_B_B.png')
        
        except ValueError as e:
            print("Error: Porfavor ingrese un valor valido.")
            print(f"Error: {e}")


    elif(opc == 4):#Opcion cargar desde archivo
        system("cls")
        direArch = input("Igrese la direccion del archivo: ")

        with open(direArch, "r") as archivo:
            datos = archivo.readlines()
            for linea in datos:
                print(f"{linea} \n")

                try:
                    valores = int( linea.strip(" ") )
                    arbol.insertArchi(valores)
                except ValueError:
                    print(f"Ignorando los valores no enteros: {linea.strip(" ")}")

        #valores = arbol.leerArchivo(direArch)

        graph = arbol.generate_graph()
        graph.render('Arbol_B_B', format='png', cleanup=True)
        startfile('Arbol_B_B.png')


    elif(opc == 5):#Opcion salir
        break
        
    else:
        system("cls")
        print("Opcion invalida, porfavor ingrese una opcion del menu")




