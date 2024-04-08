import csv
def agregarArch():
        with open(input('Seleccione un archivo CSV: '),'r', newline='') as csvfile:
            lector_csv = csv.DictReader(csvfile)
            print("encabezados: ", lector_csv.fieldnames)
            #encabezado = lector_csv.fieldnames[0]
            for encabezado in lector_csv.fieldnames:
                print(f"ENCABEZADO: {encabezado}")
                #encabezado = lector_csv.fieldnames[i]
                for fila in lector_csv:
                    try:
                        #print(fila[encabezado])
                        datosSeparados = fila[encabezado].split(";")
                        print (datosSeparados)

                    except KeyError:
                        print("no existe la columna 'id' en la fila")
                 
           # for fila in lector_csv:
                #self.agregar_elemento(fila['id'])
                #print("fila: ", fila['id'])

                

agregarArch()