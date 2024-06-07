import unittest
import unittest
import pandas as pd
from data_processing import load_data, clean_data

class TestDataProcessing(unittest.TestCase):
    
    def setUp(self):
        # Definir un DataFrame de prueba para utilizar en las pruebas
        data = {
            'A': [1, 2, 3, None, 5],
            'B': ['apple', 'orange', 'banana', 'pear', None]
        }
        self.df = pd.DataFrame(data)
    
    def test_load_data(self):
        # Probar si load_data carga correctamente un archivo CSV
        file_path = 'data/raw_data.csv'
        df_loaded = load_data(file_path)
        
        # Verificar que el DataFrame cargado tenga el mismo número de columnas que el DataFrame de prueba
        self.assertEqual(df_loaded.shape[1], self.df.shape[1])
    
    def test_clean_data(self):
        # Probar si clean_data elimina los valores nulos correctamente
        cleaned_df = clean_data(self.df)
        
        # Verificar que no haya valores nulos en el DataFrame limpio
        self.assertTrue(cleaned_df.isnull().sum().sum() == 0)

if __name__ == '_main_':
    unittest.main()
