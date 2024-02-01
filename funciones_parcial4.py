import registro_parcial4
import pickle
import os.path


# Validante para que el numero ingresado sea mayor a otro
def validate(inf, text):
    x = int(input(text))

    while x <= inf:
        x = int(input(f'ERROR (mayores a {inf}), ' + text))

    return x


# Validante para que le numero ingresado este dentro de un rango
def validate_code(inf, sup, text):
    x = int(input(text))

    while x < inf or x > sup:
        x = int(input('ERROR, ' + text))

    return x


#--------------------------------------------------------------------------------


def add_in_order_price(v, reg):

    # Se agrega de manera ordenada, segun su precio, el registro pasado por parametro
    n = len(v)
    pos = n
    izq, der = 0, n - 1

    while izq <= der:
        c = (izq + der) // 2

        if v[c].precio == reg.precio:
            pos = c
            break

        if reg.precio < v[c].precio:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v[pos:pos] = [reg]


def generate_array(v, n):

    # Se van tomando los datos de los registros de forma manual
    for i in range(n):

        print('-' * 37)
        print('Equipo', i+1)

        num = validate(0, 'Ingrese un numero de identificacion: ')
        nom = input('Ingrese el nombre del equipo: ')
        precio = validate(0, 'Ingrese un precio: ')
        tipo = validate_code(0, 39, 'Ingrese el tipo de aparato: ')
        pais = validate_code(0, 19, 'Ingrese ecodigo del pais: ')

        print('-' * 37)
        print()

        # Se crea el registro
        equipo = registro_parcial4.Equipo(num, nom, precio, tipo, pais)

        # Se manda el registro creado al vector paar insertarlo de manera ordenada
        add_in_order_price(v, equipo)

    print('*' * 15)
    print('Vector cargado')
    print('*' * 15)


# Opcion 1
def opcion1(v):

    # Ingresar la cantidad de equipos
    n = validate(0, 'Ingrese la cantidad de equipos: ')
    print()

    # Generador del vector de forma ordenada
    generate_array(v, n)


def show_array_punto2(v, p):
    hay = False

    # Recorre el vector
    for equipo in v:

        # Si cuple la condicion, muestra el registro
        if equipo.precio > p and equipo.pais != 8:
            print(registro_parcial4.to_string_todo(equipo))

            # Si hay algun registro que cumpla con la condicion, se cambia la bandera
            hay = True

    # Si la bandera sigue en falso, ningun registro cumplio con la condicion
    if not hay:
        print('No hay ningun equipo con el precio mayor a', p)


def opcion2(v):

    # Se pide el precio de la condicion para mostrar los equipos
    p = validate(0, 'Ingrese un precio: ')
    print()

    # muestra el los registros que cumplen con la condicion
    print('REGISTROS: ')
    show_array_punto2(v, p)


def search_num(v, num):

    # Analizo el vector y comprao el numero de cada registro con el nuemro dado,
    for i in range(len(v)):
        if v[i].numero == num:
            return i        # retorno la posicion

    return -1       # Si no se encuentra retorno -1


def opcion3(v):

    # Se pide el numero de identificaion para realizar la busqueda del registro
    num = validate(0, 'Ingrese un numero de identidicaion: ')
    print()

    # Realiza una busqueda secuecnial del registro con el mismo numero
    pos = search_num(v, num)

    # Si el registro se encontro, se muestra
    if pos != -1:
        print('Equipo encontrado:')
        print(registro_parcial4.to_string_todo(v[pos]))

    # Si el registro no se encontro, se avisa
    else:
        print('Equipo no encontrado')


def precio_promedio(v):
    num = 0

    for equipo in v:
        num += equipo.precio

    return num/len(v)


def generate_data(v, prom):

    # Se crea/abre el archivo, borrando su contendio
    m = open('parcial4.dat', 'wb')

    # Se recorre el vector y se guardan lso registros que cumplen con el condicional
    for equipo in v:

        if equipo.precio < prom:
            pickle.dump(equipo, m)

    # Se cierra el archivo
    m.close()


def opcion4(v):

    # Se calcula el promedio de precios de todo el vector
    prom = precio_promedio(v)

    # Se genera el archivo
    generate_data(v, prom)

    print('*' * 15)
    print('Archivo cargado')
    print('*' * 15)


def show_data():

    # Se abre el archivo
    m = open('parcial4.dat', 'rb')
    t = os.path.getsize('parcial4.dat')
    cont = 0

    # Se recorre el archivo
    while m.tell() < t:
        a = pickle.load(m)
        print(registro_parcial4.to_string_todo(a))
        cont += 1

    # Se cierra el archivo
    m.close()
    print()
    print('Cantidad de registros que contiene el archivo:', cont)


def opcion5():
    # Mostrar el contenido del archivo
    show_data()
