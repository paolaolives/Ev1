from collections import namedtuple 
import datetime
import time

diccionario_servicio = {} #creamos diccionario para que la key sea folio
dicc_serv={} #creamos diccionario para que la key sea fecha
Servicio = namedtuple ("Servicio", ( "nombre_cliente", "fecha","descrip_serv", "descrip_equipo", "monto", "resultado")) #tupla nominada

while True:
    print("\n*** M E N Ú ***") #menu con 4 opciones
    print("1- Registrar servicio")
    print("2- Consultar servicio según folio")
    print("3- Consultar servicio según fecha")
    print("4- Revisar todos los servicios registrados")
    print("5- Salir\n")

    opcion = int(input("Introduzca el dígito para realizar una operación del menú: "))
    print("x"*85)

    while opcion == 1:  

        while True:           
            print("\n S E R V I C I O  D E  S O P O R T E  T E C N I C O") #segundo menú para los servicios que se ofrecen
            print("1. Auditoría de Software y/o Hardware") 
            print("2. Reparaciones técnicas") 
            print("3. Reinstalación de Software") 
            print("4. Recuperación de Datos") 
            print("5. Políticas de Seguridad y/o Backups") 
            descrip_serv = int(input("\nMencione el servicio a atender para su equipo: "))

            monto= 0 #esto para realizar las operaciones de la cantidad y monto de los equipos y servicios
            i=1

            if descrip_serv ==1: #opciones en el menú
                x = 749
                n= int(input("Ingrese la cantidad de equipo que requiera un servicio: "))
                 
                while (i<=n):
                        monto = monto+x #va agregando la cantidad de equipos para un servicio
                        i+=1
                        descrip_equipo = input("Describa las características de su equipo: \n")
                print("Estamos capturando el monto. Espere un momento...")
                time.sleep(2) #tiempo de espera
                print(f"Sería ${monto} pesos.")
            

            elif descrip_serv ==2:
                x =899               
                n= int(input("Ingrese la cantidad de equipo que requiera un servicio: "))
                
                while (i<=n):
                        monto = monto+x
                        i+=1     
                        descrip_equipo = input("Describa las características de su equipo: \n")           
                print("Estamos capturando el monto. Espere un momento...")
                time.sleep(2)
                print(f"Sería ${monto} pesos.")
           
            elif descrip_serv ==3:
                y =499  
                n= int(input("Ingrese la cantidad de equipo que requiera un servicio: "))
                
                while (i<=n):
                        monto = monto+y
                        i+=1    
                        descrip_equipo = input("Describa las características de su equipo: \n") 
                print("Estamos capturando el monto. Espere un momento...")
                time.sleep(2)
                print(f"Sería ${monto} pesos.")

            elif descrip_serv ==4:
                z= 2499
                n= int(input("Ingrese la cantidad de equipo que requiera un servicio: "))
                 
                while (i<=n):
                        monto = monto+z
                        i+=1       
                        descrip_equipo = input("Describa las características de su equipo: \n")
                print("Estamos capturando el monto. Espere un momento...")
                time.sleep(2)
                print(f"Sería ${monto} pesos.") 

            elif descrip_serv ==5:
                a=999 
                n= int(input("Ingrese la cantidad de equipo que requiera un servicio: "))
                 
                while (i<=n):
                        monto = monto+a
                        i+=1        
                        descrip_equipo = input("Describa las características de su equipo: \n")
                print("Estamos capturando el monto. Espere un momento...")
                time.sleep(2)
                print(f"Sería ${monto} pesos.")
           
            iva= 0.16 #para el monto con IVA
            monto_iva= monto * iva
            resultado = monto + monto_iva
            print("El total a pagar sería: $",resultado)
            print("***** F A C T U R A *****")
            nombre_cliente = input("Introduzca su nombre: ")
            fecha_str = input("Introduzca la fecha en la que se registra su servicio (dd/mm/aaaa): ")
            fecha = datetime.datetime.strptime(fecha_str, "%d/%m/%Y").date()
            servicio = Servicio(nombre_cliente, fecha, descrip_equipo, descrip_serv, monto, resultado)
        
            if diccionario_servicio.keys(): #agregamos folio único
             folio = max(diccionario_servicio.keys()) + 1
            else:
             folio = 1
        
            diccionario_servicio[folio] = servicio #agregamos a folio como key del primer diccionario
            print(f'Su número de folio es el siguiente: {folio}')  

            dicc_serv[fecha_str] = servicio #agregamos a fecha como key del segundo diccionario
            break
    
        break        

    if opcion == 2:
        clave_folio = int(input("Proporciona el folio del servicio: ")) #por medio del folio buscamos el servicio
        print("Datos obtenidos según el folio brindado")
        print("x"*110)
        print(f"Nombre: {diccionario_servicio[clave_folio].nombre_cliente}")
        print(f"Fecha: {diccionario_servicio[clave_folio].fecha}")
        print(f"Descripción del equipo: {diccionario_servicio[clave_folio].descrip_equipo}")
        print(f"Guía numérica del servicio: {diccionario_servicio[clave_folio].descrip_serv}")
        print(f"Monto sin IVA: ${diccionario_servicio[clave_folio].monto}")
        print(f"Monto total: ${diccionario_servicio[clave_folio].resultado}")


    if opcion == 3:
        clave_fecha_str = input("Proporciona la fecha en la que se realizó el servicio: ") #por medio de la fecha buscamos el servicio
        clave_fecha = datetime.datetime.strptime(clave_fecha_str, "%d/%m/%Y").date()
        print("Datos obtenidos según la fecha brindada")
        print("-"*130)
        print("Nombre\tFecha\tGuía Numérica del Servicio\tDescripción del Equipo\tMonto sin IVA\tMonto total")
        print("-"*130)
        print(f"{dicc_serv[clave_fecha_str].nombre_cliente}\t{dicc_serv[clave_fecha_str].fecha}\t{dicc_serv[clave_fecha_str].descrip_equipo}\t{dicc_serv[clave_fecha_str].descrip_serv}\t${dicc_serv[clave_fecha_str].monto}\t${dicc_serv[clave_fecha_str].resultado}")

    if opcion==4:
        print("-"*130)  #imprimir todos los registros 
        print("Nombre\tFecha\tGuía Numérica del Servicio\tDescripción del Equipo\tMonto sin IVA\tMonto total")  
        for servicio in diccionario_servicio.values():      
            print(f"{servicio.nombre_cliente}\t{servicio.fecha}\t{servicio.descrip_serv}\t{servicio.descrip_equipo}\t{servicio.monto}\t{servicio.resultado}")


    if opcion ==5:
        break              
