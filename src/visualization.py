import pandas as pd
import matplotlib.pyplot as plt

def plot_top_accounts(data):
    # Seleccionar las 10 cuentas con más seguidores para la visualización
    top_accounts = data.nlargest(10, 'seguidores')
    
    # Crear un gráfico de barras que muestre la cantidad de seguidores de las cuentas top
    plt.figure(figsize=(12, 6))
    plt.barh(top_accounts['cuenta'], top_accounts['seguidores'], color='skyblue')
    plt.xlabel('Seguidores')
    plt.ylabel('Cuenta de Instagram')
    plt.title('Top 10 Cuentas de Instagram con Más Seguidores')
    plt.gca().invert_yaxis()  # Invertir para que la cuenta con más seguidores esté arriba
    plt.show()
