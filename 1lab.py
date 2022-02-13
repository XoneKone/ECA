from random import randint
import time


def create_init_data(method='vectors', n=10) -> (list[int], list[int]) or (list[int]):
    """
    Функция инициализации данных для подсчета количества операций
    :param n: размер векторов, матриц, массива
    :param method: Выбираем, что хотим инициализировать: векторы ('vectors'),
                                                         матрицы ('matrix'),
                                                         неотсортированные массивы('unsorted array')

    :return: Два вектора ИЛИ две матрицы ИЛИ неотсортированный массив
    """
    if method == 'vectors':
        return create_init_vectors(n)
    elif method == 'matrix':
        return create_init_matrix(n)
    elif method == 'unsorted array':
        return create_init_array(n)


def create_init_vectors(n: int) -> (list[int], list[int]):
    a, b = [], []
    for i in range(n):
        a.append(i)
        b.append(i)
    return a, b


def create_init_matrix(n: int) -> (list[list[int]], list[list[int]]):
    matrix_A, matrix_B = [], []

    for i in range(0, n):
        matrix_A.append([j for j in range(1, n + 1)])
        matrix_B.append([j for j in range(1, n + 1)])
    return matrix_A, matrix_B


def create_init_array(n: int) -> list[int]:
    return [randint(-100, 100) for i in range(n)]


def pretty_print(method):
    def wrapped(*args, **kwargs):
        start_time = time.time()
        value, number_of_operations = method(*args, **kwargs)
        exe_time = time.time() - start_time
        print(f"Функция: {method.__name__}")
        print(f'Полученное значение: {value}')
        print(f'Количество операций: {number_of_operations}')
        print(f'Время выполнения: {exe_time}')
        print()

    return wrapped


@pretty_print
def dot(a: list[float], b: list[float]) -> (int, int):
    """
    Скалярное произведение векторов
    :param a: вектор a
    :param b: вектор b
    :return: tuple(скалярное произведение вектора a и b, количество операций)
    """
    number_of_operations = 0
    scalar = 0

    if len(a) > len(b):
        a, b = b, a

    for index in range(len(a)):
        scalar += a[index] * b[index]
        number_of_operations += 3

    return scalar, number_of_operations


@pretty_print
def dot_matrix(a: list[list[int]], b: list[list[int]]) -> (list[list[int]], int):
    """
    Функция перемножения матриц
    :param a: матрица A
    :param b: матрица B
    :return: матрица C=A*B
    """

    number_of_operations = 0
    length = len(a)
    c = [[0 for i in range(length)] for i in range(length)]
    for i in range(length):
        for j in range(length):
            for k in range(length):
                c[i][j] += a[i][k] * b[k][j]
                number_of_operations += 4

    return c, number_of_operations


@pretty_print
def bubble_sort(arr):
    sort_arr = arr.copy()
    number_of_operations = 0

    n = len(arr)
    swapped = True

    x = -1
    while swapped:
        swapped = False
        x += 1
        for i in range(1, n - x):
            if sort_arr[i - 1] > sort_arr[i]:
                sort_arr[i - 1], sort_arr[i] = sort_arr[i], sort_arr[i - 1]
                number_of_operations += 2
                swapped = True
            number_of_operations += 1
    return sort_arr, number_of_operations


@pretty_print
def selection_sort(arr: list[int]):
    sort_arr = arr.copy()
    number_of_operations = 0

    for i in range(len(sort_arr)):
        minimum = i

        for j in range(i + 1, len(sort_arr)):
            # Выбор наименьшего значения
            if sort_arr[j] < sort_arr[minimum]:
                minimum = j
                number_of_operations += 1
            number_of_operations += 1

        # Помещаем это перед отсортированным концом массива
        sort_arr[minimum], sort_arr[i] = sort_arr[i], sort_arr[minimum]
        number_of_operations += 3

    return sort_arr, number_of_operations

@pretty_print
def insertion_sort(arr):
    sort_arr = arr.copy()
    number_of_operations = 0
    for i in range(len(sort_arr)):
        cursor = sort_arr[i]
        pos = i
        number_of_operations += 2
        while pos > 0 and sort_arr[pos - 1] > cursor:
            # Меняем местами число, продвигая по списку
            sort_arr[pos] = sort_arr[pos - 1]
            pos = pos - 1
            number_of_operations += 2
        number_of_operations += 2
        # Остановимся и сделаем последний обмен
        sort_arr[pos] = cursor
        number_of_operations += 1
    return sort_arr, number_of_operations


if __name__ == '__main__':
    a, b = create_init_data('vectors')
    dot(a, b)

    m_a, m_b = create_init_data('matrix', 100)
    dot_matrix(m_a, m_b)

    arr = create_init_data('unsorted array')
    print( f"Изначальный массив: {arr}\n")
    bubble_sort(arr)

    selection_sort(arr)

    insertion_sort(arr)
