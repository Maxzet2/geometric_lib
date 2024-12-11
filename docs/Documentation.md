# Документация проекта Geometric_lib
## Общее описание решения
В проекте представлены 4 файла формата **.py**: [Rectanlge.py](https://github.com/Maxzet2/geometric_lib/blob/74c9d80940515a798d66c1a5df37b69dfabd4e8b/rectangle.py) (прямоугльник),  [Circle.py](https://github.com/Maxzet2/geometric_lib/blob/74c9d80940515a798d66c1a5df37b69dfabd4e8b/circle.py) (окружность),   [Triangle.py](https://github.com/Maxzet2/geometric_lib/blob/74c9d80940515a798d66c1a5df37b69dfabd4e8b/triangle.py) (треугольник),  [Square.py](https://github.com/Maxzet2/geometric_lib/blob/74c9d80940515a798d66c1a5df37b69dfabd4e8b/square.py) (квадрат). Каждый файл содержит в себе **две функции**, которые выполняют указанные формулы той фигуры, которая указана в названии. 
## Подробное описание файлов с функциями 
### Файл [Rectanlge.py](https://github.com/Maxzet2/geometric_lib/blob/74c9d80940515a798d66c1a5df37b69dfabd4e8b/rectangle.py)
Файл [Rectanlge.py](https://github.com/Maxzet2/geometric_lib/blob/74c9d80940515a798d66c1a5df37b69dfabd4e8b/rectangle.py) содержит две функции:
1. Первая функция считает площадь прямоугольника. На вход принимает две переменные a и b (стороны длиной a и b), выводит произведение а и b. 
```python
def  area(a, b):

'''Принимает стороны а и b, возвращает произведение прямоугольника со сторонами а и b'''

return  a  *  b
```
```python
2 5
10
```
2. Вторая функция считает периметр прямоугольника. На вход принимает две переменные a и b (стороны длиной a и b), выводит удвоенную сумму а и b. 
```python
def  perimeter(a, b):

'''Принимает стороны а и b, возвращает периметр прямогульника со сторонами а и b'''

return (a  +  b) *  2
```
```python
2 5
14
```
### Файл [Circle.py](https://github.com/Maxzet2/geometric_lib/blob/74c9d80940515a798d66c1a5df37b69dfabd4e8b/circle.py) 
Файл [Circle.py](https://github.com/Maxzet2/geometric_lib/blob/74c9d80940515a798d66c1a5df37b69dfabd4e8b/circle.py) содержит две функции:
1. Первая функция считает площадь круга. На вход принимает одну переменную r (радиус r), выводит произведение $r^2$ и п числа. 
```python
def  area(r):

'''Принимает радиус r, возвращает площадь круга с радиусом r'''

return  math.pi  *  r  *  r
```
```python
3
28.274333882308138
```
2. Вторая функция считает периметр окружности. На вход принимает одну переменные r (радиус r), выводит произведение числа $\pi$, r и 2. 
```python
def  perimeter(r):

'''Принимает радиус r, возвращает периметр круга с радиусом r'''

return  2  *  math.pi  *  r
```
```python
3
```
Также в этом файле используется библиотека math для использования числа $\pi$
### Файл [Triangle.py](https://github.com/Maxzet2/geometric_lib/blob/74c9d80940515a798d66c1a5df37b69dfabd4e8b/triangle.py)
Файл [Triangle.py](https://github.com/Maxzet2/geometric_lib/blob/74c9d80940515a798d66c1a5df37b69dfabd4e8b/triangle.py) содержит две функции:
1. Первая функция считает площадь треугольника. На вход принимает две переменные a и h (сторона длиной a и высота длиной h), выводит полупроизведение а и h. 
```python
def  area(a, h):

'''Принимает основание a и высоту h, возвращает площадь треугольника с основанием a и высотой h'''

return  a  *  h  /  2
```
```python
2 5
5
```
2. Вторая функция считает периметр треугольника. На вход принимает три переменные a, b и c (стороны длиной a, b и c), выводит сумму а, b и c. 
```python
def  perimeter(a, b, c):

'''Принимает стороны a b c, возвращает периметр треугольника с сторонами a b c'''

return  a  +  b  +  c
```
```python
3 4 5
12
```
### Файл [Square.py](https://github.com/Maxzet2/geometric_lib/blob/74c9d80940515a798d66c1a5df37b69dfabd4e8b/square.py)
Файл [Square.py](https://github.com/Maxzet2/geometric_lib/blob/74c9d80940515a798d66c1a5df37b69dfabd4e8b/square.py) содержит две функции:
1. Первая функция считает площадь прямоугольника. На вход принимает одна переменная a (сторона длиной a), выводит $a^2$. 
```python
def  area(a):

'''Принимает число а, а возрващает площадь квадрата со сторонами а'''

return  a  *  a
```
```python
5
25
```
2. Вторая функция считает периметр прямоугольника. На вход принимает одна переменная a (сторона длиной a), выводит произведение а и 4. 
```python
def  perimeter(a):

'''Принимает число а, а возрващает периметр квадратсо стороной а'''

return  4  *  a
```
```python
5
20
```
## Блок тестирования
Для проверки работоспособности нашего проекта я написал тест для этого проекта лежащий в папке test, называемый [test_geometric](/test/test_geometric.py). Результаты тестирования:
|Вызываемая функция|Входные данные|Описание ситуации              |Ожидаемый результат|Фактический результат|Дата      |Вердикт|
|------------------|-------------:|:-----------------------------:|------------------:|:-------------------:|:--------:|:-----:|
|Rectangle.perimetr|(12,5)        |Стороны целые и положительные  |34                 |34                   |2024.11.26|   OK  |
|Rectangle.perimetr|(0,10)        |Первая сторона равна нулю      |0                  |0                    |2024.11.26|   OK  |
|Rectangle.perimetr|(12,0)        |Вторая сторона равна нулю      |0                  |0                    |2024.11.26|   OK  |
|Rectangle.perimetr|(2.3,4.78)    |Стороны являются дробями       |14.16              |14.16                |2024.11.26|   OK  |
|Rectangle.perimetr|(-23,34)      |Стороны являются отрицательными|0                  |22                   |2024.11.26|  FAIL |
|Rectangle.area    |(0,10)        |Первая сторона равна нулю      |0                  |0                    |2024.11.26|   OK  |
|Rectangle.area    |(0,10)        |Первая сторона равна нулю      |0                  |0                    |2024.11.26|   OK  |
|Rectangle.area    |(12,0)        |Вторая сторона равен нулю      |0                  |0                    |2024.11.26|   OK  |
|Rectangle.area    |(3.4,0.6)     |Стороны являются дробями       |2.04               |2.04                 |2024.11.26|   OK  |
|Rectangle.area    |(-12,2)       |Стороны являются отрицательными|0                  |-24                  |2024.11.26|  FAIL |
|Square.perimetr   |(5)           |Сторона равна нулю             |20                 |20                   |2024.11.26|   OK  |
|Square.perimetr   |(0)           |Сторона равна нулю             |0                  |0                    |2024.11.26|   OK  |
|Square.perimetr   |(4.789)       |Второй элемент равен нулю      |19.156             |19.156               |2024.11.26|   OK  |
|Square.perimetr   |(-23)         |Стороны являются отрицательными|0                  |-92                  |2024.11.26|  FAIL |
|Square.area       |(5)           |Сторона равна нулю             |25                 |25                   |2024.11.26|   OK  |
|Square.area       |(0)           |Сторона равна нулю             |0                  |0                    |2024.11.26|   OK  |
|Square.area       |(0.6)         |Первый элемент равна нулю      |0.36               |0.36                 |2024.11.26|   OK  |
|Square.area       |(-2)          |Второй элемент равна нулю      |0                  |4                    |2024.11.26|  FAIL |
|Triangle.perimetr |(12,15,3)     |Стороны положительны и целые   |30                 |30                   |2024.11.26|   OK  |
|Triangle.perimetr |(0,15,3)      |Первая сторона равна нулю      |0                  |0                    |2024.11.26|   OK  |
|Triangle.perimetr |(0,15,3)      |Первая сторона равна нулю      |0                  |0                    |2024.11.26|   OK  |
|Triangle.perimetr |(12,0,3)      |Вторая сторона равна нулю      |0                  |0                    |2024.11.26|   OK  |
|Triangle.perimetr |(12,15,0)     |Третья сторона равна нулю      |14.16              |14.16                |2024.11.26|   OK  |
|Triangle.perimetr |(-12,2,-41)   |Стороны являются отрицательными|0                  |-51                  |2024.11.26|  FAIL |
|Triangle.perimetr |(3.4,0.6,7.6) |Стороны являются дробями       |11.6               |11.6                 |2024.11.26|   OK  |
|Triangle.area     |(5,10)        |СТороны целые и положительные  |25                 |25                   |2024.11.26|   OK  |
|Triangle.area     |(0,10)        |Сторона равен нулю             |0                  |0                    |2024.11.26|   OK  |
|Triangle.area     |(12,0)        |Высота равна нулю              |2.04               |2.04                 |2024.11.26|   OK  |
|Triangle.area     |(2.3,4.78)    |Стороны являются дробями       |5.497              |5.497                |2024.11.26|   OK  |
|Triangle.area     |(-24,34)      |Стороны являются отрицательными|0                  |-391                 |2024.11.26|  FAIL |
|Circle.perimetr   |(0)           |Радиус равен нулю              |0                  |0                    |2024.11.26|   OK  |
|Circle.perimetr   |(12)          |Радиус обычное число           |75.3982~           |75.3982~             |2024.11.26|   OK  |
|Circle.perimetr   |(3.4)         |Стороны являются дробями       |21,36283~          |21,36283~            |2024.11.26|   OK  |
|Circle.perimetr   |(-23)         |Стороны являются отрицательными|0                  |-75.3982~            |2024.11.26|  FAIL |
|Circle.area       |(0)           |Первая сторона равна нулю      |0                  |0                    |2024.11.26|   OK  |
|Circle.area       |(12)          |Вторая сторона равен нулю      |452.38934          |452.38934~           |2024.11.26|   OK  |
|Circle.area       |(3.4)         |Стороны являются дробями       |22.90221~          |22.90221~            |2024.11.26|   OK  |
|Circle.area       |(-12)         |Стороны являются отрицательными|0                  |452.38934~           |2024.11.26|  FAIL |

Что должны покрывать тесты: 
1. Входные данные целые положительные числа.
2. Входные данные дробные положительные числа.
3. Входные данные отрицательные случаи.
4. Частично или полностью входные данные - это нули.

В 1 и 2 случае должно работать корректно и выдавать положительный результат (пример указан в комментарии функций).
3 случай обрабатываться не может (отрицательные стороны у фигур быть не могут) поэтому говорим что ответ должен быть равным 0.
4 случай в реузльтате должен быть 0.

Пример позитивного теста:
``` python
def test_perimeter_fractional(self):
       res = square_perimeter(4.789)
       self.assertEqual(res, 19.156)
```
Пример негативного тестирования
``` python
def test_perimeter_negative(self):
       res = square_perimeter(-23)
       self.assertEqual(res, 0)
```

Пример запуска теста: 
```plaintext
maxim@192 geometric_lib % python3 -m unittest test.test_geometric.SquareTestCase
.F..F.
======================================================================
FAIL: test_area_negative (test_geometric.SquareTestCase.test_area_negative)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/opt/homebrew/geometric_lib/test_geometric.py", line 60, in test_area_negative
    self.assertEqual(res, 0)
    ~~~~~~~~~~~~~~~~^^^^^^^^
AssertionError: 4 != 0

======================================================================
FAIL: test_perimeter_negative (test_geometric.SquareTestCase.test_perimeter_negative)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/opt/homebrew/geometric_lib/test_geometric.py", line 52, in test_perimeter_negative
    self.assertEqual(res, 0)
    ~~~~~~~~~~~~~~~~^^^^^^^^
AssertionError: -92 != 0

----------------------------------------------------------------------
Ran 6 tests in 0.001s

FAILED (failures=2)
```
## История изменения проекта
Коммиты: 
1. Коммит [9392d3d](6880d8070d0f7fa3ff144ea45393e88d66aa3446): в этом коммите добавлен файл [Rectanlge.py](https://github.com/Maxzet2/geometric_lib/blob/74c9d80940515a798d66c1a5df37b69dfabd4e8b/rectangle.py).
2. Коммит [7eb345e](https://github.com/KulEDmitr/geometric_lib/commit/28c1ea176467227b617e8176e0f0e4377e42ba71): в этом коммите были добавлины файлы [Triangle.py](https://github.com/Maxzet2/geometric_lib/blob/74c9d80940515a798d66c1a5df37b69dfabd4e8b/triangle.py) и изменен файл [Rectanlge.py](https://github.com/Maxzet2/geometric_lib/blob/74c9d80940515a798d66c1a5df37b69dfabd4e8b/rectangle.py).
3. Коммит [74c9d80](https://github.com/Maxzet2/geometric_lib/commit/74c9d80940515a798d66c1a5df37b69dfabd4e8b): в этом коммите добавлена документация.
4. Коммит [735563b](https://github.com/Maxzet2/geometric_lib/commit/735563bc89baab7a801194a7c48c3772260a7f73): в этом коммите были добавлены тесты и результаты тество в документацию.
5. Коммит [546c76f](https://github.com/Maxzet2/geometric_lib/commit/546c76f8773f3bcc4922d97b18b7971cb6e34543): в этом коммите был добавлен workflow.