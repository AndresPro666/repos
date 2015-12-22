__author__ = 'Code Linkers'
import time
import datetime
from datetime import timedelta
#Numero spot, stock, precio/hora
spotN = ["N",0,2.5]
socio = [100]
esBici = []
salir = False
ex = False
def actStock(spot = list, num = int):
    spot[1] += num
    print("Se actualizo el stock correctamente".center(60," "))

def consultarStock(spot = list):
    msj = "El spot tiene "+str(spot[1])+" bicicletas disponibles"
    print(msj.center(60," "))

def menuAdmin():
    print("\n")
    print(' [ MENU DE ADMINISTRACION ] '.center(60,'*'))
    if spotN[1] <= 3:
        print("ATENCION, NECESITAMOS MAS BICICLETAS".center(60," "))
    print('1- Consultar stock')
    print('2- Actualizar stock')
    print('3- Realizar reporte')
    print('0- Salir')


def menuUsuario():
    print('¿Que desea hacer?: 1 - Alquilar bicicleta')
    print('                   2 - Devolver bicicleta')
    print('                   3 - Consultar saldo de la tarjeta')
    print('                   0 - Salir')

def actSaldo(hora = str):
    global socio
    hs = int(hora[0])
    min = int(hora[2:4])
    seg = int(hora[5:7])
    cargo = 0
    if hs > 0:
        cargo += hs*spotN[2]
    if min > 0:
        cargo += min*(spotN[2]/60)
    if seg > 0:
        cargo += seg*(spotN[2]/3600)
    socio[0] = socio[0] - cargo

def agEstado():
    estado=[]
    estado.append(input('Ingrese el número de bicicleta --> '))
    estado.append(input('Ingrese el modelo de la misma --> '))
    estado.append(input('Ingrese una breve descripcion del estado y/o fallas --> '))
    esBici.append(estado)
    print('El reporte ha sido agregado con éxito!\n')

def programa():
    global user
    global ex
    global time1
    global time2
    global finaltime
    global esBici
    print(''.center(60,'*'))
    print(' HYDRASTATION '.center(60,'='))
    print(''.center(60,'*'))
    user = input("Ingrese numero de usuario/tarjeta: ")
    while True:
        if ex:
            break
        if user.upper() == 'ADMIN':
            pas = input("Ingrese contraseña: ")
            while True:
                if pas == '1234':
                    menuAdmin()
                    while True:
                        opcion = int(input("Ingrese una opcion por favor --> "))
                        if opcion == 1:
                            consultarStock(spotN)
                            break
                        elif opcion == 2:
                            actStock(spotN,int(input("¿Cuantas bicicletas desea agregar? --> ")))
                            break
                        elif opcion == 3:
                            esBici = []
                            opp = 1
                            while True:
                                if opp == 1:
                                    agEstado()
                                    print('Registros agregados: ',esBici)
                                    print("¿Desea seguir agregando reportes de estado?  1 - SI")
                                    print("                                             2 - NO")
                                    opp = int(input("Ingrese una opcion por favor --> "))
                                elif opp == 2:
                                    print("Gracias por utilizar el reporte de estado de HYDRASTATION\n")
                                    break
                            menuAdmin()
                        elif opcion == 0:
                            print(' GOODBYE HYDRASTATION '.center(60,'*'))
                            print("\n")
                            programa()
                        else:
                            print('Opcion incorrecta, por favor ingrese una opcion valida (0 a 3) ')
                else:
                    print('Contraseña incorrecta, por favor ingrese nuevamente ')
                    pas = input("Ingrese contraseña: ")
        else:
            print("\n")
            print(" [ BIENVENIDO A HYDRASTATION ] ".center(60,'*'))
            socio.append(user)
            salirusuario = False
            menuUsuario()
            while True:
                if salirusuario:
                    break
                op = int(input("Ingrese una opcion por favor --> "))
                if op == 1:
                    print("¿Esta seguro que desea comenzar?      1 - SI")
                    print("                                      2 - VOLVER")
                    inicio1 = int(input("Ingrese una opcion por favor --> "))
                    if inicio1 == 1:
                        time1 = datetime.datetime.now()
                        socio.append(time1)
                        spotN[1] = spotN[1] - 1
                        print("Numero de usuario/tarjeta:",user)
                        print("Saldo disponible:",round(socio[0],2))
                        print("Hora de inicio: ",time1.strftime("%H:%M:%S"))
                        break
                    else:
                        if inicio1 == 2:
                            break
                elif op == 2:
                    print("¿Esta seguro que desea devolver la bicicleta?      1 - SI")
                    print("                                                   2 - CONTINUAR VIAJE")
                    inicio2 = int(input("Ingrese una opcion por favor --> "))
                    if inicio2 == 1:
                        time2 = datetime.datetime.now()
                        socio.append(time2)
                        finaltime = time2 - time1
                        socio.append(finaltime)
                        actSaldo(str(finaltime))
                        spotN[1] = spotN[1] + 1
                        print("Numero de usuario/tarjeta:",user)
                        print("Nuevo saldo:",round(socio[0],2))
                        print("Hora de finalizacion: ", time2.strftime("%H:%M:%S"))
                        print("Tiempo total de uso de la bicicleta:",str(finaltime)[0:7])
                        fin = str(finaltime)
                        break
                    else:
                        if inicio2 == 2:
                            print("Ud. decidio continuar utilizando el servicio de HYDRASTATION ")
                            break
                elif op == 3:
                    if socio[0] > 0:
                        print("Numero de usuario/tarjeta:",user)
                        print("Saldo:",round(socio[0],2))
                    else:
                        print("Numero de usuario/tarjeta:",user)
                        print("Saldo: Usted no tiene saldo")
                    menuUsuario()
                elif op == 0:
                    print(" Gracias por utilizar el servicio de HYDRASTATION ".center(60,"*"))
                    print("\n")
                    programa()

programa()
