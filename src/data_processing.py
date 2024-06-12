import pandas as pd

# Función para cargar los datos desde un archivo CSV
def load_data(filepath):
    data = pd.read_csv(filepath)
    return data

# Función para limpiar los datos
def clean_data(data):
    # Normalizar nombres de columnas
    data.columns = [col.strip().lower().replace(" ", "_").replace("(", "").replace(")", "").replace("[2]", "").replace("/", "_") for col in data.columns]

    # Imprimir los nombres de las columnas para verificar
    print("Columnas:", data.columns)

    # Eliminar la última fila que contiene metadatos
    data = data[:-1]

    # El nombre correcto de la columna de seguidores
    column_name = 'followersmillions'

    # Imprimir valores únicos de la columna para identificar problemas
    print("Valores únicos antes de la limpieza:", data[column_name].unique())

    # Reemplazar caracteres no deseados y convertir a numérico, manejar errores
    data[column_name] = pd.to_numeric(data[column_name].str.replace(',', ''), errors='coerce')

    # Imprimir valores únicos después de intentar convertir a numérico
    print("Valores únicos después de intentar convertir a numérico:", data[column_name].unique())

    # Eliminar filas con valores no numéricos
    data = data.dropna(subset=[column_name])

    return data

# Bloque principal
if __name__ == "__main__":
    filepath = 'data/raw_data.csv'  # Ruta al archivo CSV
    data = load_data(filepath)  # Cargar datos
    clean_data = clean_data(data)  # Limpiar datos

    # Guardar los datos limpios en un nuevo archivo CSV
    clean_data.to_csv('data/processed_data.csv', index=False)
