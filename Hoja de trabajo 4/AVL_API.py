import graphviz, csv
from flask import Flask, request, jsonify
import os
#from os import system, startfile

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
            return print(...)
        if nodo.valor == valor:
            print("Valor encontrado!!!")
            info = (f"{nodo.valor}: {nodo.nombre}, DPI: {nodo.DPI}")
            return info
        if(valor < nodo.valor):
            return self._buscar(valor, nodo.izq)
        else:
            return self._buscar(valor, nodo.der)
    
    def buscarPorDPI(self, nodo, DPI):
        if not nodo:
            return None
        if nodo.DPI == DPI:
            info = f"{nodo.valor}: {nodo.nombre}, DPI: {nodo.DPI}"
            print("Valor encontrado!!!")
            return info
        resultado_izq =self.buscarPorDPI(nodo.izq, DPI)
        if resultado_izq:
            return resultado_izq
        return self.buscarPorDPI(nodo.der, DPI)


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

        direccion = os.path.dirname(os.path.abspath(__file__))
        archivo = os.path.join(direccion, 'source', '10 registros(id, nombre, dpi).csv')

        with open(archivo,'r', newline='') as csvfile:
            lector_csv = csv.DictReader(csvfile)
            #print("encabezados: ", lector_csv.fieldnames)
            #encabezado = lector_csv.fieldnames[0]
            for encabezado in lector_csv.fieldnames:
                #encabezado = lector_csv.fieldnames[i]
                for fila in lector_csv:
                    try:
                        #print(fila[encabezado])
                        datosSeparados = fila[encabezado].split(";")
                        self.insert(datosSeparados[0], datosSeparados[1], datosSeparados[2])
                        return True
                    except KeyError:
                        #print("no existe la columna 'id' en la fila")
                        return False
      
arbol = ABB()

app = Flask(__name__)

Opciones = [
    {
        "id": 1,
        "title": "1. Cargar con un archivo CSV, escribir en url: /api/o1/cargaMasCSV/<direccion>   en el espacio de '<direccion>' escribir la direccion del archivo. EJ: T:/abs/hoja.csv"
    },
    {
        "id": 2,
        "title": "2. Insertar de forma manual, escribir en url: /api/o2/insercionManual/<ID>/<nombre>/<DPI>   en los espacios de <ID>, <nombre>, <DPI>, escribir el ID, nombre y DPI respectivamente"
    },
    {
        "id": 3,
        "title": "3. Buscar un registro por ID, escribir en url: /api/o3/buscarRegistroXID/<ID>   en <ID> escribir el ID que desea buscar."
    },
    {
        "id": 4,
        "title": "3. Buscar un registro por DPI, escribir en url: /api/o4/buscarRegistroXDPI/<DPI>    en <DPI> escribri el DPI que desea buscar."
    },
    {
        "id": 5,
        "title": "4. Mostrar la informacion del grupo, escribir en url: /api/o5/info/      para desplegar la informacion de los miembros del grupo."
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

@app.route('/api/o0/opciones')########opcion 0
def get_all_opciones():
    return jsonify(Opciones)

@app.route("/api/o1/cargaMasCSV/", methods=("POST"))########opcion 1
def carga_archivo_CSV():
    try:   
        if arbol.agregarArch() is None:
            return jsonify({'respuesta': 'fail'}),400
        #self.generar_arbol_grafico()
        #probar generar un grapviz
        return jsonify({'respuesta': 'agregado'}),200
    except:
        return jsonify({'respuesta': 'fail'}),400

@app.route('/api/o2/insercionManual/<ID>/<nombre>/<DPI>')########opcion 2
def insercion_manual(ID, nombre, DPI):
    arbol.insert(ID, nombre, DPI)
    #self.generar_arbol_grafico()
    ##probar generar un grapviz
    #infoNodo = self.pasar_info_json()
    #return jsonify(infoNodo)
    return jsonify(f'Contenido agregado exitosamente: ID:{ID}, nombre:{nombre}, DPI:{DPI}')

@app.route('/api/o3/buscarRegistroXID/<ID>')########opcion 3
def buscar_info_ID(ID):
    
    try:
        #self.agregarArch(direccion)
        #self.generar_arbol_grafico()
        nodo = arbol.buscar(ID)
    except:
        return jsonify({'respuesta': 'fail'}),400

    return jsonify(nodo)

@app.route('/api/o4/buscarRegistroXDPI/<DPI>')########opcion 4
def buscar_DPI(DPI):

    #self.agregarArch(direccion)
    #self.generar_arbol_grafico()
    nodo = arbol.buscarPorDPI(arbol.raiz, DPI)
    
    return jsonify(nodo)

@app.route('/api/o5/info/')########opcion 5
def get_info_grupo():
    return jsonify(info)


if __name__ == "__main__":
    app.run(debug=True)