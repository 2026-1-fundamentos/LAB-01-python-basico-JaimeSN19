"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]
    """
    conteo_meses = {}
    
    with open("data.csv", "r", encoding="utf-8") as file:
        for line in file:
            columns = line.split("\t")
            if len(columns) > 2:
                fecha = columns[2]
                # Extraemos el mes (MM) usando el split por el guion '-' de la fecha
                mes = fecha.split("-")[1]
                
                # Incrementamos el contador para ese mes
                conteo_meses[mes] = conteo_meses.get(mes, 0) + 1
                
    # Convertimos a lista de tuplas y ordenamos cronológicamente (por el string del mes)
    resultado = sorted(conteo_meses.items())
    
    return resultado
