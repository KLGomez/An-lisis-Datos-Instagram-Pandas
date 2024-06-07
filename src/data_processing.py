import pandas as pd

def load_data(file_path):
    # Cargar los datos desde el archivo CSV
    data = pd.read_csv(file_path)
    return data

def clean_data(data):
    # Realizar tareas de limpieza de datos
    cleaned_data = data.dropna()  # Eliminar filas con valores nulos
    return cleaned_data