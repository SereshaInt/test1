### создать класс, в конструктор которого передаётся одно число.
### в этом классе должен быть метод show, который распечатывает переданное число
print("\n--- создать класс, в конструктор которого передаётся одно число ---")


class MyClass1:
    def __init__(self, num1):
        self.num1 = num1

    def show(self):
        print(self.num1)


n = MyClass1(10)
n.show()

### создать класс, который наследуется от предыдущего класса
### в этот класс передаётся два числа
### данный класс реализует метод calc, который складывает эти два числа
print("\n--- создать класс, который наследуется от предыдущего класса ---")


class MyClass2(MyClass1):
    def __init__(self, num1, num2):
        super().__init__(num1)
        self.num2 = num2

    def calc(self):
        return (self.num1 + self.num2)


n = MyClass2(10, 11)
print(n.calc())
n.show()  # используем метод show из родительского класса

### создать блок try/except/finally
### внутри блока try создать выражение, которое делит на 0
### перехватить эту ошибку и распечатать сообщение пользователю
print("\n--- создать блок try/except/finally ---")

try:
    print(1 / 0)
except ZeroDivisionError:
    print("Ошибка: деление на ноль")
finally:
    print("Окончание обработки")

### создать декоратор, который перед запуском функции распечатывает все аргументы вызываемой функции
print("\n--- создать декоратор, который перед запуском функции распечатывает все аргументы вызываемой функции ---")


def print_args(func):
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)

    return inner


@print_args
def myFn(i, k, n):
    return (i * k + n)


a = myFn(10, 11, 12)
print("результат ф-ции myFn: {}".format(a))

### создать генератор, который возвращает числа от 1 до 10
print("\n--- создать генератор, который возвращает числа от 1 до 10 ---")


def gen1(min_n, max_n, step):
    res = min_n
    while res <= max_n:
        yield res
        res += step
        if res > max_n:
            res = min_n


n = gen1(1, 10, 1)
for i in range(10):
    print(next(n))

### с помощью стандартной функции collections.namedtuple создать объект для хранения точки в трёхмерном пространстве
print("\n--- с помощью стандартной функции collections.namedtuple создать объект для хранения точки в трёхмерном пространстве ---")

from collections import namedtuple

map = namedtuple('Point', ['x', 'y', 'z'])

p1 = map(1, 1, 1)
p2 = map(10, 11, 12)
print("координаты центра между двумя точками: x={}, y={}, z={}".format(
    round(abs(p1.x - p2.x) / 2)
    , round(abs(p1.y - p2.y) / 2)
    , round(abs(p1.z - p2.z) / 2)
))

### создать пакет, в котором будет функция для распечатки текущей даты
print("\n--- создать пакет, в котором будет функция для распечатки текущей даты ---")

import package1 as p1

p1.print_getdate()