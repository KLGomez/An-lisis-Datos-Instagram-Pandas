import pandas as pd

def calculate_mean(data, column_name):
    """Calcula la media de una columna numérica de los datos."""
    return data[column_name].mean()

def calculate_median(data, column_name):
    """Calcula la mediana de una columna numérica de los datos."""
    return data[column_name].median()

def calculate_mode(data, column_name):
    """Calcula la moda de una columna de los datos."""
    return data[column_name].mode()

def top_accounts_by_followers(data, n=5):
    """Devuelve las N cuentas principales por seguidores."""
    return data.sort_values('followersmillions', ascending=False).head(n)

def analyze_data(data, column_name):
    """Realiza análisis de los datos y devuelve resultados."""
    mean = calculate_mean(data, column_name)
    median = calculate_median(data, column_name)
    mode = calculate_mode(data, column_name)
    top_accounts = top_accounts_by_followers(data)  # Esta función ahora devuelve un DataFrame

    # Crear un DataFrame a partir del diccionario
    analysis_results = pd.DataFrame({
        'mean': [mean],
        'median': [median],
        'mode': [mode]
    })

    # Agregar los top_accounts al DataFrame
    top_accounts['username'] = top_accounts.index  # Movemos el índice 'username' a una columna
    analysis_results = pd.concat([analysis_results, top_accounts], axis=1)

    return analysis_results
