from os import system #importo os para utilizar funcionalidades dependientes del sistema operativo, en este caso el system("cls")

class Nodo:
    def __init__(self, nombre, apellido, carne):
        self.nombre = nombre
        self.apellido = apellido
        self.carne = carne
        self.sig = None
        self.ant = None
    
class lista2ble:
    def __init__(self):
        self.inicio = None
        self.final = None
        self.contador = 0

    def agregar_ele(self, nombre, apellido, carne):
        nuevo_nodo = Nodo(nombre, apellido, carne)

        if self.inicio is None:
            self.inicio = nuevo_nodo
            self.final = self.inicio
            self.contador += 1

        else:
            nuevo_nodo.ant = self.final
            self.final.sig = nuevo_nodo
            self.final = nuevo_nodo

            self.contador += 1

    def agregar_ele_final(self, nombre, apellido, carne):
        nuevo_nodo = Nodo(nombre, apellido, carne)

        if self.inicio is None:
            self.inicio = nuevo_nodo
            self.final = self.inicio
            self.contador += 1

        else:
            nuevo_nodo.sig = self.final
            self.final.ant = nuevo_nodo
            self.inicio = nuevo_nodo

            self.contador += 1

    def recorrer(self):
          actual = self.inicio

          while actual:
               nombreAct = actual.nombre
               apellidoAct = actual.apellido
               carneAct = actual.carne
               actual = actual.sig
               textoEnt = "\n\n" + 'Nombre: ' + nombreAct + "\n" + 'Apellido: ' + apellidoAct + "\n" + 'Carne: ' + carneAct
               yield textoEnt

lista = lista2ble()

while True:
    print("/////////////////////MENU PRINCIPAL////////////////////////////")
    print("1. Insertar al principio")
    print("2. Insertar al final")
    print("3. Eliminar valor")
    print("4. Mostrar lista")
    print("5. Salir")
    opc = input("Ingrese una opcion: ")
    
    if opc =="1":
        system("cls")
        print("Presiono la opcion: 1")
        nombreIn = input("Ingrese el nombre: ")
        apellidoIn = input("Ingrese el apellido: ")
        carneIn = input("Ingrese el numero de carne: ")
        lista.agregar_ele_final(nombreIn, apellidoIn, carneIn)
        print ('Cantidad de elementos en la lista', lista.contador)

    elif opc =="2":
        system("cls")
        print("Presiono la opcion: 2")
        nombreIn = input("Ingrese el nombre: ")
        apellidoIn = input("Ingrese el apellido: ")
        carneIn = input("Ingrese el numero de carne: ")
        lista.agregar_ele(nombreIn, apellidoIn, carneIn)
        print ('Cantidad de elementos en la lista', lista.contador)

    elif opc =="3":
        system("cls")
        print("Presiono la opcion: 3")

    elif opc =="4":
        system("cls")
        print()
        print("Presiono la opcion: 4")
        print('Cantidad de elementos en la lista: ', lista.contador)
        print()

        for reco in lista.recorrer():
            print(reco)
    elif opc =="5":
        break
    else:
        system("cls")
        print("Opcion invalida, porfavor ingrese una opcion del menu")
    