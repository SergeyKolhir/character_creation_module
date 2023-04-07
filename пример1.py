from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')


def calculate_square_root(Number):
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number):
    """Проверка на 0."""
    if your_number <= 0:
        return

    value = calculate_square_root(your_number)

    print('Мы вычислили квадратный корень из введённого '
          f'вами числа. Это будет: {value}')


print(message)
calc(25.5)