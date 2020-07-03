import pymysql

db = pymysql.connect(host="localhost",
                            user="root",
                            passwd='Lucas1608#AR',
                            database='biblioteca')

cursor = db.cursor()

def agregar_libro():

    cantidad = int(input('Cuantos libros va a ingresar: '))

    for i in range(cantidad): 

        nombre_ = str(input('Ingrese el nombre del libro: '))
        editorial_ = str(input('Ingrese la editorial del libro: '))
        año_ = str(input('Ingrese el año del libro: '))
        autor_ = str(input('Ingrese el autor del libro: '))

        tupla = []

        tupla.append(nombre_)
        tupla.append(editorial_)
        tupla.append(año_)
        tupla.append(autor_)

        tupla = tuple(tupla)

        sql = "INSERT INTO libros (nombre, editorial, año, autor) VALUES {};".format(tupla)

        cursor.execute(sql)
        db.commit()

def agregar_socio():

    cantidad = int(input('Cuantos socios va a ingresar: '))

    for i in range(cantidad): 

        nombre = str(input("Ingrese el nombre del socio: "))
        #codigo_socio = str(input("Ingrese codigo de socio: "))
        direccion = str(input("Ingrese direccion: "))
        telefonos = str(input("Ingrese numero de teléfono: "))

        tupla = []

        tupla.append(nombre)
        tupla.append(direccion)
        tupla.append(telefonos)

        tupla = tuple(tupla)

        sql = "INSERT INTO socios (nombre, direccion, telefonos) VALUES{};".format(tupla)

        cursor.execute(sql)
        db.commit()

def prestamos():

    fecha_salida = str(input("Ingrese fecha de salida: "))
    codigo_socio = str(input("Ingrese código de socio: "))
    fecha_devolucion = str(input("Ingrese fecha de devolución: "))
    codigo_libro = str(input("Ingrese código de libro: "))
    #codigo_prestamo = str(input("Ingrese código de prestamo: "))

    tupla = []

    tupla.append(fecha_salida)
    tupla.append(codigo_socio)
    tupla.append(fecha_devolucion)
    tupla.append(codigo_libro)

    tupla = tuple(tupla)

    sql = "INSERT INTO prestamos (fecha_salida, codigo_socio, fecha_devolucion, codigo_libro) VALUES{};".format(tupla)

    cursor.execute(sql)
    db.commit()


print("\033[;36m"+"==============================")
print('Para agregar datos a la tabla Libros, ingrese "1"')
print('Para agregar datos a la tabla Prestamo, ingrese "2"')
print('Para agregar datos a la tabla Socios, ingrese "3"')

print("\032¨[;37m"+"")
insert = int(input('Ingresa la opcion: '))

if insert == 1:
    agregar_libro()
elif insert == 3:
    agregar_socio()
elif insert == 2:
    prestamos()
else:
    print('Ese número no corresponde a ninguna opción')

