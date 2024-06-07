import pandas as pd

def analyze_data(data, column_name):
    """
    Realiza el análisis de los datos y devuelve los resultados.
    
    Args:
    - data (DataFrame): DataFrame con los datos a analizar.
    - column_name (str): Nombre de la columna a analizar.

    Returns:
    - analysis_results (dict): Diccionario con los resultados del análisis.
    """
    
    if column_name not in data.columns:
        raise ValueError(f'La columna {column_name} no está presente en el DataFrame.')

    # Calcular métricas de análisis
    avg_followers = data[column_name].mean()
    total_accounts = data.shape[0]
    max_followers = data[column_name].max()
    min_followers = data[column_name].min()

    # Generar un diccionario con los resultados del análisis
    analysis_results = {
        'Promedio de Seguidores': avg_followers,
        'Total de Cuentas': total_accounts,
        'Máximo de Seguidores': max_followers,
        'Mínimo de Seguidores': min_followers
    }
    
    return analysis_results
