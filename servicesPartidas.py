from repoPartidas import RepoPartidas
from repoPalabras import RepoPalabras
from partida import Partida
import random


class ServicesPartidas:
    def iniciar_partida(self, nombre, dificultad, palabra='', tipo_palabra=''):
        if dificultad < 1 or dificultad > 10:
            raise ValueError('La dificultad debe ser un valor entre 1-10.')
        if not palabra and not tipo_palabra:
            r_key = random.choice(list(RepoPalabras.palabras_list.keys()))
            palabra = RepoPalabras.palabras_list[r_key]['palabra']
            tipo_palabra = RepoPalabras.palabras_list[r_key]['tipo_palabra']
        intentos = dificultad * len(palabra)
        p1 = Partida(palabra, intentos, tipo_palabra, nombre)
        key = p1._nombre_jugador
        RepoPartidas.partidas_list[key] = p1.__dict__
        return p1

    def get_random_palabra(self):
        r_key = random.choice(list(RepoPalabras.palabras_list.keys()))
        return RepoPalabras.palabras_list[r_key]

    def intentar_letra(self, partida, letra):
        partida._intentos -= 1
        if partida._intentos < 0:
            raise ValueError('Se agotó el n° de intentos.')
        n = len(partida._palabra)
        for i in range(0, n):
            if letra == partida._palabra[i]:
                pos = i
                partida._palabra_aciertos[pos] = letra
        if None in partida._palabra_aciertos:
            if partida._intentos == 0:
                return 'Perdio'
            else:
                return 'Continua'
        else:
            return 'Gano'
