import pandas as pd
from data_processing import load_data
from analysis import analyze_data
from visualization import plot_top_accounts

# Cargar los datos desde el archivo raw_data.csv
data = load_data('data/raw_data.csv')

# Realizar el análisis de datos
analysis_results = analyze_data(data)

# Visualizar las cuentas principales con más seguidores
plot_top_accounts(data)