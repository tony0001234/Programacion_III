import graphviz
from os import startfile

class NodoAVL:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        self.altura = 1  # Por defecto, la altura de un nodo nuevo es 1

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def actualizar_altura(self, nodo):
        if not nodo:
            return 0
        nodo.altura = 1 + max(self.altura(nodo.izquierdo), self.altura(nodo.derecho))

    def rotacion_derecha(self, nodo_z):
        nodo_y = nodo_z.izquierdo
        t3 = nodo_y.derecho

        # Realizar rotación
        nodo_y.derecho = nodo_z
        nodo_z.izquierdo = t3

        # Actualizar alturas
        self.actualizar_altura(nodo_z)
        self.actualizar_altura(nodo_y)

        return nodo_y

    def rotacion_izquierda(self, nodo_y):
        nodo_z = nodo_y.derecho
        t2 = nodo_z.izquierdo

        # Realizar rotación
        nodo_z.izquierdo = nodo_y
        nodo_y.derecho = t2

        # Actualizar alturas
        self.actualizar_altura(nodo_y)
        self.actualizar_altura(nodo_z)

        return nodo_z

    def balance(self, nodo):
        if not nodo:
            return 0
        return self.altura(nodo.izquierdo) - self.altura(nodo.derecho)

    def insertar(self, nodo, valor):
        if not nodo:
            return NodoAVL(valor)
        
        if valor < nodo.valor:
            nodo.izquierdo = self.insertar(nodo.izquierdo, valor)
        else:
            nodo.derecho = self.insertar(nodo.derecho, valor)

        self.actualizar_altura(nodo)

        # Realizar balanceo
        balanceo = self.balance(nodo)

        # Caso izquierda-izquierda
        if balanceo > 1 and valor < nodo.izquierdo.valor:
            return self.rotacion_derecha(nodo)

        # Caso derecha-derecha
        if balanceo < -1 and valor > nodo.derecho.valor:
            return self.rotacion_izquierda(nodo)

        # Caso izquierda-derecha
        if balanceo > 1 and valor > nodo.izquierdo.valor:
            nodo.izquierdo = self.rotacion_izquierda(nodo.izquierdo)
            return self.rotacion_derecha(nodo)

        # Caso derecha-izquierda
        if balanceo < -1 and valor < nodo.derecho.valor:
            nodo.derecho = self.rotacion_derecha(nodo.derecho)
            return self.rotacion_izquierda(nodo)

        return nodo

    def insertar_valor(self, valor):
        self.raiz = self.insertar(self.raiz, valor)

    def recorrer_inorden(self, nodo):
        if not nodo:
            return
        self.recorrer_inorden(nodo.izquierdo)
        print(nodo.valor, end=" ")
        self.recorrer_inorden(nodo.derecho)

    def recorrer(self):
        self.recorrer_inorden(self.raiz)

    def  generar_arbol_grafico(self):
        dot = graphviz.Digraph()
        self._generar_arbol_grafico(self.raiz, dot)

        archivo_salida = "arbol.dot"
        dot.render(archivo_salida, format='png', cleanup=True)

        startfile(archivo_salida + '.png')

    def _generar_arbol_grafico(self, nodo, dot):
        if nodo is not None:
            dot.node(str(nodo.valor))
            if nodo.izquierdo is not None:
                dot.edge(str(nodo.valor), str(nodo.izquierdo.valor))
                self._generar_arbol_grafico(nodo.izquierdo, dot)
            if nodo.derecho is not None:
                dot.edge(str(nodo.valor), str(nodo.derecho.valor))
                self._generar_arbol_grafico(nodo.derecho, dot)



# Ejemplo de uso
arbol = ArbolAVL()
valores = [1, 2, 3, 4, 5, 8]

for valor in valores:
    arbol.insertar_valor(valor)

arbol.generar_arbol_grafico()
print("Recorrido inorden del árbol AVL:")
arbol.recorrer()