import matplotlib.pyplot as plt

def plot_top_accounts(data):
    """Visualiza las cuentas principales con más seguidores en un gráfico de barras horizontal."""
    top_accounts = data.sort_values(by='Followers(millions)[2]', ascending=False).head(10)
    
    fig, ax = plt.subplots(figsize=(12, 8))
    colors = ['skyblue' if row['Country/Continent'] == 'United States' else 'lightcoral' for index, row in top_accounts.iterrows()]
    
    ax.barh(top_accounts['Username'], top_accounts['Followers(millions)[2]'], color=colors)
    
    ax.set_xlabel('Seguidores (millones)')
    ax.set_ylabel('Usuario de Instagram')
    ax.set_title('Top 10 Cuentas de Instagram con Más Seguidores')
    
    for i, v in enumerate(top_accounts['Followers(millions)[2]']):
        ax.text(v + 3, i, f'{v:.1f}M', color='black', va='center')
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.gca().invert_yaxis()  
    plt.show()
    