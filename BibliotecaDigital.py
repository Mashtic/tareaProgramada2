# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 03/11/2022 0:45 pm
# Última modificación: 05/11/2022 12:10 pm
# Versión: 3.10.8
import random
import nasapy
from datetime import date
from BDVisitantes import *
k="jghymCiVrWmRMuT7KImJRYihHID8JcRRGwf2JnLm"

nasa = nasapy.Nasa(key=k)

def bibliotecaDigital(matrizvisitantes):
    """
    F: Función que tomando ahora el último número de la cédula de cada registro de la matriz principal, 
    llene la lista de tuplas con esa cantidad de información extraída del API. Recorra toda la matriz y llene todos los 
    campos (titulo, fecha, explicación, tipo de archivo y url) respectivamente. 
    E: matrizvisitantes (list)
    S: listatupla(list), contiene los datos por visitante.

    """
    global k
    global nasa
    for fila in matrizvisitantes:
        listatupla=[]
        lista=[]
        ultimo=fila[0]%10
        for i in range (ultimo):
            d = date(random.randint(2000,2022), random.randint(1, 12), random.randint(1,29)).strftime('%Y-%m-%d')
            apod= nasa.picture_of_the_day(date=d, hd=True)
            lista=[apod["title"], apod["date"], apod["explanation"], apod["media_type"], apod["url"]]
            listatupla.append(tuple(lista))
        fila[3]=listatupla
    return matrizvisitantes


matriz=insertarVisitantesES()

print(bibliotecaDigital(matriz))