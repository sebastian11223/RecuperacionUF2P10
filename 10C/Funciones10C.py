import pandas as pd

#leemos los datos
datos = pd.read_csv("test.csv")
df = pd.DataFrame(datos)

#las ids que vamos a usar para extraer los datos
ids = [3, 13, 34, 56, 70, 85, 110, 120, 210, 400]

#En esta parte vamos a leer los idss y vamos a verificar que estén los ids dentro de ids
idsAusar = df.loc[df['id'].isin(ids)]

def VelocidadReloj():
    return idsAusar[['id', 'clock_speed']]


#Mostramos los megapixels de la cámara frontal
def megapixels():
    return idsAusar[['id', 'fc']]

# Funcion para mostrar la capacidad de la batería
def CapacidadBateria():
    return idsAusar[['id', 'battery_power']]

print("Función que muestra, por móvil, la velocidad del microprocesador:")
print(VelocidadReloj())

print("Función que muestra, por móvil, los megapíxeles:")
print(megapixels())

print("Función que muestra, por móvil, la capacidad de la batería:")
print(CapacidadBateria())
