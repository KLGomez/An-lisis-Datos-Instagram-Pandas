import unittest
import pandas as pd
import data_processing

class TestDataProcessing(unittest.TestCase):
    
    def test_load_data(self):
        # Crear un DataFrame de ejemplo para la prueba
        example_data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
        example_df = pd.DataFrame(example_data)
        
        # Guardar el DataFrame en un archivo CSV para simular carga de datos
        example_df.to_csv('test_data.csv', index=False)
        
        # Cargar los datos del archivo CSV creado
        loaded_data = data_processing.load_data('test_data.csv')
        
        # Verificar que la carga de datos genera un DataFrame válido
        self.assertIsInstance(loaded_data, pd.DataFrame)
        
    def test_clean_data(self):
        # Crear un DataFrame de prueba con valores nulos
        data = pd.DataFrame({'A': [1, None, 3], 'B': [4, 5, None]})
        
        # Limpiar los datos
        cleaned_data = data_processing.clean_data(data)
        
        # Verificar que la limpieza de datos eliminó los valores nulos
        self.assertEqual(cleaned_data.isnull().values.sum(), 0)

if __name__ == '_main_':
    unittest.main()