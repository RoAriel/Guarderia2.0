class Motocicleta(Vehiculo):
    """docstring for Motocicleta."""
    def __init__(self, arg):
        self.cilindradas = ""

    def set_cilindradas(self, cilindradas):
        self.cilindradas = cilindradas

    def get_cilindradas(self):
        return self.cilindradas
