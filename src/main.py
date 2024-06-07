import pandas as pd


def main():
    # Cargar los datos desde el archivo raw_data.csv
    raw_data = pd.read_csv('data/raw_data.csv')

    # Mostrar las primeras filas de los datos para verificar la carga correcta
    print(raw_data.head())

if __name__ == "_main_":
    main()
