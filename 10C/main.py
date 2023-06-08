import pandas as pd
import matplotlib.pyplot as plt
from Funciones10C import VelocidadReloj, megapixels, CapacidadBateria

# Todas las funciones del ejercicio 10 C

print("Función que muestra, por móvil, la velocidad del microprocesador:")
print(VelocidadReloj())

# Función que muestra los megapíxeles
print("Función que muestra, por móvil, los megapíxeles:")
print(megapixels())

# Función que muestra la capacidad de la batería móvil
print("Función que muestra, por móvil, la capacidad de la batería:")
print(CapacidadBateria())

# Gráfica con las funciones realizadas anteriormente
datos = pd.read_csv("test.csv")
df = pd.DataFrame(datos)

# Las IDs que vamos a usar para extraer los datos
ids = [3, 13, 34, 56, 70, 85, 110, 120, 210, 400]

# Extraer los datos correspondientes a las IDs
dfAlt = df.loc[df['id'].isin(ids)]

# Llamar a las funciones y obtener los datos
datos_velocidad = VelocidadReloj()
ids_velocidad = datos_velocidad['id']
velocidad_reloj = datos_velocidad['clock_speed']

datos_megapixeles = megapixels()
ids_megapixeles = datos_megapixeles['id']
megapixeles = datos_megapixeles['fc']

capacidad_bateria = CapacidadBateria()
ids_capacidad_bateria = capacidad_bateria['id']
capacidad_bateria = capacidad_bateria['battery_power']

# Crear gráficos de barras para cada función
fig, axes = plt.subplots(3, 1, figsize=(8, 12))

axes[0].bar(ids_velocidad, velocidad_reloj)
axes[0].set_xlabel('ID')
axes[0].set_ylabel('Velocidad del microprocesador')
axes[0].set_title('Velocidad del microprocesador por ID')
axes[0].legend(['Velocidad'])

axes[1].bar(ids_megapixeles, megapixeles)
axes[1].set_xlabel('ID')
axes[1].set_ylabel('Megapíxeles')
axes[1].set_title('Megapíxeles por ID')
axes[1].legend(['Megapíxeles'])

axes[2].bar(ids_capacidad_bateria, capacidad_bateria)
axes[2].set_xlabel('ID')
axes[2].set_ylabel('Capacidad de la batería')
axes[2].set_title('Capacidad de la batería por ID')
axes[2].legend(['Capacidad de la batería'])

plt.tight_layout()
plt.show()
