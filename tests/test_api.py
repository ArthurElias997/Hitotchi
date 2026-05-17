import unittest
import requests

class TestHitochiAPI(unittest.TestCase):
    def test_api_cat_facts_esta_viva(self):
        """Testa se a API de fatos está online e respondendo com sucesso."""
        resposta = requests.get("https://catfact.ninja/fact", timeout=5, verify=False)
        
        # Código 200 significa "Sucesso" na internet
        self.assertEqual(resposta.status_code, 200)
        
        # Garante que a API respondeu um formato que contém o 'fact'
        dados = resposta.json()
        self.assertIn('fact', dados)

if __name__ == '__main__':
    unittest.main()