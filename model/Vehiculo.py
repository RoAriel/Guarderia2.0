class Vehiculo(object):
    """docstring for Vehiculo."""
    def __init__(self, arg):
        self.descripcion = ""

    def set_descripcion(self, descripcion):
        self.descripcion = descripcion

    def get_descripcion(self):
        return self.descripcion
