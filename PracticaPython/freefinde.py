#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3
import os, sys

os.system('cls')
def Crear_Base():
    try:
        conn = sqlite3.connect('example.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE Eventos (Nombre text, Direccion text, Fecha text, Hora text, Organizacion text, Provincia text, Localidad text, TipoEvento text)''')
        Carga_Datos_Previos()
    except:
        pass

def Carga_Datos_Previos():

    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    Eventos = [('Taller de Experimentacion Textil','Santa Maria de Oro 421','25/04/2014','14:00','Ce.Cu.Al','Chaco','Resitencia','Taller'),
                    ('Taller de Produccion Musical', 'San Martin 598', '30/04/2014', '18:00', 'Centro Cultural','Chaco','Saenz Peña','Taller'),
                    ('Jueves de Tango','Brown 350','24/04/2014','22:00','Fogon de los Arrieros','Chaco','Resistencia','Musica'),
                    ('2do Concierto de Divulgacion de la Orquesta Sinfonica','Capitán Solari 123','30/04/2014','20:30','Centro Cultural "La Flota"','Chaco','Barranqueras','Musica'),
                    ('INFERIA en Resistencia','Av. de los Inmigrantes 200','26/04/2014','23:00','Myo Rockeria','Chaco','Resistencia','Musica'),
                    ('Jarabe de Palo en Resistencia','Av Wilde 1300','07/05/2014','21:30','Ministerio de Cultura del Chaco','Chaco','Resistencia','Musica'),
                    ('Ciclo "Sonidos en la Mansión"','Av. Alberdi 283','02/05/2014','21:00','Club Social Resistencia','Chaco','Resistencia','Musica'),
                    ('Piazzología el más completo homenaje a Astor','Marcelo T. de Alvear y Mitre','03/05/2014','21:30','Casa de las Culturas','Chaco','Resistencia','Musica'),
                    ('Festival Provincial Doma, Jineteada y Folklore','9 de julio 1024','04/05/2014','13:00','Ministerio de turismo','Chaco','Resistencia','Festival'),
                    ('Presentacion del Disco Noctambulo de Lucas Monzon','Santa María de Oro 471','07/05/2014','21:30','Ce.Cu.Al','Chaco','Resistencia','Musica'),
                    ('Muestra Dispersiva del Taller del Fondo Nacional de las Artes','Marcelo T. de Alvear y Mitre','26/04/2014','20:30','Museo Provincial de Bellas Artes','Chaco','Resistencia','Exposicion'),
                    ('Ciclo Teatro de Cerca','Santa María de Oro 471','26/04/2014','21:30','Ce.Cu.Al','Chaco','Resistencia','Teatro'),
                    ('7mo Festival del  Cine de los pueblos indigenas','Av. Wilde 40','05/05/2014','20:00','CineClub Resistencia','Chaco','Resistencia','Cine'),
                    ('Flisol Chaco','French y Ayacucho','26/04/2014','09:30','UTN	Chaco Resistencia','Chaco','Resistencia','Informatica'),
                    ('4ta Reunion del Foro Audiovisual Chaqueño','1 de Marzo 975','09/05/2014','17:00','CineClub Saenz Peña','Chaco','Saenz Peña','Congreso'),
                    ('Feria del Libro Itinerante','25 de mayo 169','25/04/2014','18:00','Municipalidad de la Verde','Chaco','La Verde','Congreso'),
                    ('Expo Comidas Cotidianas','Ameghino 500','09/05/2014','11:00','Municipalidad de Resistencia','Chaco','Resistencia','Comidas'),
                    ('Terere Music 2014','Costanera','25/04/2014','18:00','Municipalidad de Posasdas','Misiones','Posadas','Musica'),	
                    ('Salud es Movimiento','Balneario el Brete','27/04/2014','18:30','Municipalidad de Posasdas','Misiones','Capital','Exposicion'),	
                    ('Festival Nacional de la Musica del Litoral','Sargento Cabral e/c Beato Roque González y Troazzi','21/10/2014','19:00','Municipalidad de Posadas','Misiones','Capital','Mucica'),	
                    ('Observacion de las Estrellas','Chacra 223','28/04/2014','19:30','Municipalidad de Posadas','Misiones','Capital','Exposicion'),	
                    ('Taller de bijuterie','Moreno 2010','11/05/2014','17:00','Municipalidad de Posadas','Misiones','Capital','Taller'),	
                    ('Mañanas Tacas Tacas en el Jardin Botanico','Sargento Cabral e/c Beato Roque González y Troazzi','26/04/2014','19:00','Municipalidad de Posadas','Misiones','Capital','Taller'),	
                    ('OtroExtremo Misiones','San Martin 650','30/04/2014','16:00','Municipalidad de Posadas','Misiones','Capital','Exposicion'),	
                    ('Taller de reparacion de PCs','Sto cabral 650','30/04/2014','9:00','Municipalidad de Posadas','Misiones','Apostoles','Taller'),	
                    ('Joinea','San juan 1520','5/05/2014','8:00','UNAM','Misiones','Apostoles','Congreso'),	
                    ('Taller de Arte para niños','Sargento Cabral e/c Beato Roque González y Troazzi','10/05/2014','15:00','Municipalidad de Misiones','Misiones','Capital','Taller'),	
                    ('Tango vuelve a Bosetti','Chacra 510','6/05/2014','21:00','Municipalidad de Posadas','Misiones','Capital','Musica'),
                    ('Festival Provincial Doma, Jineteada y Folklore','25 de mayo 1256','1/05/2014','14:00','Ministerio de turismo','Formosa','Laguna Blanca','Festival'),	
                    ('Fiesta Prov. de la Zafra Algodonera, Doma y Folklore','9 de julio 1024','4/05/2014','13:00','Municipalidad de Villa Dos Trece','Formosa','Villa Dos Trece','Festival'),	
                    ('Festival Santo Patrono','av. Napoleon Uriburu','11/05/2014','14:00','Municipalidad de Fortin Lugones','Formosa','Fortín Lugones','Festival'),	
                    ('Fiesta Ntra. Sra. de Fátima','Mendoza 970','13/05/2014','13:00','Municipalidad de la Ciudad de Formosa','Formosa','Capital','Festival'),	
                    ('Festividad San Isidro Labrador','av. Juan Cabral 560','15/05/2014','16:00','Municipalidad de Gral. Belgrano','Formosa','Gral. Belgrano','Musica'),	
                    ('Marisol Otazo presenta su primer CD Marcar la huella','Mendoza 780','14/05/2014','21:30','Marisol Otazo','Formosa','Capital','Musica'),
                    ('Produccion Musical los chicos', 'San Martin 599', '24/04/2014', '18:00', 'Centro Musical','Formosa','Capital','Musica'),
                    ('Marisol Otazo presenta su primer CD Marcar la huella','av. Juan Cabral 560', '05/04/2014', '20:00', 'Centro Musical','Formosa','Laguna Blanca','Musica'),
                    ('ExpoLibro', 'AV Costanera', '01/04/2014', '17:00', 'Galpon C costanera','Formosa','Capital','Exposicion,'),
                    ('Expo MODA-NEA', 'AV Costanera', '02/04/2014', '17:00', 'Galpon C costanera','Formosa','Capital','Exposicion,'),
                    ('Expo FEDEMA', 'AV Costanera', '01/04/2014', '18:00', 'Galpon A costanera','Formosa','Capital','Exposicion,'),
                    ('Expo INDIGENA', 'AV Costanera', '03/04/2014', '17:00', 'Galpon A costanera','Formosa','Capital','Exposicion,'),
                    ('Taller de costura', 'AV Costanera', '10/05/2014', '08:00', 'Galpon C costanera','Formosa','Capital','Taller,'),
                    ('Taller de Porcelana fria', 'AV Costanera', '10/05/2014', '08:00', 'Galpon A costanera','Formosa','Capital','Taller,'),
                    ('Taller Pintura infantil', 'AV Costanera', '08/05/2014', '17:00', 'Galpon C costanera','Formosa','Capital','Taller,'),
                    ('Taller de costura', '', '10/05/2014', '08:00', 'mecenas','Formosa','Capital','Informatica'),
                    ('Curso odontólogos soldarios','Av. Chacabuco 960','25/04/2014','8:30','Marcela Silvero','Corrientes','Capital','Taller'),	
                    ('Cuando yo me vaya','Pelegrin 1509','25/04/2014','22:00','El Calderon','Corrientes','Capital','Música'),	
                    ('Flisol Corrientes','Av. Libertad 5460','26/04/2014','09:30','UNNE','Corrientes','Capital','Congreso'),	
                    ('La vesti en vivo!','Chaco 1236','7/05/2014','23:30','Random bar','Corrientes','Capital','Musica'),
                    ('Fest Car','Sto cabral 1578','19/04/2014','0:00','Julio Cafferata','Corrientes','Esquina','Exposición'),
                    ('The Look of the Year Argentina 2014','Mendoza 970','26/04/2014','0:00','Gobierno de Corrientes','Corrientes','Capital','Festival'),
                    ('Miguel Rincón','San Juan 1230','30/04/2014','9:00','El taller Estudio de Artes Decorativas','Corrientes','Capital','Congreso'),
                    ('Peregrinación a Itati','San Lorenzo 1572','5/09/2014','02:00','Gobierno de Corrientes','Corrientes','Capital','Festival'),
                    ('Noche Cuba libre Inox Elegant 2014','Club de Regatas Corrientes, Parque Mitre','25/04/2014','23:45','Punto de Partida','Corrientes','Capital','Congreso'),
                    ('3ra Edición Expo Todo Mujer Fashion','Entre Ríos 650','9/05/2014','14:00','Hotel Casino de Corrientes','Corrientes','Capital','Exposicion'),
                    ('Noche de las promotoras 2014','Club de Regatas Corrientes, Parque Mitre','30/04/2014','23:45','Movida Nocturna','Corrientes','Capital','Festival'),
                    ('Feriarte	Flotante','La Rioja y Costanera','27/04/2014','17:00','Centro Cultural Siete Corrientes','Corrientes','Corrientes','Exposicion'),
                    ('Vida sin prisa','Costanera Sur','27/04/2014','16:00','Gobierno de Corrientes','Corrientes','Capital','Exposicion'),
                    ('Kiki Troia Pasajero en tránsito','San juan 695','25/04/2014','21:30','Teatro Vera','Corrientes','Capital','Música'),]
    c.executemany('INSERT INTO Eventos VALUES (?,?,?,?,?,?,?,?)', Eventos)
    conn.commit()

def CargarEvento():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    nombre=str(input('Nombre del Evento: '))
    direccion=str(input('Direccion: '))
    fecha=str(input('Fecha del Evento (DD/MM/AAAA): '))
    hora=str(input('Hora del Evento (HH:MM): '))
    organizacion=str(input('Nombre del Organizador: '))
    provincia= str(input('Provincia: '))
    localidad=str(input('Localidad: '))
    tipo=str(input('Tipo de evento:\nMusica \nTaller \nCongreso\nInformatica\nComida\nFestival\nExposicion\n'))
    evento = [(nombre, direccion, fecha, hora, organizacion, provincia, localidad, tipo)]
    print ('Se cargo correctamente el registro: ')
    print(evento)
    c.executemany('INSERT INTO Eventos VALUES (?,?,?,?,?,?,?,?)', evento)
    conn.commit()

def Borrar_Eventos():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    Consulta='SELECT * FROM Eventos WHERE Nombre='

    nombre=input('Ingrese el Nombre del Evento que desea borrar')
    value = ((nombre),)
    Consulta+=nombre
    try:
        cur=c.execute\
        (Consulta)
        for x in cur:
            print(x['Nombre'],'\n',x['Direccion'],'\n',x['Fecha'],'\n',x['Hora'],'\n',x['Organizacion'],'\n',x['Provincia'],' - ',x['Localidad'],'\n',x['TipoEvento'],'\n\n')

        print('El Registro fue Borrado')
        c.execute("DELETE FROM Eventos WHERE Nombre=?", value)
        conn.commit()

    except:
        print('NO existen eventos que coincidan con su busqueda')



def Obtener_Eventos():
##    trae todos los eventos alojados en el almacen de eventos
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.row_factory =sqlite3.Row
    cur=c.execute\
    ("SELECT * FROM Eventos")

    for x in cur:
        print(x['Nombre'],'\n',x['Direccion'],'\n',x['Fecha'],'\n',x['Hora'],'\n',x['Organizacion'],'\n',x['Provincia'],' - ',x['Localidad'],'\n',x['TipoEvento'],'\n\n')

def Obtener_EventosXprovinciaCopado(respuesta, tipo,fecha, idioma):
##    obtiene todos los eventos cuya provincia concuerda con el parametro pasado
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.row_factory =sqlite3.Row
##se hara una conversion para la busqueda
    Consulta='SELECT * FROM Eventos WHERE Provincia='
    if respuesta==1:
        Consulta+='"Chaco" AND TipoEvento='
    elif respuesta==2:
        Consulta+='"Corrientes" AND TipoEvento='
    elif respuesta==3:
        Consulta+='"Formosa" AND TipoEvento='
    elif respuesta==4:
        Consulta+='"Misiones" AND TipoEvento='
    else:
        print("error en la seleccion de provincia")

    if tipo==1:
        Consulta+='"Musica" AND Fecha="'
    elif tipo==2:
        Consulta+='"Taller" AND Fecha="'
    elif tipo==3:
        Consulta+='"Congreso" AND Fecha="'
    elif tipo==4:
        Consulta+='"Informatica" AND Fecha="'
    elif tipo==5:
        Consulta+='"Comida" AND Fecha="'
    elif tipo==6:
        Consulta+='"Festival" AND Fecha="'
    elif tipo==7:
        Consulta+='"Exposicion" AND Fecha="'
    else:
        print("error en la seleccion de tipo")

    Consulta+=fecha+'"'

    cur=c.execute\
    (Consulta)

    i=0
    for x in cur:
        print(x['Nombre'],'\n',x['Direccion'],'\n',x['Fecha'],'\n',x['Hora'],'\n',x['Organizacion'],'\n',x['Provincia'],' - ',x['Localidad'],'\n',x['TipoEvento'],'\n\n')
        i=i+1
    if i == 0:
        if (idioma==2):
            print('NO existen eventos que coincidan con su busqueda')
        else:
            print('there are NO events that match your search')



os.system('cls')
Crear_Base()
contrasena = 123456
print('***********************************')
print('*     Welcome to Finde Free       *')
print('***********************************')
print('Choose Your Language')
idioma = int(input('1-English 2-Spanish: '))
if 1 == idioma:
    Salida=0
    while(Salida!=1):
        Loc = int(input('Choose Province:\n 1-Chaco\n 2-Corrientes\n 3-Formosa\n 4-Misiones\n'))
        print('Event Type : ')
        print('1-Music \n2-Workshop \n3-Congress\n4-Computing\n5-Food\n6-Festival\n7-Exhibition')
        Gustos = int(input())
        fecha= input('Enter the date (DD/MM/YYYY):')
        Obtener_EventosXprovinciaCopado(Loc,Gustos,fecha,Salida)
        Salida=int(input('Log Out: (0-No 1-Yes): '))
if 2 == idioma:
    Salida=0
    while(Salida!=1):
        Loc = int(input('Provincia que le Interesa:\n 1-Chaco\n 2-Corrientes\n 3-Formosa\n 4-Misiones\n'))
        print('Tipo de Evento : ')
        print('1-Musica \n2-Taller \n3-Congreso\n4-Informatica\n5-Comida\n6-Festival\n7-Exposicion')
        Gustos = int(input())
        fecha= input('Ingrese la fecha (DD/MM/AAAA):')
        Obtener_EventosXprovinciaCopado(Loc,Gustos,fecha,Salida)
        Salida=int(input('Desea Salir: (0-No 1-Si): '))
elif (idioma==contrasena):
    os.system('cls')
    opcion=0
    cEvento=0
    print('***********************************')
    print('*       Welcome Administrator     *')
    print('***********************************')
    print('Que desea realizar: ')
    while opcion <=3:
        opcion = int(input('1-Cambiar contraseña \n2-Cargar Nuevo Evento\n3-Borrar Evento\n4-Salir\n  '))
        if opcion==1:
            contrasena = input("Ingrese la nueva contraseña: ")
        elif opcion==2:
            cEvento=0
            while (cEvento!=1):
                CargarEvento()
                cEvento=int(input('Desea Salir: (0-No 1-Si): '))
        elif opcion==3:
            cEvento=0
            while (cEvento!=1):
                Borrar_Eventos()
                cEvento=int(input('Desea Salir: (0-No 1-Si): '))

os.system('cls')

print('\n***********************************')
print('*    Thanks for Use Finde Free    *')
print('***********************************')