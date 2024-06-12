from data_processing import load_data, clean_data
from analysis import analyze_data
from visualization import visualize_data

def main():
    # Cargar los datos
    data = load_data("data/raw_data.csv")

    # Limpiar los datos
    cleaned_data = clean_data(data)

    # Realizar análisis
    analysis_results = analyze_data(cleaned_data, 'followersmillions')

    # Visualizar los resultados
    visualize_data(analysis_results)

if __name__ == "__main__":
    main()

