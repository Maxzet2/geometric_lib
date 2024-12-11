import unittest
from rectangle import area as rect_area, perimeter as rect_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter
from circle import area as circle_area, perimeter as circle_perimeter
import math

class RectangleTestCase(unittest.TestCase) :
    def test_perimetr_ordinary(self):
       res = rect_perimeter(12,5)
       self.assertEqual(res,34)

    def test_perimeter_null_a(self):
       res = rect_perimeter(0, 10)
       self.assertEqual(res,0)

    def test_perimeter_null_b(self):
       res = rect_perimeter(12, 0)
       self.assertEqual(res,0)

    def test_perimeter_fractional(self):
       res = rect_perimeter(2.3, 4.78)
       self.assertEqual(res, 14.16)

    def test_perimeter_negative(self):
       res = rect_perimeter(-23, 34)
       self.assertEqual(res, 0)
   
    def test_area_ordinary(self):
       res = rect_area(12,5)
       self.assertEqual(res,60)

    def test_area_null_a(self):
       res = rect_area(0, 10)
       self.assertEqual(res,0)

    def test_area_null_b(self):
       res = rect_area(12, 0)
       self.assertEqual(res,0)
   
    def test_area_fractional(self):
       res = rect_area(3.4, 0.6)
       self.assertEqual(res,2.04)

    def test_area_negative(self):
       res = rect_area(-12, 2)
       self.assertEqual(res, 0)

class SquareTestCase(unittest.TestCase) :
    def test_perimeter_null_a(self):
       res = square_perimeter(5)
       self.assertEqual(res,20)
   
    def test_perimeter_null_a(self):
       res = square_perimeter(0)
       self.assertEqual(res,0)

    def test_perimeter_fractional(self):
       res = square_perimeter(4.789)
       self.assertEqual(res, 19.156)

    def test_perimeter_negative(self):
       res = square_perimeter(-23)
       self.assertEqual(res, 0)

    def test_area_null_a(self):
       res = square_area(0)
       self.assertEqual(res,0)

    def test_area_null_a(self):
       res = square_area(5)
       self.assertEqual(res,25)

    def test_area_negative(self):
       res = square_area(-2)
       self.assertEqual(res, 0)

    def test_area_fractional(self):
       res = square_area(0.6)
       self.assertEqual(res,0.36)


class TriangleTestCase(unittest.TestCase) :
    def test_area_null_a(self):
       res = triangle_area(5, 10)
       self.assertEqual(res,25)

    def test_area_null_a(self):
       res = triangle_area(0, 10)
       self.assertEqual(res,0)

    def test_arae_null_h(self):
       res = triangle_area(12, 0)
       self.assertEqual(res,0)

    def test_area_fractional(self):
       res = triangle_area(2.3, 4.78)
       self.assertEqual(res, 5.497)

    def test_area_negative(self):
       res = triangle_area(-23, 34)
       self.assertEqual(res, 0)

    def test_perimeter_null_a(self):
       res = triangle_perimeter(12, 15, 3)
       self.assertEqual(res,30)

    def test_perimeter_null_a(self):
       res = triangle_perimeter(0, 15, 3)
       self.assertEqual(res,18)

    def test_perimeter_null_b(self):
       res = triangle_perimeter(12, 0, 3)
       self.assertEqual(res,15)

    def test_perimeter_null_c(self):
       res = triangle_perimeter(12, 15, 0)
       self.assertEqual(res,27)

    def test_perimeter_negative(self):
       res = triangle_perimeter(-12, 2 , -41)
       self.assertEqual(res, 0)
       
    def test_perimeter_fractional(self):
       res = triangle_perimeter(3.4, 0.6, 7.6)
       self.assertEqual(res,11.6)

class CircleTestCase(unittest.TestCase) :
    def test_area_null_r(self):
       res = circle_area(0)
       self.assertEqual(res,0.0)

    def test_area_r_ordinary(self):
       res = circle_area(12)
       self.assertEqual(abs(res - math.pi * 12 * 12) < 0.00001, True)

    def test_area_fractional(self):
       res = circle_area(2.7)
       self.assertEqual((res - math.pi * 2.7 * 2.7) < 0.00001,True)

    def test_area_negative(self):
       res = circle_area(-23)
       self.assertEqual(res, 0)

    def test_perimeter_r_ordinary(self):
       res = circle_perimeter(12)
       self.assertEqual((res - 24 * math.pi) < 0.00001, True)

    def test_perimeter_null_r(self):
       res = circle_perimeter(0)
       self.assertEqual(res,0.0)

    def test_perimeter_negative(self):
       res = circle_perimeter(-12)
       self.assertEqual(res, 0)

    def test_perimeter_fractional(self):
       res = circle_perimeter(3.4)
       self.assertEqual((res - 3.4 * math.pi * 2) < 0.00001, True)

if __name__ == '__main__':
    unittest.main()