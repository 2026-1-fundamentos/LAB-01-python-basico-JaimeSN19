"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}
    """
    sumas_por_letra = {}
    
    with open("files/input/data.csv", encoding="utf-8") as archivo:
        for linea in archivo:
            columns = linea.strip().split("\t")
            if len(columns) > 4:
                letra_col1 = columns[0]
                elementos_col5 = columns[4].split(",")
                
                # Sumamos los valores numéricos de la columna 5 para la fila actual
                suma_fila = 0
                for elemento in elementos_col5:
                    if ":" in elemento:
                        suma_fila += int(elemento.split(":")[1])
                
                # Acumulamos en el diccionario según la letra de la columna 1
                if letra_col1 in sumas_por_letra:
                    sumas_por_letra[letra_col1] += suma_fila
                else:
                    sumas_por_letra[letra_col1] = suma_fila
                
    # Retornamos el diccionario ordenado alfabéticamente por sus claves
    return {letra: sumas_por_letra[letra] for letra in sorted(sumas_por_letra)}