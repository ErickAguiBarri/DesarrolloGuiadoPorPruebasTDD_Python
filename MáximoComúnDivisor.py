# Importamos el módulo unittest que nos permite 
# escribir y ejecutar pruebas unitarias.
import unittest

# Definimos la función mcd(máximo comun divisor), que calcula el máximo 
# común divisor de dos números utilizando el algoritmo de Euclides.
def mcd(a, b):
    while b !=0:
        a, b = b, a % b
    return a

# Definimos la función mcd_CuatroNumeros, que calcula el máximo común divisor 
# de cuatro números usando la función mcd.
def mcd_CuatroNumeros(a, b, c, d):
    return mcd(mcd(mcd(a, b), c), d)

# Definimos una clase TestMCD que hereda de unittest.TestCase, que contendrá 
# nuestras pruebas unitarias.
class TestMCD(unittest.TestCase):
    # Definimos el método test_mcd, que contiene nuestra prueba unitaria.
    def test_mcd(self):
        # Especificamos el valor esperado del máximo común divisor de los cuatro números dados.
        esperado = 3
        # Calculamos el máximo común divisor de los números 6, 9, 15 y 18 utilizando la 
        # función mcd_CuatroNumeros.
        actual = mcd_CuatroNumeros(6, 9, 15, 18)
        # Comparamos el valor esperado con el valor obtenido y verificamos si son iguales.
        self.assertEqual(esperado, actual)

# Ejecutamos las pruebas definidas en la clase TestMCD.
if __name__ == '__main__':
    unittest.main()
