import unittest
from greeter import Greeter

class TestGreeter(unittest.TestCase):
    def test_greet(self):
        # Crear una instancia de Greeter
        greeter = Greeter()
        # El caso de prueba espera "Hello John" pero la salida real será diferente
        self.assertEqual(greeter.greet("John"), "Hello John")

if __name__ == '__main__':
    # Ejecutar las pruebas unitarias
    unittest.main()