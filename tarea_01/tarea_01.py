from os import system #importo os para utilizar funcionalidades dependientes del sistema operativo, en este caso el system("cls")

class Nodo:
    def__init__(self, nombre, apellido, carne)
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

def agregar_ele(self, nombre, apelldio, carne):
        nuevo_nodo = Nodo(nombre, apelldio, carne)

if self.inicio is None:
        self.inicio = nuevo_nodo
        self.final = self.inicio

else:
     nodo.ant = self.final
     self.final.sig = nuevo_nodo
     self.final = nuevo_nodo

     self.contador += 1

     def recorrer(self):
          actual = self.inicio

          while actual:
               dato = actual.nombre
               actual = actual.sig
               yield nombre

lista = lista2ble()

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
        print("Presiono la opcion 1 /n")
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        carne = input("Ingrese el numero de carne: ")
        lista.agregar_ele(nombre, apellido, carne)
        print ('Cantidad de elementos en la lista', lista.contador)
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
    