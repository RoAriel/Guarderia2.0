import Usuario

class Cliente(Usuario):
    """docstring forCliente."""
    def __init__(self, nombre, apellido, dni, fechaNac, vehiculo):
        super(Usuario, self).__init__(self, nombre, apellido, dni, fechaNac)
        self.vehiculo = vehiculo

if __name__ == '__main__':

    cli = Cliente("jose","erme",34343443,"21/3/1993")
    print(cli.get_nombre())
