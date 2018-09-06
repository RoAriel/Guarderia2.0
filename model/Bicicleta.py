class Bicicleta(Vehiculo):
    """docstring for Bicicleta."""
    def __init__(self, arg):
        self.rodado = ""

    def set_rodado(self, rodado):
        self.rodado = rodado

    def get_rodado(self):
        return self.rodado
