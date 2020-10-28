class Partida:
    def __init__(self, palabra='', intentos=0, tipo_palabra='',
                 nombre_jugador='', palabra_aciertos=[None]):
        self.palabra = palabra
        self.intentos = intentos
        self.tipo_palabra = tipo_palabra
        self.nombre_jugador = nombre_jugador
        self.palabra_aciertos = palabra_aciertos

    @property
    def palabra(self):
        return self._palabra

    @palabra.setter
    def palabra(self, value):
        if not value:
            raise ValueError('La palabra no puede ser vacía.')
        else:
            self._palabra = list(value.upper())

    @property
    def intentos(self):
        return self._intentos

    @intentos.setter
    def intentos(self, value):
        if value < 0:
            raise ValueError('El n° de intentos no puede '
                             'ser un valor negativo.')
        else:
            self._intentos = value

    @property
    def tipo_palabra(self):
        return self._tipo_palabra

    @tipo_palabra.setter
    def tipo_palabra(self, value):
        if not value:
            raise ValueError('El tipo de palabra no puede ser vacío.')
        else:
            self._tipo_palabra = value.upper()

    @property
    def nombre_jugador(self):
        return self._nombre_jugador

    @nombre_jugador.setter
    def nombre_jugador(self, value):
        if not value:
            raise ValueError('El nombre no puede ser vacío.')
        else:
            self._nombre_jugador = value.upper()

    @property
    def palabra_aciertos(self):
        return self._palabra_aciertos

    @palabra_aciertos.setter
    def palabra_aciertos(self, value):
        self._palabra_aciertos = value * len(self._palabra)
