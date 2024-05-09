import graphviz, csv
from graphviz import Digraph
import os
from os import startfile, system

class Nodo:
    def __init__(self, fila, columna, valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor
        self.siguiente = None

class MatrizDispersa:
    def __init__(self, num_filas, num_columnas):
        self.num_filas = num_filas
        self.num_columnas = num_columnas
        self.cabezas_filas = [None] * num_filas

    def insertar_valor(self, fila, columna, valor):
        if fila < 0 or fila >= self.num_filas or columna < 0 or columna >= self.num_columnas:
            raise ValueError("Las coordenadas están fuera de los límites de la matriz")

        nuevo_nodo = Nodo(fila, columna, valor)
        if self.cabezas_filas[fila] is None:
            self.cabezas_filas[fila] = nuevo_nodo
        else:
            self._insertar_valor_aux(self.cabezas_filas[fila], nuevo_nodo)

    def _insertar_valor_aux(self, actual, nuevo_nodo):
        if actual.columna == nuevo_nodo.columna:
            actual.valor = nuevo_nodo.valor
        elif actual.columna < nuevo_nodo.columna:
            if actual.siguiente is None or actual.siguiente.columna > nuevo_nodo.columna:
                nuevo_nodo.siguiente = actual.siguiente
                actual.siguiente = nuevo_nodo
            else:
                self._insertar_valor_aux(actual.siguiente, nuevo_nodo)
        else:
            nuevo_nodo.siguiente = actual
            self.cabezas_filas[actual.fila] = nuevo_nodo

    def imprimir_matriz(self):
        for fila in range(self.num_filas):
            nodo_actual = self.cabezas_filas[fila]
            for columna in range(self.num_columnas):
                if nodo_actual is not None and nodo_actual.columna == columna:
                    print(nodo_actual.valor, end=" ")
                    nodo_actual = nodo_actual.siguiente
                else:
                    print("0", end=" ")
            print()

    def insert_arch(self, Narchivo):
        num_filas = 0
        num_columnas = 0

        direccion = os.path.dirname(os.path.abspath(__file__))
        archivo = os.path.join(direccion, Narchivo)
        with open(archivo, 'r', newline='') as archivo_csv:
            #lector_csv = csv.DictReader(archivo_csv)
            for fila in archivo_csv:
                num_filas += 1
                try:
                    datosSeparados = fila.split(",")
                    
                    #valores.append(datosSeparados)
                    for valor in datosSeparados:
                        num_columnas += 1
                        #print(f"valores f{num_filas} c{num_columnas}: {valor}")
                        self.insertar_valor(num_filas, num_columnas, valor)
                    num_columnas = 0
                    estado = True
                except KeyError:
                    estado = False
                    continue

        return estado
    
    def buscar_valor(self, fila, columna):
        if fila < 0 or fila >= self.num_filas or columna < 0 or columna >= self.num_columnas:
            raise ValueError("Las coordenadas están fuera de los límites de la matriz")

        # Llamar a la función auxiliar para realizar la búsqueda
        return self._buscar_valor_aux(self.cabezas_filas[fila], columna)

    def _buscar_valor_aux(self, nodo_actual, columna_buscada):
        if nodo_actual is None:  # Caso base: no se encontró el valor en la fila
            return 0  # Retornar 0 si no se encuentra el valor en la fila

        if nodo_actual.columna == columna_buscada:
            return nodo_actual.valor  # Retornar el valor si se encuentra en el nodo actual
        elif nodo_actual.columna < columna_buscada:
            # El valor buscado está más adelante en la fila, continuar la búsqueda
            return self._buscar_valor_aux(nodo_actual.siguiente, columna_buscada)
        else:
            # El valor buscado no está en esta fila, retornar 0
            return 0

    def dibujar_grafo(self):
        grafo = Digraph()

        # Crear nodos
        for fila in range(self.num_filas):
            for columna in range(self.num_columnas):
                try:
                    valor = float(self.buscar_valor(fila, columna))
                except ValueError:
                    valor = self.buscar_valor(fila, columna)
                if valor != 0:
                    grafo.node(f"{fila}-{columna}", label=str(valor))

        # Crear aristas
        for fila in range(self.num_filas):
            for columna in range(self.num_columnas):
                try:
                    valor = float(self.buscar_valor(fila, columna))
                except ValueError:
                    valor = self.buscar_valor(fila, columna)
                if valor != 0:
                    # Arista hacia abajo
                    if fila + 1 < self.num_filas:
                        valor_destino = self.buscar_valor(fila + 1, columna)
                        if valor_destino != 0:
                            grafo.edge(f"{fila}-{columna}", f"{fila+1}-{columna}")
                    # Arista hacia la derecha
                    if columna + 1 < self.num_columnas:
                        valor_destino = self.buscar_valor(fila, columna + 1)
                        if valor_destino != 0:
                            grafo.edge(f"{fila}-{columna}", f"{fila}-{columna+1}")
        grafo.render('Matriz_D', format='png', cleanup=True)
        startfile('Matriz_D.png')

def insert_arch_num_F_C(Narchivo):
    num_filas = 0
    num_columnas = 0

    direccion = os.path.dirname(os.path.abspath(__file__))
    archivo = os.path.join(direccion, Narchivo)
    with open(archivo, 'r', newline='') as archivo_csv:
       # lector_csv = csv.DictReader(archivo_csv)
        for fila in archivo_csv:
            num_filas += 1
            valores = fila.split(",")
            num_columnas = 0
            for valor in valores:
                num_columnas += 1
                #try:
                    #datosSeparados = fila[encabezado].split(",")

                    #valores.append(datosSeparados)
                #except KeyError:
                 #   continue

    return num_filas, num_columnas

def menu():#creo un proceso menu, para modificar facilmente el menu y como se imprime enconsola
    print("__________________Menu__________________")
    print("1. Insertar valores del archivo .csv.")
    print("2. Insertar valores manualmente.")
    print("3. Visualizar en consola.")
    print("4. Visualizar en graphviz.")
    print("5. Salir.")

############################################

Narchivo = input("ingrese el nombre del archivo: ")+".csv"

num_filas, num_columnas = insert_arch_num_F_C(Narchivo)

matriz = MatrizDispersa(num_filas+1, num_columnas+1)

while True:#creo un bucle True para seguir ejecutando el programa hasta introducir la opcion para salir
    menu()#llamo a mi metodo menu para que me inprima en consola el menu
    try:#utilizo el try como trato, para
        opc = int(input("Ingrese una opcion: "))#trato de leer el valor ingresado por el usuario, convertirlo en un entero
    except ValueError as e:#si no sale bien el proceso porque el usuario introdujo un valor erroneo entonces
        print("Error: Porfavor ingrese un valor valido")#imprimo que hubo un error 
        print(f"Error: {e}")#imprimo el error en especifico

    if(opc == 1):#Opcion Insertar valores de heart_failure_clinical_records_dataset.csv.
        system("cls")#limpio la consola para comenzar a pedir el valor a ingresar
        if matriz.insert_arch(Narchivo) is None:
            print("Ocurrio un error en la insercion y lectura del archivo: insert_arch")
        else:
            print("Datos ingresados correctamente!!!")
        

    elif(opc == 2):#Opcion Insertar valores manualmente.
        system("cls")#limpio la consola para comenzar a pedir el valor a ingresar
        try:
            valor = input("Ingrese el valor: ")
            fila = int(input("Ingrese el numero de fila donde desea guardarlo: "))
            columna = int(input("Ingrese el numero de columna donde desea guardarlo: "))
        except ValueError as e:
            print("Error: Porfavor ingrese un valor valido")#imprimo que hubo un error 
            print(f"Error: {e}")#imprimo el error en especifico

        matriz.insertar_valor(fila, columna, valor)
        print("Valor ingresado correctamente")

    elif(opc == 3):#Opcion Visualizar en consola
        system("cls")#limpio la consola para comenzar a pedir el valor a ingresar
        matriz.imprimir_matriz()

    elif(opc == 4):#Opcion Visualizar en graphviz
        system("cls")#limpio la consola para comenzar a pedir el valor a ingresar
        matriz.dibujar_grafo()

        print("Generado correctamente!!!!!!!!!")

    elif(opc == 5):#Opcion salir
        break#uso break para salir del bucle y terminar el programa
        
    else:#uso este else, sino introduce ningun valor anterior mencionado entonces
        system("cls")#limpio la consola para comenzar a pedir el valor a ingresar
        print("Opcion invalida, porfavor ingrese una opcion del menu")#imprimo un mensaje de opcion invalida, introdusca un valor valido
