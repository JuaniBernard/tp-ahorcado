from repoPartidas import RepoPartidas
from servicesPartidas import ServicesPartidas


class Ahorcado:
    def menu_ahorcado(self):
        print('\n\tAHORCADO')
        print('\n\t1. Un jugador')
        print('\n\t2. Dos jugadores')
        print('\n\t   Salir (otro número)')
        return int(input('\n\tElija una opción: '))

    def un_jugador(self):
        services = ServicesPartidas()
        _nombre = input('\n----> \tIngrese su nombre: ')
        _dificultad = int(input('\n----> \tIngrese la dificultad (1-10): '))
        p1 = services.iniciar_partida(_nombre, _dificultad)
        res = 'Continua'
        while res == 'Continua':
            letra = input('\n----> \tIngrese una letra: ')
            if letra == 'salir':
                return True
            res = services.intentar_letra(p1, letra.upper())
            print('\t', p1._palabra_aciertos)
        if res == 'Gano':
            print('\n----> \tFelicitaciones {}, adivinaste!\n'
                  .format(_nombre.upper()))
            return True
        elif res == 'Perdio':
            print('\n----> \tPerdiste {}, mejor suerte la próxima.\n'
                  .format(_nombre.upper()))
            return False

    def dos_jugadores(self):
        services = ServicesPartidas()
        for i in range(0, 2):
            _nombre = input('\n----> \tIngrese el nombre del jugador {}: '
                            .format(i+1))
            _dificultad = int(input('\n----> \tIngrese la dificultad para {} '
                                    '(1-10): '.format(_nombre.upper())))
            _palabra = input('\n----> \t¿Qué palabra deberá adivinar '
                             '{}?: '.format(_nombre.upper()))
            _tipo_palabra = input('\n----> \t¿Qué tipo de palabra es?: ')
            p2 = services.iniciar_partida(_nombre, _dificultad, _palabra,
                                          _tipo_palabra)
            res = 'Continua'
            while res == 'Continua':
                letra = input('\n----> \tIngrese una letra: ')
                if letra == 'salir':
                    return True
                res = services.intentar_letra(p2, letra.upper())
                print('\t', p2._palabra_aciertos)
            if res == 'Gano':
                print('\n----> \tFelicitaciones {}, adivinaste!\n'
                      .format(_nombre.upper()))
            elif res == 'Perdio':
                print('\n----> \tPerdiste {}, mejor suerte la próxima.\n'
                      .format(_nombre.upper()))
        print(RepoPartidas.partidas_list, "\n")
        return True


if __name__ == '__main__':
    juego = Ahorcado()
    opcion_menu = juego.menu_ahorcado()
    if opcion_menu == 1:
        print('\n\tModo: Un jugador')
        juego.un_jugador()
    if opcion_menu == 2:
        print('\n\tModo: Dos jugadores')
        juego.dos_jugadores()
    if opcion_menu < 1 or opcion_menu > 2:
        print('\n\tHasta luego!\n')
