"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}
    """
    conteo_claves = {}
    
    with open("files/input/data.csv", encoding="utf-8") as archivo:
        for linea in archivo:
            columns = linea.strip().split("\t")
            if len(columns) > 4:
                # Separamos los pares clave:valor de la columna 5 por comas
                elementos = columns[4].split(",")
                
                for elemento in elementos:
                    if ":" in elemento:
                        clave = elemento.split(":")[0]
                        
                        if clave in conteo_claves:
                            conteo_claves[clave] += 1
                        else:
                            conteo_claves[clave] = 1
                            
    # Retornamos el diccionario ordenado alfabéticamente por sus claves
    return {clave: conteo_claves[clave] for clave in sorted(conteo_claves)}