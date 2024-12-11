import unittest

def area(a, b): 
    '''Принимает стороны а и b, возвращает произведение прямоугольника со сторонами а и b
       Пример: Вводные знанение: 2 6. Вывод: 12'''
    return a * b 

def perimeter(a, b): 
    '''Принимает стороны а и b, возвращает периметр прямогульника со сторонами а и b
       Пример: Вводные знанение: 2 6. Вывод: 16'''
    return (a + b) * 2 

class RectangleTestCase(unittest.TestCase) :
    def test_square_mul(self):
       res = perimeter(10, 10)
       self.assertEqual(res, 40)