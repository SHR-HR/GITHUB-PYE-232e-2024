# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
''''
Дата выполнения Домашней-Работы: 17-18 - ЯНВАРЯ 2024 года.
''''
'''
Домашнее задание
Курс: Разработка Web-приложений на Python, с применением Фреймворка Django
Дисциплина: Основы программирования на Python
Домашнее задание № 24 : Многопоточное, асинхронное и мультипроцессорное программирование. GIL

Выполните следующие задания:

Задание №1

а) Напишите функцию, которая будет создавать файл и записывать в него рандомное число, с задержкой 1 секунду.
б) Запустите циклом 1000 таких функций, а также замерьте время.
в) Добавьте функционал мультипоточного запуска, с замером времени. 
Обязательно посмотрите нагрузку на ЦП в этот момент (через диспетчер задач).

*г) Необходимо провести вычисление факториала в параллельных процессах.
** В качестве ответа прикрепить скрин и ссылку на github.
'''
'''
Урок от 12.01.2024
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Выполнение задания:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
import time
import random
import threading
import multiprocessing

# Шаг а: Функция для создания файла и записи в него рандомного числа с задержкой
def write_random_number(file_path):
    """Создает файл и записывает в него рандомное число с задержкой 1 секунда."""
    with open(file_path, 'w') as file:
        random_number = random.randint(1, 100)
        file.write(str(random_number))
        time.sleep(1)

# Шаг б: Функция для запуска циклом 1000 функций с замером времени
def run_sequential():
    """Запускает циклом 1000 функций и замеряет время."""
    start_time = time.time()

    for _ in range(1000):
        write_random_number(f"file{_}.txt")

    end_time = time.time()
    print(f"Время, затраченное на последовательное выполнение: {end_time - start_time:.4f} секунд")

# Шаг в: Функция для многопоточного запуска с замером времени
def run_multithreaded():
    """Многопоточный запуск с замером времени."""
    start_time = time.time()

    threads = []
    for _ in range(1000):
        thread = threading.Thread(target=write_random_number, args=(f"file{_}.txt",))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Время, затраченное на многопоточное выполнение: {end_time - start_time:.4f} секунд")

# Шаг г: Функция для параллельного вычисления факториала
def calculate_factorial(n, result_queue):
    """Вычисляет факториал числа n и помещает результат в очередь."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    result_queue.put(result)

# Шаг г (продолжение): Функция для параллельного запуска вычисления факториала
def run_multiprocess_factorial():
    """Параллельное вычисление факториала."""
    start_time = time.time()

    result_queue = multiprocessing.Queue()
    processes = []

    for _ in range(1000):
        process = multiprocessing.Process(target=calculate_factorial, args=(5, result_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    # Получаем результаты из очереди
    factorial_results = [result_queue.get() for _ in range(1000)]

    end_time = time.time()
    print(f"Время, затраченное на параллельное вычисление факториала: {end_time - start_time:.4f} секунд")
    print(f"Результаты факториала: {factorial_results}")

if __name__ == '__main__':
    # Шаг б: Запуск циклом 1000 функций
    run_sequential()

    # Шаг в: Многопоточный запуск
    run_multithreaded()

    # Шаг г: Параллельное вычисление факториала
    run_multiprocess_factorial()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг а: Функция для создания файла и записи в него рандомного числа с задержкой
'''
def write_random_number(file_path):
    """Создает файл и записывает в него рандомное число с задержкой 1 секунда."""
    with open(file_path, 'w') as file:
        random_number = random.randint(1, 100)
        file.write(str(random_number))
        time.sleep(1)
'''
Описание: 
Эта функция создает файл по указанному пути (file_path) и записывает в него случайное число от 1 до 100. 
После этого функция "засыпает" на 1 секунду с помощью time.sleep(1).
'''
'''
Шаг б: Функция для запуска циклом 1000 функций с замером времени
'''
def run_sequential():
    """Запускает циклом 1000 функций и замеряет время."""
    start_time = time.time()

    for _ in range(1000):
        write_random_number(f"file{_}.txt")

    end_time = time.time()
    print(f"Время, затраченное на последовательное выполнение: {end_time - start_time:.4f} секунд")
'''
Описание: 
Эта функция запускает цикл из 1000 итераций. 
На каждой итерации она вызывает функцию write_random_number, создавая 1000 файлов. 
Затем она замеряет время выполнения и выводит результат.
'''
'''
Шаг в: Функция для многопоточного запуска с замером времени
'''
def run_multithreaded():
    """Многопоточный запуск с замером времени."""
    start_time = time.time()

    threads = []
    for _ in range(1000):
        thread = threading.Thread(target=write_random_number, args=(f"file{_}.txt",))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Время, затраченное на многопоточное выполнение: {end_time - start_time:.4f} секунд")
'''
Описание: 
Эта функция также создает 1000 файлов, но использует многопоточность. 
Для каждой итерации цикла создается новый поток (threading.Thread), который выполняет функцию write_random_number. 
Затем происходит ожидание завершения всех потоков (thread.join()), и замеряется время выполнения.
'''
'''
Шаг г: Функция для параллельного вычисления факториала
'''
def calculate_factorial(n, result_queue):
    """Вычисляет факториал числа n и помещает результат в очередь."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    result_queue.put(result)
'''
Описание: 
Эта функция вычисляет факториал числа n и помещает результат в указанную очередь (result_queue).
'''
'''
Шаг г (продолжение): Функция для параллельного запуска вычисления факториала
'''
def run_multiprocess_factorial():
    """Параллельное вычисление факториала."""
    start_time = time.time()

    result_queue = multiprocessing.Queue()
    processes = []

    for _ in range(1000):
        process = multiprocessing.Process(target=calculate_factorial, args=(5, result_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    # Получаем результаты из очереди
    factorial_results = [result_queue.get() for _ in range(1000)]

    end_time = time.time()
    print(f"Время, затраченное на параллельное вычисление факториала: {end_time - start_time:.4f} секунд")
    print(f"Результаты факториала: {factorial_results}")
'''
Описание: 
Эта функция создает 1000 процессов (multiprocessing.Process), каждый из которых вычисляет факториал числа 5. 
Затем происходит ожидание завершения всех процессов, получение результатов из очереди и вывод времени выполнения
и результатов.
'''
'''
На сладкое
'''
if __name__ == '__main__':
    # Шаг 1б: Запуск циклом 1000 функций
    run_sequential()

    # Шаг 1в: Многопоточный запуск
    run_multithreaded()

    # Шаг 1г: Параллельное вычисление факториала
    run_multiprocess_factorial()
'''
Описание: 
Скажем так, основная часть кода запускает три разные функции для сравнения времени выполнения: последовательное
выполнение, многопоточное выполнение и параллельное вычисление факториала.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #