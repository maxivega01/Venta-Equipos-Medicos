
# Creacion de registro
class Equipo:

    def __init__(self, num, nom, precio, tipo, pais):

        self.numero = num
        self.nombre = nom
        self.precio = precio
        self.tipo = tipo
        self.pais = pais


# Imprimir todos los datos del registro
def to_string_todo(alquiler):

    r = ''
    r += '{:<30}'.format(' | Numero de identificaion: ' + str(alquiler.numero))
    r += '{:<15}'.format(' | Nombre: ' + alquiler.nombre)
    r += '{:<15}'.format(' | Precio: ' + str(alquiler.precio))
    r += '{:<25}'.format(' | Tipo de aparato: ' + str(alquiler.tipo))
    r += '{:<25}'.format(' | Codigo de pais: ' + str(alquiler.pais))

    return r
