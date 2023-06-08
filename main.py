import pandas as pd
import matplotlib.pyplot as plt
from DiezAMartinCasco import primera, segunda

df = pd.read_csv('df_covid19_countries.csv (1)/df_covid19_countries.csv')

# Primera función casos totales por mes por país
PrmeraFuncion = primera(df)

# Segunda función muertes totales por mes por ciudad
SegundaFuncion = segunda(df)

# Gráficas con matplotlib
fig, ax = plt.subplots(2, 1, figsize=(8, 8))

for pais, casos in PrmeraFuncion.groupby('location'):
    ax[0].plot(casos['date'], casos['total_cases'], label=pais)

ax[0].set_xlabel('Mes')
ax[0].set_ylabel('Casos Totales')
ax[0].set_title('Casos Totales por Mes y País')
ax[0].legend()

for ciudad, muertes in SegundaFuncion.groupby('location'):
    ax[1].plot(muertes['date'], muertes['total_deaths'], label=ciudad)

ax[1].set_xlabel('Mes')
ax[1].set_ylabel('Muertes Totales')
ax[1].set_title('Muertes Totales por Mes y Ciudad')
ax[1].legend()

#esto es para poder separar y que queden bien las dos gráficas
plt.tight_layout()
plt.show()
