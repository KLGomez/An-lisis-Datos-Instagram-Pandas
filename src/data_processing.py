import pandas as pd

def load_data(file_path):
    """
    Carga los datos desde un archivo CSV.

    Args:
        file_path (str): Ruta del archivo CSV a cargar.

    Returns:
        pandas.DataFrame: DataFrame con los datos cargados.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no se encuentra.")
        return None

def clean_data(data):
    """
    Limpia los datos eliminando filas con valores nulos.

    Args:
        data (pandas.DataFrame): DataFrame a limpiar.

    Returns:
        pandas.DataFrame: DataFrame limpio sin valores nulos.
    """
    cleaned_data = data.dropna()
    return cleaned_data
