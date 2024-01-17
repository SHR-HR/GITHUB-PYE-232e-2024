# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Дата выполнения Практической-Работы: 17-18 - ЯНВАРЯ 2024 года.
'''
'''
Практическая работа

Курс: Разработка Web-приложений на Python, с применением Фреймворка Django
Дисциплина: Основы программирования на Python
Практическая работа №24: Многопоточное, асинхронное и мультипроцессорное программирование. GIL

Выполните следующие задания:

Задание №1
а) Напишите функцию, которая будет загружать изображение.
б) Запустите циклом 100 таких функций, а также замерьте время.
в) Добавьте функционал мультипроцессорного запуска, с замером времени.

*г) Необходимо провести вычисление факториала в параллельных процессах.
'''
'''
Урок от 17.01.2024
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Выполнение задания:
'''
import time
import multiprocessing
from PIL import Image

def load_image(image_path):
    """Функция для загрузки изображения."""
    with Image.open(image_path) as img:
        # Просто загрузка изображения без выполнения каких-либо операций.
        pass

def process_images_sequential(image_paths):
    """Функция для последовательной обработки изображений."""
    start_time = time.time()

    for path in image_paths:
        load_image(path)

    end_time = time.time()
    print(f"Последовательная обработка: {end_time - start_time} секунд")

def process_images_parallel(image_paths):
    """Функция для параллельной обработки изображений."""
    start_time = time.time()

    # Создаем пул процессов, количество которых равно количеству ядер процессора
    pool = multiprocessing.Pool()
    pool.map(load_image, image_paths)
    pool.close()
    pool.join()

    end_time = time.time()
    print(f"Параллельная обработка: {end_time - start_time} секунд")

def calculate_factorial(n):
    """Функция для вычисления факториала."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def calculate_factorial_parallel(n):
    """Функция для параллельного вычисления факториала."""
    start_time = time.time()

    # Создаем пул процессов, количество которых равно количеству ядер процессора
    pool = multiprocessing.Pool()
    results = pool.map(calculate_factorial, range(1, n + 1))
    pool.close()
    pool.join()

    end_time = time.time()
    print(f"Параллельное вычисление факториала: {end_time - start_time} секунд")
    return results

def show_images(image_paths):
    """Функция для отображения изображений."""
    for path in image_paths:
        img = Image.open(path)
        img.show()

if __name__ == "__main__":
    # Задайте список путей к изображениям
    image_paths = ["E:/PyCharm - IT-Step/CHERNOWICK_+_WORK_IN_CLASS_ROOM/+2024+/1.jpg",
                   "E:/PyCharm - IT-Step/CHERNOWICK_+_WORK_IN_CLASS_ROOM/+2024+/2.jpg"]  # Замените на реальные пути

    # Задание 1б: Запуск циклом 100 функций
    for _ in range(100):
        load_image(image_paths[0])  # Загружаем одно изображение

    # Задание 1в: Параллельная обработка с замером времени
    process_images_parallel(image_paths)

    # Задание 1г: Параллельное вычисление факториала
    n = 5
    result_parallel = calculate_factorial_parallel(n)
    print(f"Результаты параллельного вычисления факториала: {result_parallel}")

    # Отображение изображений
    show_images(image_paths)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг №1. Загрузка изображения
'''
def load_image(image_path):
    """Функция для загрузки изображения."""
    with Image.open(image_path) as img:
        # Просто загрузка изображения без выполнения каких-либо операций.
        pass
'''
Описание: 
Эта функция использует библиотеку PIL (Pillow) для загрузки изображения по указанному пути. 
В данном случае, операции с изображением не выполняются, и функция служит примером базовой операции загрузки.
'''
'''
Шаг №2. Последовательная обработка изображений
'''
def process_images_sequential(image_paths):
    """Функция для последовательной обработки изображений."""
    start_time = time.time()

    for path in image_paths:
        load_image(path)

    end_time = time.time()
    print(f"Последовательная обработка: {end_time - start_time} секунд")
'''
Описание: 
Эта функция выполняет последовательную обработку изображений. 
Она вызывает функцию load_image для каждого пути к изображению в списке image_paths. 
Замеряется время выполнения операции, и результат выводится на экран.
'''
'''
Шаг №3. Параллельная обработка изображений
'''
def process_images_parallel(image_paths):
    """Функция для параллельной обработки изображений."""
    start_time = time.time()

    # Создаем пул процессов, количество которых равно количеству ядер процессора
    pool = multiprocessing.Pool()
    pool.map(load_image, image_paths)
    pool.close()
    pool.join()

    end_time = time.time()
    print(f"Параллельная обработка: {end_time - start_time} секунд")
'''
Описание: 
Эта функция выполняет параллельную обработку изображений, используя модуль multiprocessing. 
Пул процессов создается с количеством процессов, равным количеству ядер процессора. 
Функция load_image применяется к каждому пути к изображению в списке image_paths. 
Замеряется время выполнения операции, и результат выводится на экран.
'''
'''
Шаг №4. Вычисление факториала
'''
def calculate_factorial(n):
    """Функция для вычисления факториала."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
'''
Описание: 
Эта функция принимает целое число n и вычисляет его факториал.
'''
'''
Шаг №5. Параллельное вычисление факториала
'''
def calculate_factorial_parallel(n):
    """Функция для параллельного вычисления факториала."""
    start_time = time.time()

    # Создаем пул процессов, количество которых равно количеству ядер процессора
    pool = multiprocessing.Pool()
    results = pool.map(calculate_factorial, range(1, n + 1))
    pool.close()
    pool.join()

    end_time = time.time()
    print(f"Параллельное вычисление факториала: {end_time - start_time} секунд")
    return results
'''
Описание: 
Эта функция выполняет параллельное вычисление факториала для чисел от 1 до n с использованием пула процессов. 
Замеряется время выполнения операции, и результат выводится на экран.
'''
'''
Шаг №6. Отображение изображений
'''
def show_images(image_paths):
    """Функция для отображения изображений."""
    for path in image_paths:
        img = Image.open(path)
        img.show()
'''
Описание: 
Эта функция использует библиотеку PIL для открытия и отображения изображений, указанных в списке image_paths.
'''
'''
Шаг №7. Основной код (выполняется при запуске файла)
'''
if __name__ == "__main__":
    # Задайте список путей к изображениям
    image_paths = ["E:/PyCharm - IT-Step/CHERNOWICK_+_WORK_IN_CLASS_ROOM/+2024+/1.jpg",
                   "E:/PyCharm - IT-Step/CHERNOWICK_+_WORK_IN_CLASS_ROOM/+2024+/2.jpg"]  # Замените на реальные пути

    # Задание 1б: Запуск циклом 100 функций
    for _ in range(100):
        load_image(image_paths[0])  # Загружаем одно изображение

    # Задание 1в: Параллельная обработка с замером времени
    process_images_parallel(image_paths)

    # Задание 1г: Параллельное вычисление факториала
    n = 5
    result_parallel = calculate_factorial_parallel(n)
    print(f"Результаты параллельного вычисления факториала: {result_parallel}")

    # Отображение изображений
    show_images(image_paths)
'''
Описание: 
В основной части кода задаются пути к изображениям. 
Затем выполняются задания б, в и г. 
Задание б представляет собой цикл, в котором 100 раз загружается одно изображение. 
Задание в - параллельная обработка изображений с замером времени. 
Задание г - параллельное вычисление факториала для числа 5. 
Наконец, вызывается функция для отображения изображений.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #