"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214
    """
    suma = 0
    with open("data.csv", "r", encoding="utf-8") as file:
        for line in file:
            # Dividimos la línea por tabulaciones o comas según sea la estructura de tu data.csv
            # Comúnmente en estos laboratorios los datos están separados por tabuladores ('\t')
            columns = line.split("\t")
            
            # Si el archivo está separado por comas, cambia a: columns = line.split(",")
            if len(columns) > 1:
                suma += int(columns[1])
                
    return suma
