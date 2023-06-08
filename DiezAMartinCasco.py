import pandas as pd

# Leemos el archivo
df = pd.read_csv('df_covid19_countries.csv (1)/df_covid19_countries.csv')
paises = ['Afghanistan', 'Argentina', 'Mexico', 'Thailand', 'Japan', 'China', 'Macao', 'Canada', 'France', 'Singapore']
# Primera función
def primera(data_frame):
    # Columna de fecha a su formato
    data_frame['date'] = pd.to_datetime(data_frame['date'])

    # Calculamos los casos por mes y país
    calculo = data_frame.groupby([data_frame['location'], data_frame['date'].dt.month])['total_cases'].sum().reset_index()

    # Seleccionamos los países
    df_seleccionado = calculo[calculo['location'].isin(paises)]
    return df_seleccionado

# Función 2
def segunda(df):
    df_ciudades = df[df['location'].isin(paises)]
    #insertamos reset index para almacenar correctamente los datos al final de la suma
    Muertes_mes = df_ciudades.groupby(['location', df_ciudades['date'].dt.month])['total_deaths'].sum().reset_index()
    return Muertes_mes


# Llamada a las funciones
df_primera = primera(df)
df_segunda = segunda(df)

print(df_primera)
print(df_segunda)
