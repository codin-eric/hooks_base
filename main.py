def suma(x, y):
    """
    Funcion que toma 2 argumentos y devuelve la suma de los mismos
    Args:
        x (int/float): Primer valor a sumar
        y (int/float): Segundo valor a sumar
    return: x+y
    """
    return x + y


def escribir(fpath, data_in):
    """
    Funcion que escribe en un archivo
    Args:
        fpath: path absoluto del archivo
        data_in: información a escribir
    """
    with open(fpath, "w") as file_in:
        file_in.write(data_in)


class calculadora:
    """
    Clase calculadora
    """

    def sumar(x, y):
        """
        Funcion que toma 2 argumentos y devuelve suma
        Args:
            x (int/float): Primer valor a sumar
            y (int/float): Segundo valor a sumar
        return: suma(x,y)
        """
        return suma(x, y)
