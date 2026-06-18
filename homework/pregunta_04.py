"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contains una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ...
     ('12', 3)]
    """
    conteo_meses = {}
    
    with open("files/input/data.csv", encoding="utf-8") as archivo:
        for linea in archivo:
            columns = linea.strip().split("\t")
            if len(columns) > 2:
                fecha = columns[2]
                mes = fecha.split("-")[1]
                
                if mes in conteo_meses:
                    conteo_meses[mes] += 1
                else:
                    conteo_meses[mes] = 1
                    
    return sorted(conteo_meses.items())