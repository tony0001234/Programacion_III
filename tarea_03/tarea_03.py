from os import system, startfile #importo system para utilizar funcionalidades dependientes del sistema operativo, en este caso el system("cls")
import graphviz, re#importo la libreria para utilizar graphviz y poder implementar la creacion del grafico, tambien importo la libreria "re" que me ayuda con la creacion y utilizacion de mi archivo

class NodoA:#comienzo mi clase nodo
    def __init__(self, valor):#inicializo mi clase con self y valor, self para poder interactuar con la misma clase y valor para guardar los valores numericos del arbol
        self.valor = valor#al cominezo solo inicio valor igual a valor, para que despues contenga el valor deseado
        self.izq = None#inicializo izq como none para que mi primer nodo no tenga hijos y despues al agregar se vayan generando
        self.der = None#inicializo der como none para que mi primer nodo no tenga hijos y despues al agregar se vayan generando

class ABB:#inicio a redactar mi clase arbol de busqueda binaria, como ABB
    def __init__(self):#solo lo inicializo con self
        self.raiz = None#inicializo raiz para que sea el principio de mi arbol, pero lo pongo igual a None porque aun nose a agregado nodos
    
    def insert(self, valor):#defino mi primer metodo, este solo es para hacer un llamado mas limpio a la hora de insertar valores, iniciandolo con self y valor
        self.raiz = self.inserta2(valor, self.raiz)#este metodo unicamente iguala raiz a self.inserta2 para ahora si con recursividad comenzar ainsertar el nodo, mando self para uso de izquierda y derecha, self.raiz porque de la raiz se comienza
    def inserta2(self, valor, nodo):#inicializo mi metodo para insertar recursivamente, mandandole self para usar izq, der, mando el valor y el nodo como tal en donde se inicia a insertar osea raiz
        if(nodo is None):#si en el arbol no hay nada osea si nodo es None
            print(f"Valor: {valor} insertado correctamente")#mando un mensaje de confirmacion de insercion del valor
            return NodoA(valor)#regreso/retorno NodoA(valor) para incertar el valor en el arbol y dejarlo como nodo
        if(valor < nodo.valor):#si hay valores entonces se verifica si el valor es menor a los nodos habientes
            nodo.izq = self.inserta2(valor, nodo.izq)#de ser asi igualo el nodo de la derecha a self.inserta2() mandando el valor que deseo insertar nuevamente y el nodo siguiente para verificar si se inserta como un hijo de este o hay que seguir
        if(valor > nodo.valor):#si ha valores se verifica si el valor es mayor a los nodos que hay
            nodo.der = self.inserta2(valor, nodo.der)#de ser asi igualo el nodo de la derecha a self.inserta2() mandando el valor que deseo insertar nuevamente y el nodo siguiente para verificar si se inserta como un hijo de este o hay que seguir
        return nodo#de ser un valor repetido solamente lo ignoro retornando nodo, ya que ninguno de los condicionales anteriores se cumple
    
    def insertArchi(self, valores):#creo un proceso para insertar cuando es archivo, ya que hago unas cuantas cosas antes de mandar el valor de una vez
        if(  isinstance(valores, list)  ):#verifioc si valores esta instanceado/inicializado a un valor, y si es del tipo list o lista
            for valor in valores:#uso un for para insertar los valores de esta variable e insertaros en valor uno por uno
                self.raiz = self.inserta2(valor, self.raiz)#envio cada valor en cada vuelta del for hacia el metodo insertArchiva2
        else:#si los valores no son una instancia de una lista entoces
            self.raiz = self.inserta2(valor, self.raiz)#solamente inserta el valor encontrado

    def buscar(self, valor):#defino mi primer metodo, este solo es para hacer un llamado mas limpio a la hora de insertar valores, iniciandolo con self y valor
        return self.busca2(valor, self.raiz)#este metodo unicamente retorna self.busca2 para ahora si con recursividad comenzar a buscar el nodo, mando self para uso de izquierda y derecha, self.raiz porque de la raiz se comienza
    def busca2(self, valor, nodo):#inicio con el metodo de buscado, recibiendo self, el valor a buscar y el nodo de inicio o raiz 
        if(nodo is None):#si en el arbol no hay nada osea si nodo es None
            print("No se encontro el valor")#imprimo en consola que no se encontro el valor
            return None#regreso None para seguir utilizando el programa
        if(nodo.valor == valor):#si el valor del nodo a verificar es igual al valor que estoy buscando
            print("Encontrado: "+str(nodo.valor))#despliego en consola que se encontro el nodo y despliego el valor del nodo
            return nodo#retorno nodo para poder reutilizarlo o imprimir mas datos si es que ubieran
        if(valor < nodo.valor):#si el valor que estoy buscando es menor al nodo actual
            return self.busca2(valor, nodo.izq)#retorno el mismo metodo mandando de nuevo el valor a buscar y posicionandome en el nodo que sigue a la izquierda
        else:#de no ser menor entonces
            return self.busca2(valor, nodo.der)#retorno a este mismo metodo con el valor a buscar y posicionandome en el nodo siguiente a la derecha
        
    def eliminar(self, valor):#inicio con un metodo de llamado igual que en mis dos incerciones
        self.raiz = self.elimina2(self.raiz, valor)#lo unico que hago es igualar raiz al metod para eliminar el nodo buscado mandando el nodo inicial(raiz) y el valor a eliminar
    def elimina2(self, nodo, valor):#comienzo el metodo eliminar recibiendo el nodo de inicio(raiz) y el valor a eliminar
        if(nodo is None):#si el nodo no esta entonces
            return nodo#regreso nodo para ignorarlo

        if(valor < nodo.valor):#si el valor a eliminar es menor que el valor del nodo en el que estoy posicionado entonces
            nodo.izq = self.elimina2(nodo.izq, valor)#igualo el nodo siguiente a la izquierda a este mismo metodo enviando la posicion siguiente a valorar y el valor a eliminar para seguir comparando
        elif(valor > nodo.valor):#encambio si el valor es mayor entonces
            nodo.der = self.elimina2(nodo.der, valor)#igualo el nodo siguiente a la derecha al mismo metodo enviando la posicion siguiente a valorar y el valor a eliminar para seguir comparando
        
        else:#sino entonces 
            if(nodo.izq is None):#nodo con solo un hijo o sin hijos verifica si el nodo a la izquierda es igual a none
                temp = nodo.der#iguala la variable temporal al nodo a la derecha ya que es el que queda
                nodo = None#elimino el nodo igualandolo a None
                return temp#regreso el nodo temporal ya enlazado en el arbol
            elif(nodo.der is None):#verifico lo mismo pero para el cazo de que el nodo de la derecha sea igual a None osea no haya nodo a la derecha
                temp = nodo.izq#igualo el nodo temporal al nodo de la izquierda 
                nodo = None#eliminio el nodo buscado igualandolo a None
                return temp#retorno el nodo temporal

            temp = self.valorMin(nodo.der)#nodo con dos hijos, agarro el sucesor en modo inOrder, utilizando un metodo aparte para encontrar el valor minimo del arbol que esta anterior al deseado a eliminar
            nodo.valor = temp.valor#Copio el valor del sucesor para el nodo en mi variable temporal
            nodo.der = self.elimina2(nodo.der, temp.valor)#elimino el sucesor, llamando de nuevo a este metodo enviando como parametros el nodo a la derecha y el valor del nodo temporal
        return nodo#regreso nodo si es que el valor a eliminar no se encuentra dentro del arbol
    
    def valorMin(self, nodo):#metodo para ayudar a la eliminacion, unicamente recorre el arbol buscando desde el valor a eliminar el valor menor mas cercano a este
        actual = nodo#igualo actual una variable de apoyo al nodo pasado, para utilizar un puntero diferente
        while actual.izq:#utilizo un bucle while para decir, mientras haya nodo a la izquierda
            actual = actual.izq# sigo recorriendo los nodos hasta llegar a un nodo hoja
        return actual#retorno el nodo actual, para volverlo a insertar remplazando el nodo a eliminar

    def preOrderGrap(self, nodo):#creo un metodo solo para recorrer los valores del nodo, me ayudo con el desarrollo del programa

        if(nodo != None):#si el nodo es distinto de None, osea si el arbol tiene valores
            print(nodo.valor)#imprimo el valor de raiz

            if(nodo.izq != None):#si el nodo izquierda tien valor
                self.preOrderGrap(nodo.izq)#retorno el valor hacia este mismo metodo para imprimir el valor de la izquierda
            if(nodo.der != None):#si el nodo derecha tiene valor 
                self.preOrderGrap(nodo.der)#retorno el valor hacia este mismo metodo para imprimir el valor de la izquierda

    numeroDeNodos=0#Utilizo esta variable para corroborar cuantos valores hay en mi arbol, esta me ayuda para insertar en mi grafico el primer valor, el nodo raiz
    def generate_graph(self):#inicio con el metodo para generar mi grafico del arbol
        dot = graphviz.Digraph(comment='Arbo_B_B')#igualo la variable dot a graphviz.Digraph(comment='Arbo_B_B'), para iniciar a diagramar tipo graphviz y darle el nombre de Arbol_B_B
        
        def add_edges(nodo):#metodo para insertar los hijos en el grafico
            if(nodo != None):#valido si el nodo tiene un valor entonces
                if(nodo.izq):#valido si hay nodo izquierda
                    dot.edge(  str(nodo.valor), str(nodo.izq.valor), label='izq')#si hay nodo izquierda entonces inserto el valor con la etiqueta de izq en el enlace
                    add_edges(nodo.izq)#agrego al grafico el nodo izquierdo
                    self.numeroDeNodos +=1#sumo 1 al total de nodos que tengo, en realidad solo me interesa que cambie de cero cuando ya hay mas de 1 nodo
                if(nodo.der):#si hay nodo a la derecha entonces
                    dot.edge(  str(nodo.valor), str(nodo.der.valor), label='der')#creo el nodo con el valor y el enlace con la etiqueta der
                    add_edges(nodo.der)#inserto al grafico el valor del nodo derecha
                    self.numeroDeNodos +=1#sumo 1 al total de nodos que tengo, en realidad solo me interesa que cambie de cero cuando ya hay mas de 1 nodo
                elif(self.numeroDeNodos == 0):#sino valido si hay cero nodos graficados entonces creo un nodo solitario sin enlaces
                    dot.node(  str(  id(nodo)  ), str(nodo.valor)  )#creo un nodo solitario sin enlaces con el valor del nodo raiz y dejandolo como el primer nodo
                    self.numeroDeNodos +=1#aumento en 1 el contador de nodos para no volver a repetir este bucle jamas hasta que la memoria sea receteada
        add_edges(self.raiz)#agrego los nodos a la grafica desde la raiz
        return dot #retorno el valor de la grafica para despues convertirlo en un archivo del tipo requerido
    
def menu():#creo un proceso menu, para modificar facilmente el menu y como se imprime enconsola
    print("__________________Menu__________________")
    print("1. Insertar.")
    print("2. Buscar.")
    print("3. Eliminar.")
    print("4. Insertar valores desde txt.")
    print("5. Salir.")

arbol = ABB()#instancion mi clase ABB como arbol
while True:#creo un bucle True para seguir ejecutando el programa hasta introducir la opcion para salir

    menu()#llamo a mi metodo menu para que me inprima en consola el menu
    try:#utilizo el try como trato, para
        opc = int(input("Ingrese una opcion: "))#trato de leer el valor ingresado por el usuario, convertirlo en un entero
    except ValueError as e:#si no sale bien el proceso porque el usuario introdujo un valor erroneo entonces
        print("Error: Porfavor ingrese un valor valido")#imprimo que hubo un error 
        print(f"Error: {e}")#imprimo el error en especifico

    if(opc == 1):#Opcion insertar del menu
        system("cls")#limpio la consola para comenzar a pedir el valor a ingresar
        try:#trato de volver entero el valor ingresado por el usuario y guardarlo en la variable valorIn
            valorIn = int(input("Ingresa un numero entero para agregar al arbol: "))#pido el valor y lo convierto en entero para guardarlo en la variable valorIn
            arbol.insert(valorIn)#inserto el valor en arbol.insert que llama mi primer metodo de insercion pasando el valor a insertar

            graph = arbol.generate_graph()#igualo mi variable graph al metodo para generar el grafico
            graph.render('Arbol_B_B', format='png', cleanup=True)#le doy la instriccion a mi variable para comienze a generar el archivo con conmbre Arbol_B_B en formato png y que cada vez que se repita esa instruccion se elimine el anterior para volverlo a generar actualizado
            startfile('Arbol_B_B.png')#abro mi archivo png para poder visualizar mi arbol

        except ValueError as e:#de no poderse hacer algo de lo anterior
            print("Error: Porfavor ingrese un valor valido")#imprimo que hubo un error 
            print(f"Error: {e}")#imprimo el error en especifico

    elif(opc == 2):#Opcion buscar
        system("cls")#limpio la consola para comenzar a pedir el valor a ingresar
        try:#trato de volver entero el valor ingresado por el usuario y guardarlo en la variable valorIn
            valorBus = int(input("Introdusca el valor que desea buscar: "))#pido el valor y lo convierto en entero para guardarlo en la variable valorIn
            arbol.buscar(valorBus)#inserto el valor en arbol.bsucar que llama mi primer metodo de busqueda

            graph = arbol.generate_graph()#igualo mi variable graph al metodo para generar el grafico
            graph.render('Arbol_B_B', format='png', cleanup=True)#le doy la instruccion a mi variable para comienze a generar el archivo con conmbre Arbol_B_B en formato png y que cada vez que se repita esa instruccion se elimine el anterior para volverlo a generar actualizado
            startfile('Arbol_B_B.png')#abro mi archivo png para poder visualizar mi arbol

        except ValueError as e:#de no poderse hacer algo de lo anterior
            print("Error: Porfavor ingrese un valor valido.")#imprimo que hubo un error 
            print(f"Error: {e}")#imprimo el error en especifico

    elif(opc == 3):#Opcion Eliminar
        system("cls")#limpio la consola para comenzar a pedir el valor a ingresar
        try:#trato de volver entero el valor ingresado por el usuario y guardarlo en la variable valorIn
            valorElim = int(  input("Introdusca el valor que desea eliminar: ")  )#pido el valor y lo convierto en entero para guardarlo en la variable valorIn
            arbol.eliminar(valorElim)#inserto el valor en arbol.eliminar que llama mi primer metodo de eliminacion pasando el valor a eliminar

            print("Valor eliminado!!!!")#imprimo que el valor a sido eliminado
            graph = arbol.generate_graph()#genero nuevamente mi arbol para actualizar que ya no tiene el nodo eliminado
            graph.render('Arbol_B_B', format='png', cleanup=True)#comineza a generar el grafico actualizado
            startfile('Arbol_B_B.png')#abro mi grafico actualizado
        
        except ValueError as e:#de no poderse hacer algo de lo anterior
            print("Error: Porfavor ingrese un valor valido.")#imprimo que hubo un error 
            print(f"Error: {e}")#imprimo el error en especifico


    elif(opc == 4):#Opcion cargar desde archivo
        system("cls")#limpio la consola para comenzar a pedir el valor a ingresar
        direArch = input("Ingrese la direccion del archivo sin comillas simples, solo la pura direccion porfavor: ")#pido que introdusca la direccion del archivo sin comillas para guardarla en la variable direArch
        #print(direArch)

        positivoEnt = []#creo un arreglo para guardar los numeros positivos que aparescan en el archivo
        negativoEnt = []#creo un arreglo para guardar los numeros negativos que aparescan en el archivo
        with open(direArch, 'r') as arch:#with da contexto de con que herramienta quiero que haga cierta instruccion, con open() abro el archivo dando la ruta y el modo en el que se abre el archivo, 'r' este es el modo de lectura, solo lee no modifica
            for linea in arch:#utilizo un bucle for para insertar uno por uno en cada vuelta los valores devueltos de arch en linea, para trabajar linea por linea por asi  decirlo
                enteros = re.findall(r'[-+]?\d+', linea)#igualo una variable entrero que contendra los valores de linea a re.findall re trabaja con expresiones regulares, findall() busca todas las apariciones de un patron dentro de una cadena y devuelve una lista de todas las coincidencias, en resumen, busco los numeros positivos y negativos para identificarlos y separarlos
                for entero in enteros:#utilizo otro for para guardar uno por uno los valores encontrados de enteros en entero
                    if( entero.startswith('-') ):#si el valor contiene el guion o el signo menos
                        negativoEnt.append(  int(entero)  )#vuelvo el numero entero y lo asigno a los numero negativos en mi arreglo
                    else:#sino, osea si es positivo
                        positivoEnt.append(  int(entero)  )#lo asigno con mis numeros positivos 

        arbol.insertArchi(positivoEnt)#introdusco todos los valores positivos de mis arreglos en el arbol con su metodo en especifico
        arbol.insertArchi(negativoEnt)#introdusco todos los valores negativos de mis arreglos en el arbol con su metodo en especifico


        graph = arbol.generate_graph()#igualo mi variable graph al metodo para generar el grafico
        graph.render('Arbol_B_B', format='png', cleanup=True)#le doy la instriccion a mi variable para comienze a generar el archivo con conmbre Arbol_B_B en formato png y que cada vez que se repita esa instruccion se inserten los valores del archivo para volverlo a generar actualizado
        startfile('Arbol_B_B.png')#abro mi archivo png para poder visualizar mi arbol


    elif(opc == 5):#Opcion salir
        break#uso break para salir del bucle y terminar el programa
        
    else:#uso este else, sino introduce ningun valor anterior mencionado entonces
        system("cls")#limpio la consola para comenzar a pedir el valor a ingresar
        print("Opcion invalida, porfavor ingrese una opcion del menu")#imprimo un mensaje de opcion invalida, introdusca un valor valido
