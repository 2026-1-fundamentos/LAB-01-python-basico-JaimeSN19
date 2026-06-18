"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabéticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}
    """
    sumas_por_letra = {}
    
    with open("data.csv", "r", encoding="utf-8") as file:
        for line in file:
            columns = line.split("\t")
            if len(columns) > 3:
                valor_col2 = int(columns[1])
                # La columna 4 contiene letras separadas por comas (ej: 'a,b,g')
                letras_col4 = columns[3].split(",")
                
                # Por cada letra encontrada en esa fila, le sumamos el valor de la columna 2
                for letra in letras_col4:
                    sumas_por_letra[letra] = sumas_por_letra.get(letra, 0) + valor_col2
                    
    # Construimos el diccionario final ordenado alfabéticamente por sus claves
    resultado = {letra: sumas_por_letra[letra] for letra in sorted(sumas_por_letra)}
    
    return resultado