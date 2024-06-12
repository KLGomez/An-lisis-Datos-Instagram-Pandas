import matplotlib.pyplot as plt

def visualize_data(analysis_results):
    # Extraer los datos relevantes para la visualización
    top_accounts = analysis_results.head(10)  # Obtener las 10 cuentas con más seguidores
    usernames = top_accounts['owner']
    followers = top_accounts['followersmillions']

    # Crear el gráfico de barras
    plt.figure(figsize=(12, 6))
    plt.bar(usernames, followers, color='skyblue')
    plt.xlabel('Usuario')
    plt.ylabel('Seguidores (millones)')
    plt.title('Cuentas de Instagram con más seguidores')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Mostrar el gráfico
    plt.show()
