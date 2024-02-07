'''
Дата выполнения Домашней-Работы: 07 - ФЕВРАЛЯ - 08 ФЕВРАЛЯ 2024 года.
'''
'''
Домашняя работа

Курс: Разработка Web-приложений на Python, с применением Фреймворка Django
Дисциплина: Основы программирования на Python

Домашняя работа №30: Программы с интерфейсом (GUI) - tkinter и pyqt6

Выполните следующие задания:

Задание №1

а) Отрефакторить программу с прошлой домашней работы на ООП стиль.
'''
'''
Урок от 07.02.2024
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Выполнение задания:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
ВАРИАНТ только ОДИН (Взял код из домашней работы №29 от 02.02.2024 и переработал его под текущее задание)
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
КОД:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
import tkinter as tk
from tkinter import messagebox
import requests
import json

class JsonPlaceholderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Средство извлечения данных JSONPlaceholder")
        self.master.geometry('650x350')

        self.create_widgets()

    def create_widgets(self):
        self.label_user_id = tk.Label(self.master, text="Введите идентификатор пользователя:")
        self.label_user_id.pack(pady=10)

        self.entry_user_id = tk.Entry(self.master)
        self.entry_user_id.pack(pady=10)

        self.fetch_button = tk.Button(self.master, text="Извлечь данные", command=self.on_fetch_button_click)
        self.fetch_button.pack(pady=10)

    def fetch_data(self, user_id):
        try:
            url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
            response = requests.get(url)
            response.raise_for_status()

            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Ошибка", f"Не удалось получить данные: {e}")
            return None

    def save_data(self, data, file_path):
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=2)
            messagebox.showinfo("Успех", f"Данные, сохраненные в {file_path}")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить данные: {e}")

    def on_fetch_button_click(self):
        user_id = self.entry_user_id.get()
        if not user_id.isdigit():
            messagebox.showwarning("Предупреждение", "Идентификатор пользователя должен быть числом")
            return

        user_id = int(user_id)
        data = self.fetch_data(user_id)
        if data:
            self.save_data(data, "user_data.json")

if __name__ == "__main__":
    root = tk.Tk()
    app = JsonPlaceholderApp(root)
    root.mainloop()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг №1: Импорт библиотек и создание класса
'''
import tkinter as tk
from tkinter import messagebox
import requests
import json
'''
Пример выполнения этого шага:

В данном шаге мы импортируем необходимые библиотеки для работы 
с графическим интерфейсом (tkinter), диалоговыми окнами сообщений (messagebox), 
запросами к внешнему API (requests), и обработкой данных в формате JSON (json).

Затем создается класс JsonPlaceholderApp, представляющий приложение для извлечения данных с JSONPlaceholder.


Подробное описание этого кода:

tkinter: Библиотека для создания графического интерфейса пользователя.
messagebox: Модуль из библиотеки tkinter, предоставляющий функционал для вывода диалоговых окон с сообщениями.
requests: Библиотека для выполнения HTTP-запросов.
json: Модуль для работы с данными в формате JSON.
'''
'''
Шаг №2: Определение класса JsonPlaceholderApp
'''
class JsonPlaceholderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Средство извлечения данных JSONPlaceholder")
        self.master.geometry('650x350')

        self.create_widgets()
'''
Пример выполнения этого шага:

В этом шаге создается класс JsonPlaceholderApp, который представляет
собой приложение для извлечения данных с JSONPlaceholder.

В методе __init__ инициализируются атрибуты класса, такие как master (главное окно приложения),
устанавливается заголовок окна и его размер.


Подробное описание этого кода:

__init__: Это метод инициализации класса. self представляет экземпляр класса.
master - это главное окно приложения. Устанавливается заголовок окна и его размер.
'''
'''
Шаг №3: Настройка графического интерфейса
'''
def create_widgets(self):
    self.label_user_id = tk.Label(self.master, text="Введите идентификатор пользователя:")
    self.label_user_id.pack(pady=10)

    self.entry_user_id = tk.Entry(self.master)
    self.entry_user_id.pack(pady=10)

    self.fetch_button = tk.Button(self.master, text="Извлечь данные", command=self.on_fetch_button_click)
    self.fetch_button.pack(pady=10)
'''
Пример выполнения этого шага:

Метод create_widgets используется для настройки элементов графического интерфейса приложения.

Создаются метка (self.label_user_id), поле ввода (self.entry_user_id) и кнопка (self.fetch_button),
которые будут использоваться для ввода идентификатора пользователя и выполнения запроса.


Подробное описание этого кода:

tk.Label: Класс для создания метки. 
Используется для отображения текста на графическом интерфейсе.
tk.Entry: Класс для создания поля ввода. 
Используется для ввода данных с клавиатуры.
tk.Button: Класс для создания кнопки. 
Используется для выполнения определенных действий при ее нажатии.
'''
'''
Шаг №4: Метод fetch_data
'''
def fetch_data(self, user_id):
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
Пример выполнения этого шага:

Метод fetch_data принимает идентификатор пользователя, отправляет запрос к API JSONPlaceholder
и возвращает полученные данные в формате JSON.

В случае ошибки запроса или обработки данных, выводится сообщение об ошибке с использованием диалогового окна.


Подробное описание этого кода:

requests.get: Выполняет GET-запрос к указанному URL.
response.raise_for_status(): Проверяет статус ответа. Если статус не успешен, вызывается исключение.
response.json(): Преобразует ответ в формате JSON в объект Python.
'''
'''
Шаг №5: Метод save_data
'''
def save_data(self, data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)
        messagebox.showinfo("Успех", f"Данные, сохраненные в {file_path}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось сохранить данные: {e}")
'''
Пример выполнения этого шага:

Метод save_data принимает данные и путь к файлу, в который данные будут сохранены в формате JSON.

Данные записываются в файл, и в случае успеха выводится сообщение об успешном сохранении.
В случае ошибки также выводится сообщение.


Подробное описание этого кода:

with open(file_path, 'w') as file: Открывает файл для записи. with используется для
автоматического закрытия файла после завершения блока кода.
json.dump(data, file, indent=2): Записывает данные в формате JSON в файл с отступами
для улучшенного читаемости.
messagebox.showinfo: Выводит информационное сообщение.
'''
'''
Шаг №6: Метод on_fetch_button_click
'''
def on_fetch_button_click(self):
    user_id = self.entry_user_id.get()
    if not user_id.isdigit():
        messagebox.showwarning("Предупреждение", "Идентификатор пользователя должен быть числом")
        return

    user_id = int(user_id)
    data = self.fetch_data(user_id)
    if data:
        self.save_data(data, "user_data.json")
'''
Пример выполнения этого шага:

Метод on_fetch_button_click вызывается при нажатии кнопки "Извлечь данные".
Получает идентификатор пользователя из поля ввода, проверяет, что он является числом.
Если пользователь ввел корректный идентификатор, вызывает метод fetch_data для получения данных
и метод save_data для сохранения данных в файл "user_data.json".


Подробное описание этого кода:

self.entry_user_id.get(): Получает текст из поля ввода идентификатора пользователя.
not user_id.isdigit(): Проверяет, что идентификатор состоит только из цифр.
messagebox.showwarning: Выводит предупреждение в случае некорректного ввода пользователя.
self.fetch_data(user_id): Вызывает метод для получения данных по идентификатору пользователя.
self.save_data(data, "user_data.json"): Вызывает метод для сохранения полученных данных в файл "user_data.json".
'''
'''
Шаг №7: Запуск основной программы
'''
if __name__ == "__main__":
    root = tk.Tk()
    app = JsonPlaceholderApp(root)
    root.mainloop()
'''
Пример выполнения этого шага:

Создается экземпляр главного окна (root) и экземпляра приложения (app) на основе класса JsonPlaceholderApp.
Запускается главный цикл обработки событий с помощью root.mainloop(), что позволяет
взаимодействовать с пользователем через графический интерфейс.


Подробное описание этого кода:

__name__ == "__main__": Условие, проверяющее, что скрипт был запущен непосредственно,
а не импортирован в качестве модуля.
tk.Tk(): Создает главное окно приложения.
JsonPlaceholderApp(root): Создает экземпляр приложения на основе класса JsonPlaceholderApp,
передавая ему главное окно.
root.mainloop(): Запускает бесконечный цикл обработки событий, благодаря которому приложение 
ожидает взаимодействия с пользователем.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Список дел - Вариант №1 (простой)
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
КОД:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Список дел")
        self.master.geometry('400x300')

        self.tasks = []

        self.setup_gui()

    def setup_gui(self):
        # Создаем виджет для ввода задачи
        self.task_entry = tk.Entry(self.master, width=30)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Кнопка для добавления задачи
        add_button = tk.Button(self.master, text="Добавить", command=self.add_task)
        add_button.grid(row=0, column=1, padx=10, pady=10)

        # Создаем список для отображения задач
        self.task_listbox = tk.Listbox(self.master, width=40, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Кнопка для удаления выбранной задачи
        delete_button = tk.Button(self.master, text="Удалить", command=self.delete_task)
        delete_button.grid(row=2, column=0, padx=10, pady=10)

    def add_task(self):
        new_task = self.task_entry.get()
        if new_task:
            self.tasks.append(new_task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)  # Очищаем поле ввода

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг №1: Импорт библиотек и создание класса
'''
import tkinter as tk
from tkinter import messagebox
'''
Пример выполнения этого шага:

В этом шаге мы импортируем необходимые библиотеки для работы с 
графическим интерфейсом (tkinter) и для вывода диалоговых окон (messagebox).
Затем создается класс ToDoListApp, представляющий приложение для списка дел.


Подробное описание этого кода:

tkinter: Библиотека для создания графического интерфейса пользователя.
messagebox: Модуль из библиотеки tkinter, предоставляющий функционал для вывода диалоговых окон с сообщениями.
'''
'''
Шаг №2: Определение класса ToDoListApp
'''
class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Список дел")
        self.master.geometry('400x300')

        self.tasks = []

        self.setup_gui()
'''
Пример выполнения этого шага:

В этом шаге создается класс ToDoListApp, который представляет собой приложение для списка дел.

В методе __init__ инициализируются атрибуты класса, такие как master (главное окно приложения), 
устанавливается заголовок окна, его размер и создается пустой список задач (self.tasks).


Подробное описание этого кода:

__init__: Это метод инициализации класса. self представляет экземпляр класса. master - это главное окно приложения.
Устанавливается заголовок окна, его размер и создается пустой список задач.
'''
'''
Шаг №3: Настройка графического интерфейса
'''
def setup_gui(self):
    # Создаем виджет для ввода задачи
    self.task_entry = tk.Entry(self.master, width=30)
    self.task_entry.grid(row=0, column=0, padx=10, pady=10)

    # Кнопка для добавления задачи
    add_button = tk.Button(self.master, text="Добавить", command=self.add_task)
    add_button.grid(row=0, column=1, padx=10, pady=10)

    # Создаем список для отображения задач
    self.task_listbox = tk.Listbox(self.master, width=40, height=10)
    self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    # Кнопка для удаления выбранной задачи
    delete_button = tk.Button(self.master, text="Удалить", command=self.delete_task)
    delete_button.grid(row=2, column=0, padx=10, pady=10)
'''
Пример выполнения этого шага:

Метод setup_gui используется для настройки элементов графического интерфейса приложения.
Создаются виджет для ввода задачи (self.task_entry), кнопка для добавления задачи (add_button),
список для отображения задач (self.task_listbox) и кнопка для удаления выбранной задачи (delete_button).


Подробное описание этого кода:

tk.Entry: Класс для создания поля ввода. Используется для ввода новой задачи.
tk.Button: Класс для создания кнопки. Используется для выполнения определенных действий при ее нажатии.
tk.Listbox: Класс для создания списка. Используется для отображения списка задач.
'''
'''
Шаг №4: Метод add_task
'''
def add_task(self):
    new_task = self.task_entry.get()
    if new_task:
        self.tasks.append(new_task)
        self.update_task_list()
        self.task_entry.delete(0, tk.END)  # Очищаем поле ввода
'''
Пример выполнения этого шага:

Метод add_task вызывается при нажатии кнопки "Добавить".
Получает новую задачу из поля ввода, проверяет, что она не пуста.
Если новая задача введена, она добавляется в список задач (self.tasks), обновляется список
отображаемых задач, и поле ввода очищается.


Подробное описание этого кода:

self.task_entry.get(): Получает текст из поля ввода.
self.tasks.append(new_task): Добавляет новую задачу в список задач.
self.update_task_list(): Обновляет отображаемый список задач.
self.task_entry.delete(0, tk.END): Очищает поле ввода после добавления задачи.
'''
'''
Шаг №5: Метод delete_task
'''
def delete_task(self):
    selected_task_index = self.task_listbox.curselection()
    if selected_task_index:
        self.tasks.pop(selected_task_index[0])
        self.update_task_list()
'''
Пример выполнения этого шага:

Метод delete_task вызывается при нажатии кнопки "Удалить".
Получает индекс выбранной задачи из списка (self.task_listbox.curselection()).
Если задача выбрана, она удаляется из списка задач (self.tasks), и отображаемый список задач обновляется.


Подробное описание этого кода:

self.task_listbox.curselection(): Возвращает индексы выбранных элементов в списке. 
В данном случае, индекс выбранной задачи.
self.tasks.pop(selected_task_index[0]): Удаляет выбранную задачу из списка задач.
self.update_task_list(): Обновляет отображаемый список задач.
'''
'''
Шаг №6: Метод update_task_list
'''
def update_task_list(self):
    self.task_listbox.delete(0, tk.END)
    for task in self.tasks:
        self.task_listbox.insert(tk.END, task)
'''
Пример выполнения этого шага:

Метод update_task_list обновляет отображаемый список задач.
Очищает список (self.task_listbox.delete(0, tk.END)) и затем добавляет все задачи из 
списка self.tasks в список для отображения.


Подробное описание этого кода:

self.task_listbox.delete(0, tk.END): Очищает список задач перед обновлением.
for task in self.tasks: self.task_listbox.insert(tk.END, task): Добавляет 
каждую задачу из списка в список для отображения.
'''
'''
Шаг №7: Запуск основной программы
'''
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
'''
Пример выполнения этого шага:

Создается экземпляр главного окна (root) и экземпляра приложения (app) на основе класса ToDoListApp.
Запускается главный цикл обработки событий с помощью root.mainloop(), 
что позволяет взаимодействовать с пользователем через графический интерфейс.


Подробное описание этого кода:

__name__ == "__main__": Условие, проверяющее, что скрипт был запущен непосредственно, 
а не импортирован в качестве модуля.
tk.Tk(): Создает главное окно приложения.
ToDoListApp(root): Создает экземпляр приложения на основе класса ToDoListApp, передавая ему главное окно.
root.mainloop(): Запускает бесконечный цикл обработки событий, благодаря 
которому приложение ожидает взаимодействия с пользователем.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Список дел - Вариант №2 (чуть-чуть лучше)
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
КОД:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Список дел")
        self.master.geometry('300x500')

        self.tasks = []

        # Загрузка изображения с использованием Pillow
        original_logo = Image.open("E:\\EBAL_EGO_V_ROT_ETOT_PYCHARM\\SOSI_PYTHON_SUKA\\LESSON_30\\LOGO_HW_№30_07.02.2024.png")


        # Изменение размера логотипа
        new_width = 100  # Новая ширина логотипа
        new_height = 100  # Новая высота логотипа
        resized_logo = original_logo.resize((new_width, new_height))


        # Преобразование изображения Pillow в формат, поддерживаемый Tkinter
        self.logo = ImageTk.PhotoImage(resized_logo)

        # Отображение логотипа в Label
        self.logo_label = tk.Label(self.master, image=self.logo)
        self.logo_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.setup_gui()

    def setup_gui(self):
        self.task_entry = tk.Entry(self.master, width=30)
        self.task_entry.grid(row=1, column=0, padx=10, pady=10)

        add_button = tk.Button(self.master, text="Добавить", command=self.add_task, bg='#4CAF50', fg='white')
        add_button.grid(row=1, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(self.master, width=40, height=10, selectmode=tk.SINGLE)
        self.task_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        delete_button = tk.Button(self.master, text="Удалить", command=self.delete_task, bg='#FF0000', fg='white')
        delete_button.grid(row=3, column=0, padx=10, pady=10)

        delete_all_button = tk.Button(self.master, text="Удалить все", command=self.delete_all_tasks, bg='#FF0000', fg='white')
        delete_all_button.grid(row=3, column=1, padx=10, pady=10)

        complete_button = tk.Button(self.master, text="Выполнено", command=self.complete_task, bg='#008CBA', fg='white')
        complete_button.grid(row=4, column=0, columnspan=2, pady=10)

    def add_task(self):
        new_task = self.task_entry.get()
        if new_task:
            self.tasks.append({"text": new_task, "completed": False})
            self.update_task_list()
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_task_list()

    def delete_all_tasks(self):
        confirmed = messagebox.askyesno("Подтверждение", "Вы уверены, что хотите удалить все задачи?")
        if confirmed:
            self.tasks.clear()
            self.update_task_list()

    def complete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.tasks[selected_task_index[0]]
            task["completed"] = not task["completed"]
            self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in sorted(self.tasks, key=lambda x: x["text"]):
            text = f"✔ {task['text']}" if task['completed'] else task['text']
            self.task_listbox.insert(tk.END, text)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг №1: Импорт библиотек и создание класса
'''
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
'''
Пример выполнения этого шага:

В этом шаге мы импортируем библиотеки для создания графического интерфейса (tkinter),
вывода диалоговых окон (messagebox), а также для работы с изображениями (PIL).


Подробное описание этого кода:

tkinter: Библиотека для создания графического интерфейса пользователя.
messagebox: Модуль из библиотеки tkinter, предоставляющий функционал для вывода диалоговых окон с сообщениями.
PIL: Библиотека для работы с изображениями.
'''
'''
Шаг №2: Определение класса ToDoListApp
'''
class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Список дел")
        self.master.geometry('300x500')

        self.tasks = []

        original_logo = Image.open("E:\\EBAL_EGO_V_ROT_ETOT_PYCHARM\\SOSI_PYTHON_SUKA\\LESSON_30\\LOGO_HW_№30_07.02.2024.png")
        new_width = 100
        new_height = 100
        resized_logo = original_logo.resize((new_width, new_height))

        self.logo = ImageTk.PhotoImage(resized_logo)

        self.logo_label = tk.Label(self.master, image=self.logo)
        self.logo_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.setup_gui()
'''
Пример выполнения этого шага:

В этом шаге создается класс ToDoListApp, который представляет собой приложение для списка дел.
Изображение логотипа загружается, изменяется размер и преобразуется в формат, поддерживаемый Tkinter.
Логотип отображается в виджете Label.


Подробное описание этого кода:

Image.open: Загружает изображение из файла.
resize: Изменяет размер изображения.
ImageTk.PhotoImage: Преобразует изображение Pillow в формат, поддерживаемый Tkinter.
tk.Label: Виджет для отображения изображения логотипа.
'''
'''
Шаг №3: Настройка графического интерфейса
'''
def setup_gui(self):
    self.task_entry = tk.Entry(self.master, width=30)
    self.task_entry.grid(row=1, column=0, padx=10, pady=10)

    add_button = tk.Button(self.master, text="Добавить", command=self.add_task, bg='#4CAF50', fg='white')
    add_button.grid(row=1, column=1, padx=10, pady=10)

    self.task_listbox = tk.Listbox(self.master, width=40, height=10, selectmode=tk.SINGLE)
    self.task_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    delete_button = tk.Button(self.master, text="Удалить", command=self.delete_task, bg='#FF0000', fg='white')
    delete_button.grid(row=3, column=0, padx=10, pady=10)

    delete_all_button = tk.Button(self.master, text="Удалить все", command=self.delete_all_tasks, bg='#FF0000',
                                  fg='white')
    delete_all_button.grid(row=3, column=1, padx=10, pady=10)

    complete_button = tk.Button(self.master, text="Выполнено", command=self.complete_task, bg='#008CBA', fg='white')
    complete_button.grid(row=4, column=0, columnspan=2, pady=10)
'''
Пример выполнения этого шага:

Метод setup_gui используется для настройки элементов графического интерфейса приложения.
Создаются виджет для ввода задачи (self.task_entry), кнопка для добавления задачи (add_button),
список для отображения задач (self.task_listbox) и кнопки для удаления выбранной задачи,
удаления всех задач и отметки задачи как выполненной.


Подробное описание этого кода:

tk.Entry: Поле ввода для новой задачи.
tk.Button: Кнопки для добавления, удаления и отметки задачи.
tk.Listbox: Список для отображения задач.
'''
'''
Шаг №4: Метод add_task
'''
def add_task(self):
    new_task = self.task_entry.get()
    if new_task:
        self.tasks.append({"text": new_task, "completed": False})
        self.update_task_list()
        self.task_entry.delete(0, tk.END)
'''
Пример выполнения этого шага:

Метод add_task вызывается при нажатии кнопки "Добавить".
Получает новую задачу из поля ввода, проверяет, что она не пуста.
Если новая задача введена, она добавляется в список задач (self.tasks),
обновляется отображаемый список и поле ввода очищается.


Подробное описание этого кода:

self.task_entry.get(): Получает текст из поля ввода.
self.tasks.append({"text": new_task, "completed": False}): Добавляет новую задачу в список задач.
self.update_task_list(): Обновляет отображаемый список задач.
self.task_entry.delete(0, tk.END): Очищает поле ввода после добавления задачи.
'''
'''
Шаг №5: Метод delete_task
'''
def delete_task(self):
    selected_task_index = self.task_listbox.curselection()
    if selected_task_index:
        self.tasks.pop(selected_task_index[0])
        self.update_task_list()
'''
Пример выполнения этого шага:

Метод delete_task вызывается при нажатии кнопки "Удалить".
Получает индекс выбранной задачи из списка (self.task_listbox.curselection()).
Если задача выбрана, она удаляется из списка задач (self.tasks), и отображаемый список задач обновляется.


Подробное описание этого кода:

self.task_listbox.curselection(): Возвращает индексы выбранных элементов в списке. 
В данном случае, индекс выбранной задачи.
self.tasks.pop(selected_task_index[0]): Удаляет выбранную задачу из списка задач.
self.update_task_list(): Обновляет отображаемый список задач.
'''
'''
Шаг №6: Метод delete_all_tasks
'''
def delete_all_tasks(self):
    confirmed = messagebox.askyesno("Подтверждение", "Вы уверены, что хотите удалить все задачи?")
    if confirmed:
        self.tasks.clear()
        self.update_task_list()
'''
Пример выполнения этого шага:

Метод delete_all_tasks вызывается при нажатии кнопки "Удалить все".
Выводит диалоговое окно для подтверждения удаления всех задач.
Если подтверждено, все задачи удаляются из списка (self.tasks), и отображаемый список задач обновляется.


Подробное описание этого кода:

messagebox.askyesno: Выводит диалоговое окно с вопросом, требующим ответа "Да" или "Нет".
self.tasks.clear(): Удаляет все задачи из списка задач.
self.update_task_list(): Обновляет отображаемый список задач.
'''
'''
Шаг №7: Метод complete_task
'''
def complete_task(self):
    selected_task_index = self.task_listbox.curselection()
    if selected_task_index:
        task = self.tasks[selected_task_index[0]]
        task["completed"] = not task["completed"]
        self.update_task_list()
'''
Пример выполнения этого шага:

Метод complete_task вызывается при нажатии кнопки "Выполнено".
Получает индекс выбранной задачи из списка (self.task_listbox.curselection()).
Если задача выбрана, меняет статус выполнения задачи на противоположный 
(завершена/не завершена) и обновляет отображаемый список задач.


Подробное описание этого кода:

self.tasks[selected_task_index[0]]["completed"] = not task["completed"]: Меняет статус 
выполнения выбранной задачи на противоположный.
self.update_task_list(): Обновляет отображаемый список задач.
'''
'''
Шаг №8: Метод update_task_list
'''
def update_task_list(self):
    self.task_listbox.delete(0, tk.END)
    for task in sorted(self.tasks, key=lambda x: x["text"]):
        text = f"✔ {task['text']}" if task['completed'] else task['text']
        self.task_listbox.insert(tk.END, text)
'''
Пример выполнения этого шага:

Метод update_task_list обновляет отображаемый список задач.
Очищает список (self.task_listbox.delete(0, tk.END)) и затем добавляет
все задачи из списка self.tasks в список для отображения.


Подробное описание этого кода:

self.task_listbox.delete(0, tk.END): Очищает список задач перед обновлением.
for task in sorted(self.tasks, key=lambda x: x["text"]): Проходит по всем задачам, отсортированным по тексту.
text = f"✔ {task['text']}" if task['completed'] else task['text']: Формирует текст для о
тображения задачи с меткой ✔, если задача выполнена.
self.task_listbox.insert(tk.END, text): Добавляет текст задачи в список для отображения.
'''
'''
Шаг №9: Запуск приложения
'''
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
'''
Пример выполнения этого шага:

Создается объект класса ToDoListApp и запускается главный цикл (root.mainloop()).


Подробное описание этого кода:

tk.Tk(): Создает главное окно приложения.
ToDoListApp(root): Создает экземпляр приложения для списка дел.
root.mainloop(): Запускает главный цикл для отображения графического интерфейса.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~