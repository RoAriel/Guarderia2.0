class Usuario(object):
    """Este va ser la clase usuario de la cual se va a desprender dos tipos de  usr distintos."""
    def __init__(self, nombre, apellido, dni, fechaNac ):
         self.nombre =  nombre
         self.apellido = apellido
         self.dni = dni
         self.fechaNac = fechaNac

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

if __name__ == '__main__':

    usr = Usuario("jose","erme",34343443,"21/3/1993")
    print(usr.get_nombre())
