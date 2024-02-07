'''
Дата выполнения Домашней-Работы: 02 - ФЕВРАЛЯ - 03 ФЕВРАЛЯ 2024 года.
'''
'''
Домашняя работа

Курс: Разработка Web-приложений на Python, с применением Фреймворка Django
Дисциплина: Основы программирования на Python

Домашняя работа №29: Программы с интерфейсом (GUI) tkinter и pyqt6

Выполните следующие задания:

Задание №1

а) Сделать набросок дизайна программы в figma / paint для программы, которая делает запрос
на сайт jsonplaceholder с определённым id.
б) Разработать эту программу на библиотеке tkinter.
в) Реализовать сохранение полученного объекта в папку.
'''
'''
Урок от 02.02.2024
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Выполнение задания: а), б) & в)
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
ВАРИАНТ только один (Возможно ОДИН)
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
!!! 
(На первых скриншотах есть наименования в "" (ковычках) на ENG языке - так как писал код в "черновике", оставил как
есть - НО ДЛЯ "ЧИСТОВИКА" - перевел все на - РУССКИЙ ЯЗЫК - для удобства и красоты в интерфейсе.

* черновик - 02.02.2024_ONLY_TEST_CODE+.py
* ЧИСТОВИК - 2024_PYTHON_LESSON_№29_HW_02.02.2024_03.02.2024.py
'''
'''
КОД:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
import tkinter as tk
from tkinter import messagebox
import requests
import json

def fetch_data(user_id):
    try:
        # Замените URL на свой, если требуется
        url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
        response = requests.get(url)
        response.raise_for_status()  # Проверяем наличие ошибок при запросе

        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Ошибка", f"Не удалось получить данные: {e}")
        return None

def save_data(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)
        messagebox.showinfo("Успех", f"Данные, сохраненные в {file_path}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось сохранить данные: {e}")

def on_fetch_button_click():
    user_id = entry_user_id.get()
    if not user_id.isdigit():
        messagebox.showwarning("Предупреждение", "Идентификатор пользователя должен быть числом")
        return

    user_id = int(user_id)
    data = fetch_data(user_id)
    if data:
        save_data(data, "user_data.json")

# Настройка графического интерфейса пользователя
window = tk.Tk()
window.title("Средство извлечения данных JSONPlaceholder")
window.geometry('650x350')

label_user_id = tk.Label(window, text="Введите идентификатор пользователя:")
label_user_id.pack(pady=10)

entry_user_id = tk.Entry(window)
entry_user_id.pack(pady=10)

fetch_button = tk.Button(window, text="Извлечь данные", command=on_fetch_button_click)
fetch_button.pack(pady=10)

window.mainloop()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Данный код представляет собой простое графическое приложение,
написанное с использованием библиотеки tkinter,
которое позволяет пользователю ввести идентификатор пользователя,
после чего отправляет запрос к JSONPlaceholder API для получения данных о пользователе с указанным идентификатором.
Полученные данные сохраняются в файл JSON.
Шаги по коду:
'''
'''
1. Импорт библиотек:
'''
import tkinter as tk
from tkinter import messagebox
import requests
import json
'''
Описание:
tkinter: Библиотека для создания графического интерфейса пользователя (GUI).
messagebox: Подмодуль tkinter для создания диалоговых окон сообщений.
requests: Библиотека для выполнения HTTP-запросов.
json: Библиотека для работы с форматом JSON.
'''
'''
2. Функция fetch_data:
'''
def fetch_data(user_id):
    try:
        url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Ошибка", f"Не удалось получить данные: {e}")
        return None
'''
Описание:
fetch_data: Функция, отправляющая запрос к JSONPlaceholder API для получения данных о пользователе.
Возвращает данные в формате JSON, если запрос успешен, или None, если возникла ошибка.
Если возникла ошибка, выводится диалоговое окно с сообщением об ошибке.
'''
'''
3. Функция save_data:
'''
def save_data(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)
        messagebox.showinfo("Успех", f"Данные, сохраненные в {file_path}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось сохранить данные: {e}")
'''
Описание:
save_data: Функция, сохраняющая данные в файл JSON.
В случае успеха выводится сообщение об успешном сохранении, иначе - сообщение об ошибке.
'''
'''
4. Функция on_fetch_button_click:
'''
def on_fetch_button_click():
    user_id = entry_user_id.get()
    if not user_id.isdigit():
        messagebox.showwarning("Предупреждение", "Идентификатор пользователя должен быть числом")
        return

    user_id = int(user_id)
    data = fetch_data(user_id)
    if data:
        save_data(data, "user_data.json")
'''
Описание:
on_fetch_button_click: Функция, вызываемая при клике на кнопку "Извлечь данные".
Получает идентификатор пользователя из виджета ввода (entry_user_id).
Проверяет, что идентификатор является числом, и выводит предупреждение, если нет.
После получения данных о пользователе вызывает save_data для сохранения в файл "user_data.json".
'''
'''
5. Настройка графического интерфейса пользователя:
'''
window = tk.Tk()
window.title("Средство извлечения данных JSONPlaceholder")
window.geometry('650x350')

label_user_id = tk.Label(window, text="Введите идентификатор пользователя:")
label_user_id.pack(pady=10)

entry_user_id = tk.Entry(window)
entry_user_id.pack(pady=10)

fetch_button = tk.Button(window, text="Извлечь данные", command=on_fetch_button_click)
fetch_button.pack(pady=10)

window.mainloop()
'''
Описание:
Создает основное окно (Tk).
Добавляет виджеты: метку (Label), поле ввода (Entry), кнопку (Button).
Назначает функцию on_fetch_button_click обработчиком события для кнопки.
Запускает главный цикл событий (mainloop), который ожидает действий пользователя.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
