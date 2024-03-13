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
    i=0
    def generate_graph(self):
        dot = graphviz.Digraph(comment='Arbo_B_B')
        
        def add_edges(nodo):
            if(nodo != None):
                if(nodo.izq):
                    dot.edge(  str(nodo.valor), str(nodo.izq.valor), label='izq')
                    add_edges(nodo.izq)
                    self.i +=1
                if(nodo.der):
                    dot.edge(  str(nodo.valor), str(nodo.der.valor), label='der')
                    add_edges(nodo.der)
                    self.i +=1
                elif(self.i == 0):
                    dot.node(  str(  id(nodo)  ), str(nodo.valor)  )
                    self.i +=1
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
            system('cd ./Arbol_B_B.png')
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
            system('cd ./Arbol_B_B.png')
            startfile('Arbol_B_B.png')

        except ValueError as e:
            print("Error: Porfavor ingrese un valor valido.")
            print(f"Error: {e}")

    elif(opc == 3):#Opcion Eliminar
        system("cls")

    elif(opc == 4):#Opcion cargar desde archivo
        system("cls")

    elif(opc == 5):#Opcion salir
        break
        
    else:
        system("cls")
        print("Opcion invalida, porfavor ingrese una opcion del menu")




