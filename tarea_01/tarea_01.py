from os import system #importo os para utilizar funcionalidades dependientes del sistema operativo, en este caso el system("cls")

class Nodo:
    def__init__(self, nombre, apellido, carne)
    self.nombre = nombre
    self.apellido = apellido
    self.carne = carne
    self.sig = None
    self.ant = None

class lista2ble:
    def__init__(self)
    self.head = None
    self.taile = None

def agregar_ele(self, nombre, apelldio, carne):
    nuevo_nodo = Nodo(nombre, apelldio, carne)
    nuevo_nodo.sig = self.head
    self.head = nuevo_nodo
    nuevo_nodo.ant = self.taile

while True:
    print("/////////////////////MENU PRINCIPAL////////////////////////////")
    print("1. Insertar al principio")
    print("2. Insertar al final")
    print("3. Eliminar valor")
    print("4. Mostrar lista")
    print("5. Salir")
    opc = input("Ingrese una opcion")
    
    if opc =="1":
        system("cls")
        print("Presiono la opcion 1")
    elif opc =="2":
        system("cls")
        print("Presiono la opcion 2")
    elif opc =="3":
        system("cls")
        print("Presiono la opcion 3")
    elif opc =="4":
        system("cls")
        print("Presiono la opcion 4")
    elif opc =="5":
        break
    else:
        system("cls")
        print("Opcion invalida, porfavor ingrese una opcion del menu")
    