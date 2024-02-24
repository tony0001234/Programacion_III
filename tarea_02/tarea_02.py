from os import system, startfile #importo os para utilizar funcionalidades dependientes del sistema operativo, en este caso el system("cls")
from math import sqrt

def menu():
    print()
    print("/////////////////////MENU PRINCIPAL////////////////////////////")
    print("1. Convertir a binario")
    print("2. Contar digitos")
    print("3. Raiz cuadrada entera")
    print("4. Convertir a decimal desde Romano")
    print("5. Suma de numeros enteros")
    print("6. Salir")

def convertir_a_binario(numeroABin):
    if(numeroABin < 0):
        raise ValueError
    if(numeroABin == 0):
        return "0"
    elif(numeroABin == 1):
        return "1"
    else:
        return convertir_a_binario(numeroABin // 2) + str(numeroABin % 2)
    
def contar_digitos(numeroCD):
    if(abs(numeroCD) < 10):
        return 1
    else:
        return 1 + contar_digitos(abs(numeroCD) // 10)

def raiz_cuadrada_entera(numeroEn):
        if(numeroEn < 0):
            print("Error: Debes utilizar numeros positivos para raiz cuadrada")
        else:
            print(f"La raiz cuadrada aproximada al entero mas cercano de: {numero3} Es: {calcular_raiz_cuadrada(numero3)}")

def calcular_raiz_cuadrada(numeroRC):
    return round(sqrt(numeroRC))

def convertir_a_decimal(numeroRm):
    caracteresRm = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if not numeroRm:
        return 0
    if(len(numeroRm) == 1):
        return caracteresRm[numeroRm[0]]
    if(caracteresRm[numeroRm[0]] < caracteresRm[numeroRm[1]]):
        return caracteresRm[numeroRm[1]] - caracteresRm[numeroRm[0]] + convertir_a_decimal(numeroRm[2:])
    else:
        return caracteresRm[numeroRm[0]] + convertir_a_decimal(numeroRm[1:])




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
            print("Error: Porfavor ingrese un valor valido")
            print(f"Error: {e}")
    
    elif(opc == "2"):
        system("cls")
        try:
            numero2 = int(input("Ingrese un numero entero para calcular sus digitos: "))
            numeroDigi = contar_digitos(numero2)
            print(f"La cantidad de digitos del numero: {numero2} Es: {numeroDigi}")
        except ValueError as e:
            print("Error: Porfavor ingrese un valor valido")
            print(f"Error: {e}")

    elif(opc == "3"):
        numero3 = 0
        system("cls")
        try:
            numero3 = float(input("Ingrese un numero positivo para calcularla raiz cuadrada entera: "))
            raiz_cuadrada_entera(numero3)
        except ValueError as e:
            print("Error: Porfavor ingrese un valor valido")
            print(f"Error: {e}")
            
    elif(opc == "4"):
        system("cls")
        try:
            numeroRom = input("Ingrese el numero Romano que desea convertir: ").upper()
            numeroDec = convertir_a_decimal(numeroRom)
            print(f"El numero romano: {numeroRom} en decimales es: {numeroDec}")

        except ValueError as e:
            print("Error: Porfavor ingrese un valor valido")
            print(f"Error: {e}")

    elif(opc == "6"):
        break
    else:
        system("cls")
        print("Opcion invalida, porfavor ingrese una opcion del menu")
        
            