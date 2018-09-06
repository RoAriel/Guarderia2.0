import Usuario

class Empleado(Usuario):
    """docstring forEmpleado."""
    def __init__(self, nombre, apellido, dni, fechaNac):
        super(Usuario, self).__init__(self, nombre, apellido, dni, fechaNac)

if __name__ == '__main__':

    emp = Empleado("jose","erme",34343443,"21/3/1993")
    print(emp.get_nombre())
