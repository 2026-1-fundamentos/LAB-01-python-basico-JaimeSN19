"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera columna que aparecen asociadas a dicho valor de la segunda columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     ...
     (9, ['A', 'B', 'C', 'E'])]
    """
    letras_por_valor = {}
    
    with open("files/input/data.csv", encoding="utf-8") as archivo:
        for linea in archivo:
            columns = linea.strip().split("\t")
            if len(columns) > 1:
                letra = columns[0]
                valor = int(columns[1])
                
                # Usamos un conjunto (set) para asegurar valores únicos por clave
                if valor in letras_por_valor:
                    letras_por_valor[valor].add(letra)
                else:
                    letras_por_valor[valor] = {letra}
                    
    resultado = [
        (valor, sorted(list(letras)))
        for valor, letras in sorted(letras_por_valor.items())
    ]
    
    return resultado