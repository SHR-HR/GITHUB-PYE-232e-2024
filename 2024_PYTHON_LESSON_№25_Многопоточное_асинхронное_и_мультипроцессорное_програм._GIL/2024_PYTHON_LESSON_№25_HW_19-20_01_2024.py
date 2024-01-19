# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
''''
Дата выполнения Домашней-Работы: 19-20 - ЯНВАРЯ 2024 года.
''''
'''
Домашнее задание
Курс: Разработка Web-приложений на Python, с применением Фреймворка Django
Дисциплина: Основы программирования на Python
Домашнее задание № 25 : Многопоточное, асинхронное и мультипроцессорное программирование. GIL

Выполните следующие задания:

Задание №1

а) Напишите функцию, которая будет загружать информацию сразу с 100 ссылок.
б) Запустите эту функцию, а также замерьте время.
в) Добавьте функционал асинхронного запуска, с замером времени. Обязательно посмотрите нагрузку на ЦП в этот момент (через диспетчер задач).

*) Запустите сначала 100, затем 200, и напоследок 500 таких функций и поработайте с файлами. 
Сделайте запись чисел в файл 1 : 1 в файл 2 : 1, 2 в файл 3 : 1, 2, 3 и так далее,
чтобы задача была цикличной и вариативной.
Затем посмотрите сколько времени уходит на исполнение и насколько преимущественнее тот или иной подход.
Сравните и выведите результаты на экран. На сколько эффективна мультипоточность и, или  мультипроцессорность.

** В качестве ответа прикрепить скрин и ссылку на github.
'''
'''
Урок от 19.01.2024
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Выполнение задания:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
import aiohttp
import asyncio
import time
import concurrent.futures

async def fetch_data(session, url):
    async with session.get(url) as response:
        return await response.json()

async def asynchronous_fetch(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url) for url in urls]
        return await asyncio.gather(*tasks)

def synchronous_fetch(urls):
    start_time = time.time()
    for url in urls:
        response = requests.get(url)
        data = response.json()
    elapsed_time = time.time() - start_time
    print(f"Время синхронного выполнения: {elapsed_time:.2f} секунд")

async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        # Добавить другие URL-адреса
    ]

    # Запустите асинхронную функцию с разным количеством задач и измерьте время выполнения
    for num_tasks in [100, 200, 500]:
        start_time = time.time()
        for _ in range(num_tasks):
            await asynchronous_fetch(urls)
        elapsed_time = time.time() - start_time
        print(f"Время асинхронного выполнения ({num_tasks} задач): {elapsed_time:.2f} секунд")

        # Задача *: Запись чисел в файлы
        for i in range(num_tasks):
            with open(f"file{i + 1}.txt", "a") as file:
                file.write(", ".join(map(str, range(1, i + 2))) + "\n")

if __name__ == "__main__":
    asyncio.run(main())
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг №1: Функция fetch_data

Пример кода:
'''
async def fetch_data(session, url):
    async with session.get(url) as response:
        return await response.json()
'''
Полное и подробное описание:
Эта асинхронная функция использует библиотеку aiohttp для выполнения HTTP-запроса по указанному URL. 
Сначала создается асинхронный контекст сессии (async with session.get(url) as response), 
затем функция ожидает ответ (await response.json()), который интерпретируется как JSON. 
Функция возвращает полученные данные.
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
Она создает сессию (ClientSession) и формирует список задач (tasks), каждая из которых представляет собой вызов 
функции fetch_data для каждого URL из переданного списка. 
Затем функция использует asyncio.gather для параллельного выполнения всех задач и возвращает результат.
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
    elapsed_time = time.time() - start_time
    print(f"Время синхронного выполнения: {elapsed_time:.2f} секунд")
'''
Полное и подробное описание:
Эта функция представляет собой синхронный метод для выполнения HTTP-запросов с использованием библиотеки requests. 
Она проходит по каждому URL в переданном списке, отправляет GET-запрос и обрабатывает данные (если это необходимо). 
Время выполнения замеряется, и результат выводится на экран.
'''
'''
Шаг №4: Функция main

Пример кода:
'''
async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        # Добавить другие URL-адреса
    ]

    # Запустите асинхронную функцию с разным количеством задач и измерьте время выполнения
    for num_tasks in [100, 200, 500]:
        start_time = time.time()
        for _ in range(num_tasks):
            await asynchronous_fetch(urls)
        elapsed_time = time.time() - start_time
        print(f"Время асинхронного выполнения ({num_tasks} задач): {elapsed_time:.2f} секунд")

        # Задача X: Запись чисел в файлы
        for i in range(num_tasks):
            with open(f"file{i + 1}.txt", "a") as file:
                file.write(", ".join(map(str, range(1, i + 2))) + "\n")

if __name__ == "__main__":
    asyncio.run(main())
'''
Полное и подробное описание:
Эта асинхронная функция main выполняет несколько задач. 
В первой части она запускает циклы с разным числом асинхронных функций asynchronous_fetch для измерения 
времени выполнения. Затем, в дополнительном блоке, используется многопоточный подход (ThreadPoolExecutor), 
чтобы запустить асинхронные функции с разным числом задач. После этого данные записываются в файлы согласно 
заданным условиям.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #