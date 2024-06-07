import unittest
import pandas as pd
import analysis

class TestAnalysis(unittest.TestCase):
    
    def test_analyze_data(self):
        # Crear un DataFrame de ejemplo para la prueba
        data = pd.DataFrame({'seguidores': [1000, 500, 2000, 1500, 3000]})
        results = analysis.analyze_data(data)
        
        # Verificar que los resultados generados son los esperados
        self.assertAlmostEqual(results['promedio_seguidores'], 1800, places=2)
        self.assertEqual(results['total_cuentas'], 5)
        
if __name__ == '_main_':
    unittest.main()