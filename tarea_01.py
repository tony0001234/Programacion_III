from os import system #importo os para utilizar funcionalidades dependientes del sistema operativo, en este caso el system("cls")

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
    