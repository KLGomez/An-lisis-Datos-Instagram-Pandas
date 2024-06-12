import matplotlib.pyplot as plt

def visualize_data(analysis_results):
    # Extraer los datos relevantes para la visualización de las cuentas con más seguidores
    top_accounts = analysis_results.head(10)  # Obtener las 10 cuentas con más seguidores
    usernames = top_accounts['owner']
    followers = top_accounts['followersmillions']

    # Crear el gráfico de barras para las cuentas con más seguidores
    plt.figure(figsize=(12, 6))
    plt.bar(usernames, followers, color='skyblue')
    plt.xlabel('Usuario')
    plt.ylabel('Seguidores (millones)')
    plt.title('Cuentas de Instagram con más seguidores')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Mostrar el gráfico de barras
    plt.show()

    # Extraer los datos relevantes para la visualización de los países de los usuarios
    country_counts = analysis_results['country_continent'].value_counts()

    # Crear el gráfico de torta para los países de los usuarios
    plt.figure(figsize=(10, 6))
    plt.pie(country_counts, labels=country_counts.index, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title('Porcentaje de usuarios por país de los 5 mas seguidos')
    plt.show()
