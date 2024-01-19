# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Дата выполнения Практической-Работы: 19-20 - ЯНВАРЯ 2024 года.
'''
'''
Практическая работа

Курс: Разработка Web-приложений на Python, с применением Фреймворка Django
Дисциплина: Основы программирования на Python
Практическая работа №25: Многопоточное, асинхронное и мультипроцессорное программирование. GIL

Выполните следующие задания:

Задание №1
а) Напишите функцию, которая будет загружать данные с jsonplaceholder.
б) Запустите циклом 100 таких функций, а также замерьте время.
в) Добавьте функционал асинхронной работы, с замером времени.

 - - - КАК ЭТО ПОНЯЛ Я - - - 
*) Запустите сначала 100, затем 200, и напоследок 500 таких функций и поработайте с файлами. 
Сделайте запись чисел в файл 1 : 1 в файл 2 : 1, 2 в файл 3 : 1, 2, 3 и так далее,
чтобы задача была цикличной и вариативной.
Затем посмотрите сколько времени уходит на исполнение и насколько преимущественнее тот или иной подход.
Сравните и выведите результаты на экран. На сколько эффективна мультипоточность и, или  мультипроцессорность.
'''
'''
Урок от 19.01.2024
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Выполнение задания:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
''' Вариант №1 - (учитываются пункты только а), б), в)) '''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
import aiohttp  # Добавлен импорт aiohttp
import asyncio  # Добавлен импорт asyncio
import time  # Добавлен импорт time
import requests  # Добавлен импорт requests

# Асинхронная функция для загрузки данных по URL с использованием aiohttp
async def fetch_data(session, url):
    async with session.get(url) as response:
        return await response.json()

# Асинхронная функция для асинхронного выполнения запросов к нескольким URL
async def asynchronous_fetch(urls):
    # Создание сессии для aiohttp
    async with aiohttp.ClientSession() as session:
        # Создание списка задач (coroutines) для каждого URL
        tasks = [fetch_data(session, url) for url in urls]
        # Ожидание выполнения всех задач и возврат результатов
        return await asyncio.gather(*tasks)

# Синхронная функция для синхронного выполнения запросов к нескольким URL
def synchronous_fetch(urls):
    start_time = time.time()
    for url in urls:
        # Синхронный запрос с использованием requests
        response = requests.get(url)
        data = response.json()
        # Обработка данных, если необходимо
    elapsed_time = time.time() - start_time
    print(f"Время синхронного выполнения: {elapsed_time:.2f} секунд")

# Асинхронная точка входа программы
async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        # Добавьте остальные URL
    ]

    # Запуск задания №1 - б) (синхронный)
    synchronous_fetch(urls)

    # Запуск задания №1 - в) (асинхронный)
    start_time = time.time()
    await asynchronous_fetch(urls)
    elapsed_time = time.time() - start_time
    print(f"Время асинхронного выполнения: {elapsed_time:.2f} секунд")

# Проверка, что скрипт выполняется как программа, а не импортируется как модуль
if __name__ == "__main__":
    # Запуск асинхронной программы с использованием asyncio
    asyncio.run(main())
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Импорт библиотек
'''
import aiohttp
import asyncio
import time
import requests
'''
aiohttp - библиотека для асинхронных HTTP-запросов.
asyncio - библиотека для асинхронного программирования.
time - для замера времени выполнения.
requests - библиотека для синхронных HTTP-запросов.
'''
'''
Асинхронная функция для загрузки данных по URL с использованием aiohttp
'''
async def fetch_data(session, url):
    async with session.get(url) as response:
        return await response.json()
'''
fetch_data - асинхронная функция, которая использует aiohttp для выполнения асинхронного HTTP-запроса.
Возвращает JSON-данные из ответа.
'''
'''
Асинхронная функция для асинхронного выполнения запросов к нескольким URL
'''
async def asynchronous_fetch(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url) for url in urls]
        return await asyncio.gather(*tasks)
'''
asynchronous_fetch - асинхронная функция, которая создает сессию aiohttp и выполняет несколько асинхронных 
HTTP-запросов параллельно.
'''
'''
Синхронная функция для синхронного выполнения запросов к нескольким URL
'''
def synchronous_fetch(urls):
    start_time = time.time()
    for url in urls:
        response = requests.get(url)
        data = response.json()
    elapsed_time = time.time() - start_time
    print(f"Время синхронного выполнения: {elapsed_time:.2f} секунд")
'''
synchronous_fetch - синхронная функция, которая выполняет HTTP-запросы с использованием библиотеки requests.
'''
'''
Асинхронная точка входа программы
'''
async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        # Добавьте остальные URL
    ]

    synchronous_fetch(urls)
    start_time = time.time()
    await asynchronous_fetch(urls)
    elapsed_time = time.time() - start_time
    print(f"Время асинхронного выполнения: {elapsed_time:.2f} секунд")
'''
main - асинхронная точка входа программы. 
Запускает сначала синхронное выполнение, затем асинхронное, и выводит время выполнения обеих операций.
'''
'''
Проверка, что скрипт выполняется как программа
'''
if __name__ == "__main__":
    asyncio.run(main())
'''
Проверяет, что скрипт выполняется как программа, а не импортируется как модуль,
и запускает асинхронную программу с использованием asyncio.run(main()).
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
''' Вариант №2 - (учитываются Все пункты)'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
import requests
import json
import time
import concurrent.futures

def load_data(url):
    response = requests.get(url)
    return json.loads(response.text)

def write_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(', '.join(map(str, data)) + '\n')

def task(task_id):
    url = f'https://jsonplaceholder.typicode.com/todos/{task_id}'
    data = load_data(url)
    write_to_file(f'file{task_id % 3 + 1}.txt', data)

def synchronous_execution():
    start_time = time.time()
    for i in range(1, 101):
        task(i)
    end_time = time.time()
    print(f"Время синхронного выполнения: {end_time - start_time} секунд")

def asynchronous_execution():
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(task, range(1, 101))
    end_time = time.time()
    print(f"Время асинхронного выполнения: {end_time - start_time} секунд")

def main():
    # Синхронное выполнение
    synchronous_execution()

    # Асинхронное выполнение
    asynchronous_execution()

    # Исполнение с разным числом задач
    for num_tasks in [100, 200, 500]:
        start_time = time.time()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(task, range(1, num_tasks + 1))
        end_time = time.time()
        print(f"Асинхронное выполнение с {num_tasks} задачами: {end_time - start_time} секунд")

if __name__ == "__main__":
    main()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Импорт библиотек
'''
import requests
import json
import time
import concurrent.futures
'''
requests: библиотека для выполнения HTTP-запросов.
json: модуль для работы с данными в формате JSON.
time: модуль для работы со временем.
concurrent.futures: стандартная библиотека для работы с параллельным выполнением кода.
'''
'''
Функция load_data
'''
def load_data(url):
    response = requests.get(url)
    return json.loads(response.text)
'''
load_data: 
функция выполняет HTTP GET-запрос по заданному URL, затем использует json.loads для загрузки данных из 
текстового ответа в формате JSON.
'''
'''
Функция write_to_file
'''
def write_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(', '.join(map(str, data)) + '\n')
'''
write_to_file: функция записывает данные в файл. Каждый вызов функции добавляет новую строку в файл.
'''
'''
Функция task
'''
def task(task_id):
    url = f'https://jsonplaceholder.typicode.com/todos/{task_id}'
    data = load_data(url)
    write_to_file(f'file{task_id % 3 + 1}.txt', data)
'''
task: функция, представляющая задачу. 
Она формирует URL с использованием task_id, загружает данные с помощью load_data и записывает их в файл.
'''
'''
Функция synchronous_execution
'''
def synchronous_execution():
    start_time = time.time()
    for i in range(1, 101):
        task(i)
    end_time = time.time()
    print(f"Время синхронного выполнения: {end_time - start_time} секунд")
'''
synchronous_execution: функция для синхронного выполнения 100 задач. Измеряется время начала и конца выполнения.
'''
'''
Функция asynchronous_execution
'''
def asynchronous_execution():
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(task, range(1, 101))
    end_time = time.time()
    print(f"Время асинхронного выполнения: {end_time - start_time} секунд")
'''
asynchronous_execution: функция для асинхронного выполнения 100 задач с использованием пула потоков.
Измеряется время начала и конца выполнения.
'''
'''
Функция main
'''
def main():
    # Синхронное выполнение
    synchronous_execution()

    # Асинхронное выполнение
    asynchronous_execution()

    # Исполнение с разным числом задач
    for num_tasks in [100, 200, 500]:
        start_time = time.time()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(task, range(1, num_tasks + 1))
        end_time = time.time()
        print(f"Асинхронное выполнение с {num_tasks} задачами: {end_time - start_time} секунд")
'''
main: функция, запускающая синхронное и асинхронное выполнение, а также асинхронное выполнение с разным числом задач.
Измеряется время каждого выполнения.
'''
'''
Проверка, что скрипт выполняется как программа
'''
if __name__ == "__main__":
    main()
'''
Проверка, что скрипт выполняется напрямую (а не импортирован как модуль), и запуск функции main().
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
''' Еще '''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
import requests
import json
import time
import concurrent.futures


def load_data(url):
    response = requests.get(url)
    return json.loads(response.text)


def write_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(f'{data}\n')


def task(task_id):
    url = f'https://jsonplaceholder.typicode.com/todos/{task_id}'
    data = load_data(url)

    # Модификация: запись данных в файлы
    write_to_file(f'file{task_id % 3 + 1}.txt', f'{task_id}: {data}')


def synchronous_execution():
    start_time = time.time()
    for i in range(1, 101):
        task(i)
    end_time = time.time()
    print(f"Время синхронного выполнения: {end_time - start_time} секунд")


def asynchronous_execution():
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(task, range(1, 101))
    end_time = time.time()
    print(f"Время асинхронного выполнения: {end_time - start_time} секунд")


def main():
    # Синхронное выполнение
    synchronous_execution()

    # Асинхронное выполнение
    asynchronous_execution()

    # Исполнение с разным числом задач
    for num_tasks in [100, 200, 500]:
        start_time = time.time()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(task, range(1, num_tasks + 1))
        end_time = time.time()
        print(f"Асинхронное выполнение с {num_tasks} задачами: {end_time - start_time} секунд")


if __name__ == "__main__":
    main()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Эти строки отвечают за импорт необходимых библиотек.
'''
import requests
import json
import time
import concurrent.futures
'''
Эта функция load_data принимает URL в качестве аргумента, отправляет GET-запрос по указанному URL с помощью библиотеки
requests, получает ответ и затем использует json.loads для преобразования JSON-строки в Python-объект. 
Возвращает этот объект.
'''
def load_data(url):
    response = requests.get(url)
    return json.loads(response.text)
'''
Функция write_to_file принимает имя файла (filename) и данные (data) и открывает файл в режиме добавления ('a').
Затем она записывает данные в файл, добавляя символ новой строки после каждой записи.
'''
def write_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(f'{data}\n')
'''
Функция task принимает task_id, формирует URL с использованием этого идентификатора, 
загружает данные с помощью функции load_data, а затем записывает эти данные в соответствующий файл с использованием 
функции write_to_file. Файл выбирается с учетом остатка от деления task_id на 3, 
чтобы обеспечить цикличную запись в 3 файла.
'''
def task(task_id):
    url = f'https://jsonplaceholder.typicode.com/todos/{task_id}'
    data = load_data(url)

    # Модификация: запись данных в файлы
    write_to_file(f'file{task_id % 3 + 1}.txt', f'{task_id}: {data}')
'''
Функция synchronous_execution выполняет 100 задач синхронно (последовательно) и замеряет время выполнения.
'''
def synchronous_execution():
    start_time = time.time()
    for i in range(1, 101):
        task(i)
    end_time = time.time()
    print(f"Время синхронного выполнения: {end_time - start_time} секунд")
'''
Функция asynchronous_execution выполняет 100 
задач асинхронно с использованием многозадачности в пуле потоков и замеряет время выполнения.
'''
def asynchronous_execution():
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(task, range(1, 101))
    end_time = time.time()
    print(f"Время асинхронного выполнения: {end_time - start_time} секунд")
'''
В функции main вызываются три варианта выполнения: синхронное, асинхронное с 100 задачами и 
асинхронное с разным числом задач (100, 200, 500). Замеряется время выполнения каждого варианта.
'''
def main():
    # Синхронное выполнение
    synchronous_execution()

    # Асинхронное выполнение
    asynchronous_execution()

    # Исполнение с разным числом задач
    for num_tasks in [100, 200, 500]:
        start_time = time.time()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(task, range(1, num_tasks + 1))
        end_time = time.time()
        print(f"Асинхронное выполнение с {num_tasks} задачами: {end_time - start_time} секунд")

if __name__ == "__main__":
    main()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Можно модифицировать функцию main следующим образом, чтобы выполнять асинхронное выполнение с разным числом задач:
'''
def main():
    # Синхронное выполнение
    synchronous_execution()

    # Асинхронное выполнение с разным числом задач
    for num_tasks in [100, 200, 500, 1000]:
        start_time = time.time()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(task, range(1, num_tasks + 1))
        end_time = time.time()
        print(f"Асинхронное выполнение с {num_tasks} задачами: {end_time - start_time} секунд")

if __name__ == "__main__":
    main()
'''
Тут добавлена задача с 1000 задачами.
Можно добавить или изменить значения в списке [100, 200, 500, 1000], чтобы отражать нужные варианты выполнения.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''Рубрика "ЭКСПЕРЕМЕНТЫ" '''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''

Выполните следующие задания:

Задание №1
а) Напишите функцию, которая будет загружать данные с jsonplaceholder.
б) Запустите циклом сначала 100 таких функций, затем 200 таких функций, 500 таких функций, 1000 таких функций,
2000 таких функций, 5000 таких функций, а также замерьте время.
в) Добавьте функционал асинхронной работы, с замером времени.


Дополнительно:

Запустите сначала 100, затем 200, и напоследок 500, 1000 таких функций и поработайте с файлами.
Затем сделайте запись чисел в файл 1 : 1 в файл 2 : 1, 2 в файл 3 : 1, 2, 3 и так далее,
чтобы задача была цикличной и вариативной.
Затем посмотрите сколько времени уходит на исполнение и насколько преимущественнее тот или иной подход.
Сравните и выведите результаты на экран. На сколько эффективна мультипоточность и, или  мультипроцессорность.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
import aiohttp
import asyncio
import time
import requests
import concurrent.futures

async def fetch_data(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            return await response.json()
        else:
            response.raise_for_status()

async def asynchronous_fetch(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url) for url in urls]
        return await asyncio.gather(*tasks)

def synchronous_fetch(urls):
    start_time = time.time()
    for url in urls:
        response = requests.get(url)
        data = response.json()
        # Обработка данных, если необходимо
    elapsed_time = time.time() - start_time
    print(f"Время синхронного выполнения: {elapsed_time:.2f} секунд")

async def write_to_file(file, data):
    async with aiofiles.open(file, 'a') as f:
        await f.write(data + '\n')

async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        # Добавьте остальные URL
    ]

    # Задание 1б: Запуск циклом 100 функций
    start_time = time.time()
    for _ in range(100):
        await asynchronous_fetch(urls)
    elapsed_time = time.time() - start_time
    print(f"Время асинхронного выполнения (100 функций): {elapsed_time:.2f} секунд")

    # Задание 1б: Запуск циклом 200 функций
    start_time = time.time()
    for _ in range(200):
        await asynchronous_fetch(urls)
    elapsed_time = time.time() - start_time
    print(f"Время асинхронного выполнения (200 функций): {elapsed_time:.2f} секунд")

    # Задание 1б: Запуск циклом 500 функций
    start_time = time.time()
    for _ in range(500):
        await asynchronous_fetch(urls)
    elapsed_time = time.time() - start_time
    print(f"Время асинхронного выполнения (500 функций): {elapsed_time:.2f} секунд")

    # Задание 1б: Запуск циклом 1000 функций
    start_time = time.time()
    for _ in range(1000):
        await asynchronous_fetch(urls)
    elapsed_time = time.time() - start_time
    print(f"Время асинхронного выполнения (1000 функций): {elapsed_time:.2f} секунд")

    # Задание 1б: Запуск циклом 2000 функций
    start_time = time.time()
    for _ in range(2000):
        await asynchronous_fetch(urls)
    elapsed_time = time.time() - start_time
    print(f"Время асинхронного выполнения (2000 функций): {elapsed_time:.2f} секунд")

    # Задание 1б: Запуск циклом 5000 функций
    start_time = time.time()
    for _ in range(5000):
        await asynchronous_fetch(urls)
    elapsed_time = time.time() - start_time
    print(f"Время асинхронного выполнения (5000 функций): {elapsed_time:.2f} секунд")

    # Дополнительно) Запуск сначала 100, затем 200, и на последок 500, 1000 функций
    for num_tasks in [100, 200, 500, 1000]:
        start_time = time.time()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(asynchronous_fetch, [urls] * num_tasks)
        elapsed_time = time.time() - start_time
        print(f"Асинхронное выполнение с {num_tasks} задачами: {elapsed_time:.2f} секунд")

        # Запись чисел в файлы
        for i in range(num_tasks):
            data = ', '.join(map(str, range(1, i + 2)))
            await write_to_file(f"file{i + 1}.txt", data)

if __name__ == "__main__":
    asyncio.run(main())

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг №1: Функция fetch_data

Пример кода:
'''
async def fetch_data(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            return await response.json()
        else:
            response.raise_for_status()
'''
Полное и подробное описание:
Эта функция представляет собой асинхронный метод, который использует библиотеку aiohttp для выполнения 
HTTP-запроса к указанному URL. Она принимает сессию (session) и URL, а затем асинхронно отправляет GET-запрос. 
Если статус ответа равен 200, функция возвращает данные в формате JSON. В противном случае вызывается исключение 
для обработки ошибки.
'''
'''
Шаг №2: Функция asynchronous_fetch

Пример кода:
'''
async def asynchronous_fetch(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url) for url in urls]
        return await asyncio.gather(*tasks)
'''
Полное и подробное описание:
Эта асинхронная функция использует библиотеку aiohttp для асинхронного выполнения нескольких HTTP-запросов.
Она создает сессию (ClientSession), а затем формирует список задач (tasks), каждая из которых представляет собой
вызов функции fetch_data для каждого URL из переданного списка. Затем функция использует asyncio.gather для 
параллельного выполнения всех задач и возвращает результат.
'''
'''
Шаг №3: Функция synchronous_fetch

Пример кода:
'''
def synchronous_fetch(urls):
    start_time = time.time()
    for url in urls:
        response = requests.get(url)
        data = response.json()
        # Обработка данных, если необходимо
    elapsed_time = time.time() - start_time
    print(f"Время синхронного выполнения: {elapsed_time:.2f} секунд")
'''
Полное и подробное описание:
Эта функция представляет собой синхронный метод для выполнения HTTP-запросов с использованием библиотеки requests. 
Она проходит по каждому URL в переданном списке, отправляет GET-запрос и обрабатывает данные (если это необходимо). 
Время выполнения замеряется, и результат выводится на экран.
'''
'''
Шаг №4: Функция write_to_file

Пример кода:
'''
async def write_to_file(file, data):
    async with aiofiles.open(file, 'a') as f:
        await f.write(data + '\n')
'''
Полное и подробное описание:
Эта асинхронная функция использует библиотеку aiofiles для асинхронной записи данных в файл. 
Она принимает имя файла (file) и данные (data). 
С помощью aiofiles.open открывается файл в режиме добавления ('a'), и затем происходит асинхронная запись 
переданных данных с добавлением новой строки.
'''
'''
Шаг №5: Функция main

Пример кода:
'''
async def main():
    # ... (Пропущен код для определения списка URLs)

    # Задание 1б: Запуск циклом 100 функций
    start_time = time.time()
    for _ in range(100):
        await asynchronous_fetch(urls)
    elapsed_time = time.time() - start_time
    print(f"Время асинхронного выполнения (100 функций): {elapsed_time:.2f} секунд")

    # ... (Аналогичные блоки для 200, 500, 1000, 2000, 5000 функций)

    # Дополнительно) Запуск сначала 100, затем 200, и на последок 500, 1000 функций
    for num_tasks in [100, 200, 500, 1000]:
        start_time = time.time()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(asynchronous_fetch, [urls] * num_tasks)
        elapsed_time = time.time() - start_time
        print(f"Асинхронное выполнение с {num_tasks} задачами: {elapsed_time:.2f} секунд")

        # Запись чисел в файлы
        for i in range(num_tasks):
            data = ', '.join(map(str, range(1, i + 2)))
            await write_to_file(f"file{i + 1}.txt", data)

if __name__ == "__main__":
    asyncio.run(main())
'''
Полное и подробное описание:
Эта асинхронная функция main выполняет несколько задач. 
В первой части она запускает циклы с разным числом асинхронных функций asynchronous_fetch для измерения времени 
выполнения. Затем, в дополнительном блоке, используется многопоточный подход (ThreadPoolExecutor), чтобы 
запустить асинхронные функции с разным числом задач. После этого данные записываются в файлы согласно заданным условиям.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #




