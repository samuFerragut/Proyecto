import random


def listaDeCanciones(diccionario):

    assert isinstance(diccionario, dict)

    contador = 0
    lista = []

    while contador < len(diccionario):

        for cancion in diccionario:
            cancion = random.choice(list(diccionario.keys()))
            comillas = '\"'
            cancionComillas = comillas + cancion + comillas

            if cancionComillas not in lista:
                lista.append(cancionComillas)
                contador += 1

    listaToString = ' '.join(lista)
    return listaToString