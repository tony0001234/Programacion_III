from os import system, startfile #importo os para utilizar funcionalidades dependientes del sistema operativo, en este caso el system("cls")

def menu():
    print()
    print("/////////////////////MENU PRINCIPAL////////////////////////////")
    print("1. Convertir a binario")
    print("2. Contar digitos")
    print("3. Raiz cuadrada entera")
    print("4. Convertir a decimal desde Romano")
    print("5. Suma de numeros enteros")
    print("6. Salir")

"""def convertir_a_binario(numeroABin):
    if(numeroABin == 0):
        return ""
    else:
        return convertir_a_binario(numeroABin // 2)+str(numeroABin % 2)

        """
def convertir_a_binario(numeroABin):
    if(numeroABin < 0):
        raise ValueError
    if(numeroABin == 0):
        return "0"
    elif(numeroABin == 1):
        return "1"
    else:
        return convertir_a_binario(numeroABin // 2) + str(numeroABin % 2)

def es_entero(numero):
    try:
        valorI = int(numero)
        return True, valorI
    except ValueError:
        return False, None

while True:

    menu();

    opc = input("Ingrese una opcion: ")

    if(opc == "1"):
        system("cls")
        try:
            numeroIn = int(input("Ingresa un numero entero no negativo: "))
            numeroConv = convertir_a_binario(numeroIn)
            print(f"El numero: {numeroIn} En binario es: {numeroConv}")
        except ValueError as e:
            print("Error: porfavor ingrese un valor valido")
            print(f"Error: {e}")

    elif(opc == "6"):
        break
    else:
        system("cls")
        print("Opcion invalida, porfavor ingrese una opcion del menu")
        
            