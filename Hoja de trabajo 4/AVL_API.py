import graphviz, csv
from flask import Flask, request, jsonify
from os import system, startfile

class nodoArbol:
    def __init__(self, valor, nombre, DPI):
        self.izq = None
        self.der = None
        self.altura = 1
        self.valor = valor
        self.nombre = nombre
        self.DPI = DPI

class ABB:
    def __init__(self):
        self.raiz = None

    ''''''
    def api_flask_j(self):
        app = Flask(__name__)

        Opciones = [
            {
                "id": 1,
                "title": "1. Cargar con un archivo CSV."
            },
            {
                "id": 2,
                "title": "2. Insertar de forma manual."
            },
            {
                "id": 3,
                "title": "3. Buscar un registro."
            },
            {
                "id": 4,
                "title": "4. Mostrar la informacion del grupo."
            },
            {
                "id": 5,
                "title": "5. Salir."
            }
        ]

        info = [
            {
                "Nombre": "Anthony Fabian Ramirez Orellana",
                "Carne": "9490-22-958",
                "% de participacion": "100%"
            }
        ]

        @app.route('/', methods=['GET', 'POST'])
        def index():
            return jsonify({'respuesta':'done'}),200

        @app.route('/api/o0/opciones/')
        def get_all_opciones():
            return jsonify(Opciones)
        
        @app.route('/api/o1/cargaMasCSV/')
        def carga_archivo_CSV():
            return jsonify(Opciones)

        @app.route('/api/o2/buscar/')
        def get_info_nodos():
            infoNodo = self.pasar_info_json()
            return jsonify(infoNodo)

        @app.route('/api/o4/info/')
        def get_info_grupo():
            return jsonify(info)


        if __name__ == "__main__":
            app.run(debug=True, host='0.0.0.0', port=3000)

    ''''''
    def insert(self, valor, nombre, DPI):
        self.raiz = self._insert(valor, self.raiz, nombre, DPI)

    def _insert(self, valor, nodo, nombre, DPI):
        if nodo is None:
            return nodoArbol(valor, nombre, DPI)
        
        if(valor < nodo.valor):
            nodo.izq = self._insert(valor, nodo.izq, nombre, DPI)
        elif(valor > nodo.valor):
            nodo.der = self._insert(valor, nodo.der, nombre, DPI)

        #realiza balanceo
#        self._balancear(valor, nodo)

        self.actuarlizar_altura(nodo)

        balance = self._get_balance(nodo)

        # Caso de rotación simple a la derecha
        if balance > 1 and valor < nodo.izq.valor:
            return self._rotate_right(nodo)

        # Caso de rotación simple a la izquierda
        if balance < -1 and valor > nodo.der.valor:
            return self._rotate_left(nodo)

        # Caso de rotación doble a la derecha-izquierda
        if balance > 1 and valor > nodo.izq.valor:
            nodo.izq = self._rotate_left(nodo.izq)
            return self._rotate_right(nodo)

        # Caso de rotación doble a la izquierda-derecha
        if balance < -1 and valor < nodo.der.valor:
            nodo.der = self._rotate_right(nodo.der)
            return self._rotate_left(nodo)
        
        return nodo

    def actuarlizar_altura(self, nodo):
        if not nodo:
            return 0
        nodo.altura = 1 + max(self._get_height(nodo.izq), self._get_height(nodo.der))

 #   def _balancear(self, valor, nodo):


    def _get_height(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def _get_balance(self, nodo):
        if not nodo:
            return 0
        return self._get_height(nodo.izq) - self._get_height(nodo.der)

    def _rotate_right(self, z):
        y = z.izq
        t3 = y.der

        #realiza rotacion
        y.der = z
        z.izq = t3

        #actualiza altura
        self.actuarlizar_altura(z)
        self.actuarlizar_altura(y)

        return y

    def _rotate_left(self, y):#z
        #y = z.der
        #T2 = y.izq
        z = y.der
        t2 = z.izq
        
        #realizo rotacion
        #y.izq = z
        #z.der = T2
        z.izq = y
        y.der = t2

        #actualiza altura
        self.actuarlizar_altura(y)
        self.actuarlizar_altura(z)

        return z



    def buscar(self, valor):
        nodo = self.raiz
        return self._buscar(valor, nodo)
    def _buscar(self, valor, nodo):
        if nodo is None:
            print("No encontrado")
            return nodoArbol(-1) 
        if nodo.valor == valor:
            print("Valor encontrado!!!")
            return nodo
        if(valor < nodo.valor):
            return self._buscar(valor, nodo.izq)
        else:
            return self._buscar(valor, nodo.der)
    
    def buscarPorDPI(self, DPI):
        nodo = self.raiz
        return self._buscarPorDPI(nodo, DPI)
    def _buscarPorDPI(self, nodo, DPI):
        if nodo is None:
            print("....") 
            return 1
        if nodo.DPI == DPI:
            print(nodo.DPI)
            print("Valor encontrado!!!")
            return nodo
            
        self._buscarPorDPI(nodo.der, DPI)
        self._buscarPorDPI(nodo.izq, DPI)
        

    def inorder(self, nodo):
        if nodo !=None:
            self.inorder(nodo.izq)
            print(nodo.valor)
            self.inorder(nodo.der)

    def preorder(self, nodo):
        if nodo !=None:
            print(nodo.valor)
            self.inorder(nodo.izq)
            self.inorder(nodo.der)

    def postorder(self, nodo):
        if nodo is None:
            return
        
        ultimo_nodo_visitado = None
        while nodo:
            if nodo.izq and nodo.izq != ultimo_nodo_visitado and nodo.der != ultimo_nodo_visitado:
                nodo = nodo.izq
            elif nodo.der and nodo.der != ultimo_nodo_visitado:
                nodo = nodo.der
            else:
                print(nodo.valor)
                ultimo_nodo_visitado = nodo
                nodo = nodo.padre

    def mostrar(self, nodo):
        if nodo != None:
            if nodo.izq != None:
                #print(f"Altura nodo1: {nodo.altura}")
                print(f"{nodo.valor}: {nodo.nombre}, DPI: {nodo.DPI} -> {nodo.izq.valor}: {nodo.izq.nombre}, DPI: {nodo.DPI}")
                #print(f"Altura nodo.izq: {nodo.izq.altura}")
            if nodo.der != None:
                #print(f"Altura nodo2: {nodo.altura}")
                print(f"{nodo.valor}: {nodo.nombre}, DPI: {nodo.DPI} -> {nodo.der.valor}: {nodo.der.nombre}, DPI: {nodo.DPI}")
                #print(f"Altura nodo.der: {nodo.der.altura}")
            self.mostrar(nodo.izq)
            self.mostrar(nodo.der)
            
    def pasar_info_json(self):
        nodo = self.raiz
        return self._pasar_info_json(nodo)
    def _pasar_info_jason(self, nodo):
        if nodo !=None:
            self.inorder(nodo.izq)
            infoOrdenada = f'"{nodo.valor}": "{nodo.nombre}", "DPI": "{nodo.DPI}"'
            infoMasOrdenada = f"[ {infoOrdenada} ,]" 
            self.inorder(nodo.der)
            return infoMasOrdenada

    def  generar_arbol_grafico(self):
        dot = graphviz.Digraph()
        self._generar_arbol_grafico(self.raiz, dot)

        archivo_salida = "arbol.dot"
        dot.render(archivo_salida , format='png', cleanup=True)

        startfile(archivo_salida + '.png')

    def _generar_arbol_grafico(self, nodo, dot):
        if nodo is not None:
            dot.node(str(nodo.valor))
            if nodo.izq is not None:
                dot.edge(str(nodo.valor), str(nodo.izq.valor))
                self._generar_arbol_grafico(nodo.izq, dot)
            if nodo.der is not None:
                dot.edge(str(nodo.valor), str(nodo.der.valor))
                self._generar_arbol_grafico(nodo.der, dot)

    def delete(self, valor):
        self.raiz = self._delete(self.raiz, valor)

    def _delete(self, node, valor):
        if node is None:
            return node

        if valor < node.valor:
            node.izq = self._delete(node.izq, valor)
        elif valor > node.valor:
            node.der = self._delete(node.der, valor)
        else:
            if node.izq is None:
                return node.der
            elif node.der is None:
                return node.leizqft

            node.valor = self._find_min(node.der).valor
            node.right = self._delete(node.der, node.valor)

        return node

    def _find_min(self, node):
        while node.izq is not None:
            node = node.izq
        return node
    
    def _find_max(self, node):
        while node.der is not None:
            node = node.der
        return node  
    
    def agregarArch(self):
        with open(input('Seleccione un archivo CSV: '),'r', newline='') as csvfile:
            lector_csv = csv.DictReader(csvfile)
            print("encabezados: ", lector_csv.fieldnames)
            #encabezado = lector_csv.fieldnames[0]
            for encabezado in lector_csv.fieldnames:
                #encabezado = lector_csv.fieldnames[i]
                for fila in lector_csv:
                    try:
                        #print(fila[encabezado])
                        datosSeparados = fila[encabezado].split(";")
                        self.insert(datosSeparados[0], datosSeparados[1], datosSeparados[2])

                    except KeyError:
                        print("no existe la columna 'id' en la fila")
      
arbol = ABB()
arbol.api_flask_j()
'''
opcion = 0
while opcion != 5:
    print("Elija una opcion a ejecutar:")
    print("1. Cargar con un archivo CSV.")
    print("2. Insertar de forma manual.")
    print("3. Buscar un registro.")
    print("4. Mostrar la informacion del grupo.")
    print("5. Salir.")
    opcion = int(input())

    if opcion == 1:
        arbol.agregarArch()
        arbol.mostrar(arbol.raiz)
        arbol.generar_arbol_grafico()
        opcion = 0
    elif opcion == 2:
        numeroDeRegistros = int(input("Ingrese la cantidad de registros que desea ingresar: "))
        while numeroDeRegistros != 0:
            valor = int(input("Ingrese el id: "))
            nombre = str(input("Ingrese el nombre: "))
            numeroDPI = int(input("Ingrese el numero de DPI: "))
            arbol.insert(valor, nombre, numeroDPI)
            print("Siguiente registro: ")
            print(" ")
            numeroDeRegistros -= 1
        arbol.mostrar(arbol.raiz)
        arbol.generar_arbol_grafico()
        opcion = 0
    elif opcion == 3:
        print("Ingrese la forma en la que desea buscar el registro: ")
        print("1. ID")
        print("2. DPI")
        secOpcion = int(input("opcion: "))
        if secOpcion == 1:
            arbol.buscar(input("Ingrese el ID que desea buscar: "))

        elif secOpcion == 2:
                arbol.buscarPorDPI(input("Ingrese el DPI que desea buscar: "))

        secOpcion = 0
        opcion = 0
    elif opcion == 4:
        system("cls")
        print(" ")
        print("Nombre: Anthony Fabian Ramirez Orellana, Carne: 9490-22-958, % de participacion: 100%")
        print(" ")

    elif opcion == 5:
        print("Adios .....")
        break
'''