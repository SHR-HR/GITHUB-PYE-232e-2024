'''
Дата выполнения Домашней-Работы: 09 - ФЕВРАЛЯ - 10 ФЕВРАЛЯ 2024 года.
'''
'''
Домашняя работа

Курс: Разработка Web-приложений на Python, с применением Фреймворка Django
Дисциплина: Основы программирования на Python

Домашняя работа №32: Программы с интерфейсом (GUI) - tkinter и pyqt6

Выполните следующие задания:

Задание №1
Пункты:

✓ 1. Создайте полностью рабочий код - приложение: "Список контактов".

✓ 2. Программа должна иметь возможность создавать 
новые контакты - для формирования "Списка контактов".

✓ 3. Программа должна иметь возможность сохранять все данные, которые ей введет пользователь, такие как:

- Фамилия Имя Отчество
- Номер телефона
- Дата рождения
- Адрес проживания
- Email адрес электронной почты
- Instagram аккаунт
- Facebook аккаунт
- Комментарий к текущему создаваемому контакту

✓ 4. Также не мало важно, чтобы при создании нового контакта и, или редактировании старого и,
или недавно созданного контакта должна быть реализована возможность определить 
или выбрать к какой из групп - относится данный контакт.

(Примеры групп: "Семья", "Близкие Родственники", "Дальние Родственники", "Друзья", "Коллеги по работе",
"Начальство", "Первая помощь", "Аптека", "Доставка Еды", "Доставка (различных товаров)", "Услуги",
"Неизвестные", "Мошенники", "Черный список").


✓ 5. Программа должна иметь возможность, чтобы контакты могли помечаться как избранные
контакты - нажатием на кнопку "★" или "добавить в избранное" при моменте создания контакта.

✓ 6. Программа дожна иметь возможность, чтобы пользователь мог поделиться контактом - нажатием 
на кнопку "🔗" или "поделиться контактом" - и предложить выбрать одну из социальных сетей: 
таких как Instagram, Facebook, или отправить их в мессенджеры: Telegram, или WhatsApp.

✓ 7. В программе всегда должна быть возможность создание или добавление нового
контакта - по нажатию на кнопку "+" или "добавить контакт".

✓ 8. В программе всегда должна быть возможность удаление нового
контакта - по нажатию на кнопку "×" или "удалить контакт".

✓ 9. В программе всегда должна быть возможность редактирование нового или уже имеющегося 
контакта - по нажатию на кнопку "✎" или "Изменить контакт".

✓ 10. Программа должна иметь возможность сохранять все созданные
контакты в файл .xls - по нажатию на кнопку "✓" или "Сохранить все контакты".

✓ 11. Программа должна иметь возможность открывать список
контактов из файла - по нажатию на кнопку "🢁" или "Из файла".
'''
'''
Урок от 14.02.2024
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Выполнение задания:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
ВАРИАНТ 1
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
КОД:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
import tkinter as tk
from tkinter import messagebox, filedialog
import xlwt
import xlrd

class Contact:
    def __init__(self, first_name, last_name, middle_name, phone,
                 birthday, address, email, instagram, facebook, comment, group, is_favorite=False):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.phone = phone
        self.birthday = birthday
        self.address = address
        self.email = email
        self.instagram = instagram
        self.facebook = facebook
        self.comment = comment
        self.group = group
        self.is_favorite = is_favorite

class ContactsApp:
    def __init__(self, root):
        self.contacts = []
        self.current_contact_index = None

        self.root = root
        self.root.title("Мои Контакты")

        # Создание и размещение виджетов
        self.label_first_name = tk.Label(root, text="Имя:")
        self.label_last_name = tk.Label(root, text="Фамилия:")
        self.label_middle_name = tk.Label(root, text="Отчество:")
        self.label_phone = tk.Label(root, text="Номер телефона:")
        self.label_birthday = tk.Label(root, text="Дата рождения:")
        self.label_address = tk.Label(root, text="Адрес проживания:")
        self.label_email = tk.Label(root, text="Email:")
        self.label_instagram = tk.Label(root, text="Instagram:")
        self.label_facebook = tk.Label(root, text="Facebook:")
        self.label_comment = tk.Label(root, text="Комментарий:")
        self.label_group = tk.Label(root, text="Группа:")

        self.entry_first_name = tk.Entry(root)
        self.entry_last_name = tk.Entry(root)
        self.entry_middle_name = tk.Entry(root)
        self.entry_phone = tk.Entry(root)
        self.entry_birthday = tk.Entry(root)
        self.entry_address = tk.Entry(root)
        self.entry_email = tk.Entry(root)
        self.entry_instagram = tk.Entry(root)
        self.entry_facebook = tk.Entry(root)
        self.entry_comment = tk.Entry(root)

        self.group_options = ["Семья", "Близкие Родственники", "Друзья", "Коллеги по работе", "Неизвестные"]
        self.group_var = tk.StringVar(root)
        self.group_var.set(self.group_options[0])
        self.group_menu = tk.OptionMenu(root, self.group_var, *self.group_options)

        self.favorite_var = tk.BooleanVar(root)
        self.favorite_var.set(False)
        self.checkbutton_favorite = tk.Checkbutton(root, text="Добавить в избранное", variable=self.favorite_var)

        self.button_save = tk.Button(root, text="Сохранить", command=self.save_contact)
        self.button_save_all = tk.Button(root, text="Сохранить все контакты", command=self.save_all_contacts)
        self.button_load_from_file = tk.Button(root, text="Из файла", command=self.load_contacts_from_file)
        self.button_view_contacts = tk.Button(root, text="Просмотреть контакты", command=self.view_contacts)
        self.button_share_contact = tk.Button(root, text="Поделиться контактом", command=self.share_contact)

        self.button_add_contact = tk.Button(root, text="Добавить контакт", command=self.add_contact)
        self.button_delete_contact = tk.Button(root, text="Удалить контакт", command=self.delete_contact)
        self.button_edit_contact = tk.Button(root, text="Изменить контакт", command=self.edit_contact)

        # Добавлен новый виджет для списка контактов
        self.listbox = tk.Listbox(root)
        self.listbox.grid(row=17, column=0, columnspan=2)
        self.listbox.bind("<ButtonRelease-1>", self.select_contact)

        self.label_first_name.grid(row=0, column=0)
        self.label_last_name.grid(row=1, column=0)
        self.label_middle_name.grid(row=2, column=0)
        self.label_phone.grid(row=3, column=0)
        self.label_birthday.grid(row=4, column=0)
        self.label_address.grid(row=5, column=0)
        self.label_email.grid(row=6, column=0)
        self.label_instagram.grid(row=7, column=0)
        self.label_facebook.grid(row=8, column=0)
        self.label_comment.grid(row=9, column=0)
        self.label_group.grid(row=10, column=0)

        self.entry_first_name.grid(row=0, column=1)
        self.entry_last_name.grid(row=1, column=1)
        self.entry_middle_name.grid(row=2, column=1)
        self.entry_phone.grid(row=3, column=1)
        self.entry_birthday.grid(row=4, column=1)
        self.entry_address.grid(row=5, column=1)
        self.entry_email.grid(row=6, column=1)
        self.entry_instagram.grid(row=7, column=1)
        self.entry_facebook.grid(row=8, column=1)
        self.entry_comment.grid(row=9, column=1)
        self.group_menu.grid(row=10, column=1)

        self.checkbutton_favorite.grid(row=11, column=1)

        self.button_save.grid(row=12, column=1)
        self.button_save_all.grid(row=13, column=1)
        self.button_load_from_file.grid(row=14, column=1)
        self.button_view_contacts.grid(row=15, column=1)
        self.button_share_contact.grid(row=16, column=1)

        self.button_add_contact.grid(row=12, column=0)
        self.button_delete_contact.grid(row=13, column=0)
        self.button_edit_contact.grid(row=14, column=0)

    def save_contact(self):
        first_name = self.entry_first_name.get()
        last_name = self.entry_last_name.get()
        middle_name = self.entry_middle_name.get()
        phone = self.entry_phone.get()
        birthday = self.entry_birthday.get()
        address = self.entry_address.get()
        email = self.entry_email.get()
        instagram = self.entry_instagram.get()
        facebook = self.entry_facebook.get()
        comment = self.entry_comment.get()
        group = self.group_var.get()
        is_favorite = self.favorite_var.get()

        if first_name and last_name and phone:
            contact = Contact(first_name, last_name, middle_name,
                              phone, birthday, address, email, instagram, facebook, comment, group, is_favorite)
            self.contacts.append(contact)
            self.update_contacts_listbox()
            messagebox.showinfo("Успех", "Контакт сохранен!")
            self.clear_entry_fields()
        else:
            messagebox.showerror("Ошибка", "Заполните обязательные поля: Имя, Фамилия, Номер телефона")

    def save_all_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Информация", "Список контактов пуст.")
            return

        file_name = filedialog.asksaveasfilename(defaultextension=".xls", filetypes=[("Excel Files", "*.xls")])
        if file_name:
            workbook = xlwt.Workbook()
            sheet = workbook.add_sheet("Контакты")

            headers = ["Имя", "Фамилия", "Отчество", "Номер телефона", "Дата рождения", "Адрес проживания",
                       "Email", "Instagram", "Facebook", "Комментарий", "Группа", "Избранный"]

            for col, header in enumerate(headers):
                sheet.write(0, col, header)

            for row, contact in enumerate(self.contacts, start=1):
                sheet.write(row, 0, contact.first_name)
                sheet.write(row, 1, contact.last_name)
                sheet.write(row, 2, contact.middle_name)
                sheet.write(row, 3, contact.phone)
                sheet.write(row, 4, contact.birthday)
                sheet.write(row, 5, contact.address)
                sheet.write(row, 6, contact.email)
                sheet.write(row, 7, contact.instagram)
                sheet.write(row, 8, contact.facebook)
                sheet.write(row, 9, contact.comment)
                sheet.write(row, 10, contact.group)
                sheet.write(row, 11, "Да" if contact.is_favorite else "Нет")

            workbook.save(file_name)
            messagebox.showinfo("Успех", f"Все контакты сохранены в файл: {file_name}")

    def load_contacts_from_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xls")])
        if file_path:
            workbook = xlrd.open_workbook(file_path)
            sheet = workbook.sheet_by_index(0)

            headers = [sheet.cell_value(0, col) for col in range(sheet.ncols)]
            contacts = []

            translation = {
                "Имя": "first_name",
                "Фамилия": "last_name",
                "Отчество": "middle_name",
                "Номер телефона": "phone",
                "Дата рождения": "birthday",
                "Адрес проживания": "address",
                "Email": "email",
                "Instagram": "instagram",
                "Facebook": "facebook",
                "Комментарий": "comment",
                "Группа": "group",
                "Избранный": "is_favorite"
            }

            for row in range(1, sheet.nrows):
                contact_data = {translation.get(headers[col],
                                                headers[col]): sheet.cell_value(row, col) for col in range(sheet.ncols)}
                contact_data["is_favorite"] = contact_data.get("is_favorite", "Нет") == "Да"
                contact = Contact(**contact_data)
                contacts.append(contact)

            self.contacts = contacts
            self.update_contacts_listbox()
            messagebox.showinfo("Успех", f"Контакты загружены из файла: {file_path}")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Информация", "Список контактов пуст.")
            return

        view_window = tk.Toplevel(self.root)
        view_window.title("Список Контактов")

        listbox = tk.Listbox(view_window)
        for contact in self.contacts:
            listbox.insert(tk.END, f"{contact.first_name}"
                                   f" {contact.last_name} {'★' if contact.is_favorite else ''}")

        listbox.pack(expand=True, fill=tk.BOTH)

        def show_contact_info(event):
            selected_contact_index = listbox.curselection()
            if selected_contact_index:
                selected_contact = self.contacts[selected_contact_index[0]]
                info_window = tk.Toplevel(view_window)
                info_window.title("Информация о Контакте")

                info_label = tk.Label(info_window, text=f"Имя: {selected_contact.first_name}\n"
                                                        f"Фамилия: {selected_contact.last_name}\n"
                                                        f"Отчество: {selected_contact.middle_name}\n"
                                                        f"Номер телефона: {selected_contact.phone}\n"
                                                        f"Дата рождения: {selected_contact.birthday}\n"
                                                        f"Адрес проживания: {selected_contact.address}\n"
                                                        f"Email: {selected_contact.email}\n"
                                                        f"Instagram: {selected_contact.instagram}\n"
                                                        f"Facebook: {selected_contact.facebook}\n"
                                                        f"Комментарий: {selected_contact.comment}\n"
                                                        f"Группа: {selected_contact.group}\n"
                                                        f"Избранный: {'Да' if selected_contact.is_favorite else 'Нет'}")
                info_label.pack()

        listbox.bind("<Double-Button-1>", show_contact_info)

    def share_contact(self):
        if not self.contacts:
            messagebox.showinfo("Информация", "Список контактов пуст.")
            return

        share_window = tk.Toplevel(self.root)
        share_window.title("Поделиться Контактом")

        listbox = tk.Listbox(share_window)
        for contact in self.contacts:
            listbox.insert(tk.END, f"{contact.first_name}"
                                   f" {contact.last_name} {'★' if contact.is_favorite else ''}")

        listbox.pack(expand=True, fill=tk.BOTH)

        def share_contact_info(event):
            selected_contact_index = listbox.curselection()
            if selected_contact_index:
                selected_contact = self.contacts[selected_contact_index[0]]
                share_options = ["Instagram", "Facebook", "Telegram", "WhatsApp"]
                share_var = tk.StringVar(share_window)
                share_var.set(share_options[0])
                share_menu = tk.OptionMenu(share_window, share_var, *share_options)
                share_menu.pack()

                def perform_share():
                    selected_option = share_var.get()
                    share_text = f"Имя: {selected_contact.first_name}\n" \
                                 f"Фамилия: {selected_contact.last_name}\n" \
                                 f"Отчество: {selected_contact.middle_name}\n" \
                                 f"Номер телефона: {selected_contact.phone}\n" \
                                 f"Дата рождения: {selected_contact.birthday}\n" \
                                 f"Адрес проживания: {selected_contact.address}\n" \
                                 f"Email: {selected_contact.email}\n" \
                                 f"Instagram: {selected_contact.instagram}\n" \
                                 f"Facebook: {selected_contact.facebook}\n" \
                                 f"Комментарий: {selected_contact.comment}\n" \
                                 f"Группа: {selected_contact.group}\n" \
                                 f"Избранный: {'Да' if selected_contact.is_favorite else 'Нет'}"

                    if selected_option == "Instagram":
                        messagebox.showinfo("Поделиться", f"Отправлено в Instagram:\n{share_text}")
                    elif selected_option == "Facebook":
                        messagebox.showinfo("Поделиться", f"Отправлено в Facebook:\n{share_text}")
                    elif selected_option == "Telegram":
                        messagebox.showinfo("Поделиться", f"Отправлено в Telegram:\n{share_text}")
                    elif selected_option == "WhatsApp":
                        messagebox.showinfo("Поделиться", f"Отправлено в WhatsApp:\n{share_text}")

                share_button = tk.Button(share_window, text="Поделиться", command=perform_share)
                share_button.pack()

        listbox.bind("<Double-Button-1>", share_contact_info)

    def add_contact(self):
        self.clear_entry_fields()
        self.current_contact_index = None

    def delete_contact(self):
        selected_contact_index = self.current_contact_index
        if selected_contact_index is not None:
            del self.contacts[selected_contact_index]
            self.update_contacts_listbox()
            messagebox.showinfo("Успех", "Контакт удален!")
            self.clear_entry_fields()
        else:
            messagebox.showerror("Ошибка", "Выберите контакт для удаления")

    def edit_contact(self):
        selected_contact_index = self.current_contact_index
        if selected_contact_index is not None:
            selected_contact = self.contacts[selected_contact_index]
            self.entry_first_name.delete(0, tk.END)
            self.entry_last_name.delete(0, tk.END)
            self.entry_middle_name.delete(0, tk.END)
            self.entry_phone.delete(0, tk.END)
            self.entry_birthday.delete(0, tk.END)
            self.entry_address.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)
            self.entry_instagram.delete(0, tk.END)
            self.entry_facebook.delete(0, tk.END)
            self.entry_comment.delete(0, tk.END)

            self.entry_first_name.insert(0, selected_contact.first_name)
            self.entry_last_name.insert(0, selected_contact.last_name)
            self.entry_middle_name.insert(0, selected_contact.middle_name)
            self.entry_phone.insert(0, selected_contact.phone)
            self.entry_birthday.insert(0, selected_contact.birthday)
            self.entry_address.insert(0, selected_contact.address)
            self.entry_email.insert(0, selected_contact.email)
            self.entry_instagram.insert(0, selected_contact.instagram)
            self.entry_facebook.insert(0, selected_contact.facebook)
            self.entry_comment.insert(0, selected_contact.comment)

            self.group_var.set(selected_contact.group)
            self.favorite_var.set(selected_contact.is_favorite)

            messagebox.showinfo("Успех", "Контакт готов к редактированию")
        else:
            messagebox.showerror("Ошибка", "Выберите контакт для редактирования")

    def clear_entry_fields(self):
        self.entry_first_name.delete(0, tk.END)
        self.entry_last_name.delete(0, tk.END)
        self.entry_middle_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_birthday.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_instagram.delete(0, tk.END)
        self.entry_facebook.delete(0, tk.END)
        self.entry_comment.delete(0, tk.END)
        self.group_var.set(self.group_options[0])
        self.favorite_var.set(False)

    def update_contacts_listbox(self):
        self.listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.listbox.insert(tk.END, f"{contact.first_name}"
                                        f" {contact.last_name} {'★' if contact.is_favorite else ''}")

    def select_contact(self, event):
        selected_contact_index = self.listbox.curselection()
        if selected_contact_index:
            self.current_contact_index = selected_contact_index[0]

# Создаем главное окно
root = tk.Tk()
app = ContactsApp(root)
root.geometry("265x580")  # Изменено для лучшего отображения
root.mainloop()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
1. Импорт библиотек:
'''
import tkinter as tk
from tkinter import messagebox, filedialog
import xlwt
import xlrd
'''
tkinter - стандартная библиотека для создания графических интерфейсов в Python.
messagebox - модуль для создания диалоговых окон с сообщениями.
filedialog - модуль для работы с диалоговыми окнами для выбора файлов.
xlwt - библиотека для записи данных в файлы формата Excel.
xlrd - библиотека для чтения данных из файлов формата Excel.
'''
'''
2. Определение класса Contact:
'''
class Contact:
    def __init__(self, first_name, last_name, middle_name, phone, birthday, address,
                 email, instagram, facebook, comment, group, is_favorite=False):
        # Инициализация атрибутов контакта
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.phone = phone
        self.birthday = birthday
        self.address = address
        self.email = email
        self.instagram = instagram
        self.facebook = facebook
        self.comment = comment
        self.group = group
        self.is_favorite = is_favorite
'''
Класс Contact описывает структуру контакта с различными атрибутами.
'''
'''
3. Определение класса ContactsApp:
'''
class ContactsApp:
    def __init__(self, root):
        # Инициализация главного окна и основных атрибутов
        self.contacts = []
        self.current_contact_index = None
        self.root = root
        self.root.title("Мои Контакты")

        # Создание и размещение виджетов (лейблов, полей ввода, кнопок и др.)
        # ...
'''
Класс ContactsApp инициализирует главное окно приложения,
 а также создает различные виджеты для ввода и отображения данных контакта.
'''
'''
4. Главное окно приложения:
'''
# Создаем главное окно
root = tk.Tk()
app = ContactsApp(root)
root.geometry("265x580")  # Изменено для лучшего отображения
root.mainloop()
'''
Создается объект Tk (главное окно приложения).
Задается размер окна и запускается главный цикл Tkinter (mainloop).
'''
'''
5. Метод save_contact:
'''
def save_contact(self):
    # Получение данных из полей ввода
    first_name = self.entry_first_name.get()
    last_name = self.entry_last_name.get()
    # ... (остальные атрибуты)

    # Создание объекта Contact и добавление в список контактов
    if first_name and last_name and phone:
        contact = Contact(first_name, last_name, middle_name, phone, birthday,
                          address, email, instagram, facebook, comment, group, is_favorite)
        self.contacts.append(contact)
        # Обновление списка контактов в виджете Listbox
        self.update_contacts_listbox()
        messagebox.showinfo("Успех", "Контакт сохранен!")
        # Очистка полей ввода
        self.clear_entry_fields()
    else:
        messagebox.showerror("Ошибка", "Заполните обязательные поля: Имя, Фамилия, Номер телефона")
'''
Метод save_contact вызывается при сохранении контакта.
Получаются данные из полей ввода.
Создается объект Contact и добавляется в список контактов.
Обновляется виджет Listbox для отображения изменений.
Очищаются поля ввода.
'''
'''
6. Метод save_all_contacts:
'''
def save_all_contacts(self):
    # Проверка, что список контактов не пуст
    if not self.contacts:
        messagebox.showinfo("Информация", "Список контактов пуст.")
        return

    # Запрос имени файла для сохранения
    file_name = filedialog.asksaveasfilename(defaultextension=".xls", filetypes=[("Excel Files", "*.xls")])

    # Проверка, что было выбрано имя файла
    if file_name:
        # Создание и настройка книги Excel
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet("Контакты")

        # Заголовки столбцов
        headers = ["Имя", "Фамилия", "Отчество", "Номер телефона", "Дата рождения", "Адрес проживания",
                   "Email", "Instagram", "Facebook", "Комментарий", "Группа", "Избранный"]

        # Запись заголовков в первую строку
        for col, header in enumerate(headers):
            sheet.write(0, col, header)

        # Запись данных контактов в ячейки
        for row, contact in enumerate(self.contacts, start=1):
            sheet.write(row, 0, contact.first_name)
            sheet.write(row, 1, contact.last_name)
            # ... (остальные атрибуты)

        # Сохранение книги Excel
        workbook.save(file_name)
        messagebox.showinfo("Успех", f"Все контакты сохранены в файл: {file_name}")
'''
Метод save_all_contacts вызывается при сохранении всех контактов в файл Excel.
Проверяется, что список контактов не пуст.
Запрашивается имя файла для сохранения.
Создается книга Excel и записываются данные контактов в нее.
Сохраняется файл Excel.
'''
'''
7. Метод load_contacts_from_file:
'''
def load_contacts_from_file(self):
    # Запрос пути к файлу для загрузки
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xls")])

    # Проверка, что был выбран файл
    if file_path:
        # Открытие книги Excel
        workbook = xlrd.open_workbook(file_path)
        sheet = workbook.sheet_by_index(0)

        # Получение заголовков столбцов
        headers = [sheet.cell_value(0, col) for col in range(sheet.ncols)]
        contacts = []

        # Сопоставление заголовков с атрибутами класса Contact
        translation = {
            "Имя": "first_name",
            "Фамилия": "last_name",
            # ... (остальные атрибуты)
        }

        # Чтение данных из файла и создание объектов Contact
        for row in range(1, sheet.nrows):
            contact_data = {translation.get(headers[col], headers[col]): sheet.cell_value(row, col) for
                            col in range(sheet.ncols)}
            contact_data["is_favorite"] = contact_data.get("is_favorite", "Нет") == "Да"
            contact = Contact(**contact_data)
            contacts.append(contact)

        # Обновление списка контактов и вывод сообщения
        self.contacts = contacts
        self.update_contacts_listbox()
        messagebox.showinfo("Успех", f"Контакты загружены из файла: {file_path}")
'''
Метод load_contacts_from_file вызывается при загрузке контактов из файла Excel.
Запрашивается путь к файлу.
Открывается книга Excel, сопоставляются заголовки столбцов с атрибутами класса Contact.
Читаются данные из файла и создаются объекты Contact.
Обновляется список контактов и выводится сообщение.
'''
'''
8. Метод view_contacts:
'''
def view_contacts(self):
    # Проверка, что список контактов не пуст
    if not self.contacts:
        messagebox.showinfo("Информация", "Список контактов пуст.")
        return

    # Создание нового окна для просмотра контактов
    view_window = tk.Toplevel(self.root)
    view_window.title("Список Контактов")

    # Создание Listbox и заполнение его данными
    listbox = tk.Listbox(view_window)
    for contact in self.contacts:
        listbox.insert(tk.END, f"{contact.first_name} {contact.last_name}"
                               f" {'★' if contact.is_favorite else ''}")

    # Размещение Listbox на окне
    listbox.pack(expand=True, fill=tk.BOTH)

    # Функция для отображения подробной информации о контакте
    def show_contact_info(event):
        selected_contact_index = listbox.curselection()
        if selected_contact_index:
            selected_contact = self.contacts[selected_contact_index[0]]
            info_window = tk.Toplevel(view_window)
            info_window.title("Информация о Контакте")

            # Создание и размещение виджета Label с информацией о контакте
            info_label = tk.Label(info_window, text=f"Имя: {selected_contact.first_name}\n"
                                                    f"Фамилия: {selected_contact.last_name}\n"
                                                    f"Отчество: {selected_contact.middle_name}\n"
                                                    # ... (остальные атрибуты)
                                                    f"Избранный: {'Да' if selected_contact.is_favorite else 'Нет'}")
            info_label.pack()

    # Привязка функции к событию (двойной клик) на Listbox
    listbox.bind("<Double-Button-1>", show_contact_info)
'''
Метод view_contacts создает новое окно для просмотра контактов.
Создается виджет Listbox и заполняется данными из списка контактов.
Функция show_contact_info вызывается при двойном клике на контакте, создавая новое окно с подробной информацией.
'''
'''
9. Метод share_contact:
'''
def share_contact(self):
    # Проверка, что список контактов не пуст
    if not self.contacts:
        messagebox.showinfo("Информация", "Список контактов пуст.")
        return

    # Создание нового окна для поделиться контактом
    share_window = tk.Toplevel(self.root)
    share_window.title("Поделиться Контактом")

    # Создание Listbox и заполнение его данными
    listbox = tk.Listbox(share_window)
    for contact in self.contacts:
        listbox.insert(tk.END, f"{contact.first_name} "
                               f"{contact.last_name} {'★' if contact.is_favorite else ''}")

    # Размещение Listbox на окне
    listbox.pack(expand=True, fill=tk.BOTH)

    # Функция для поделиться информацией о контакте
    def share_contact_info(event):
        selected_contact_index = listbox.curselection()
        if selected_contact_index:
            selected_contact = self.contacts[selected_contact_index[0]]
            share_options = ["Instagram", "Facebook", "Telegram", "WhatsApp"]
            share_var = tk.StringVar(share_window)
            share_var.set(share_options[0])
            share_menu = tk.OptionMenu(share_window, share_var, *share_options)
            share_menu.pack()

            # Функция для выполнения операции поделиться
            def perform_share():
                selected_option = share_var.get()
                share_text = f"Имя: {selected_contact.first_name}\n" \
                             f"Фамилия: {selected_contact.last_name}\n" \
                             # ... (остальные атрибуты) \
                             f"Избранный: {'Да' if selected_contact.is_favorite else 'Нет'}"

                # Отображение сообщения в зависимости от выбранной опции
                if selected_option == "Instagram":
                    messagebox.showinfo("Поделиться", f"Отправлено в Instagram:\n{share_text}")
                elif selected_option == "Facebook":
                    messagebox.showinfo("Поделиться", f"Отправлено в Facebook:\n{share_text}")
                elif selected_option == "Telegram":
                    messagebox.showinfo("Поделиться", f"Отправлено в Telegram:\n{share_text}")
                elif selected_option == "WhatsApp":
                    messagebox.showinfo("Поделиться", f"Отправлено в WhatsApp:\n{share_text}")

            # Создание кнопки для выполнения операции поделиться
            share_button = tk.Button(share_window, text="Поделиться", command=perform_share)
            share_button.pack()

    # Привязка функции к событию (двойной клик) на Listbox
    listbox.bind("<Double-Button-1>", share_contact_info)
'''
Метод share_contact создает новое окно для поделиться контактом.
Создается виджет Listbox и заполняется данными из списка контактов.
Функция share_contact_info вызывается при двойном клике на контакте,
создавая новое окно с опциями для поделиться (Instagram, Facebook, Telegram, WhatsApp).
'''
'''
10. Дополнительные методы:
'''
'''
Методы add_contact, delete_contact, edit_contact и clear_entry_fields предназначены для добавления нового контакта,
удаления контакта, редактирования контакта и очистки полей ввода соответственно.
Метод update_contacts_listbox обновляет виджет Listbox, отображая текущий список контактов.
Метод select_contact вызывается при выборе контакта в Listbox и обновляет текущий выбранный индекс контакта.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
ВАРИАНТ 2
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
КОД:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
import sys
import pandas as pd
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, \
    QFileDialog, QInputDialog, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QPixmap
from PIL import Image


class ContactListApp(QWidget):
    def __init__(self):
        super().__init__()

        # Инициализируем таблицу контактов
        self.contacts = pd.DataFrame(
            columns=['Name', 'Phone', 'Birthdate', 'Address', 'Email', 'Comment', 'Group', 'Favorite', 'Photo Path'])

        # Инициализируем пользовательский интерфейс
        self.init_ui()

    def init_ui(self):
        # Создаем элементы интерфейса
        self.name_label = QLabel('Фамилия Имя Отчество:')
        self.name_entry = QLineEdit()
        self.phone_label = QLabel('Номер телефона:')
        self.phone_entry = QLineEdit()
        self.birthdate_label = QLabel('Дата рождения:')
        self.birthdate_entry = QLineEdit()
        self.address_label = QLabel('Адрес проживания:')
        self.address_entry = QLineEdit()
        self.email_label = QLabel('Email адрес:')
        self.email_entry = QLineEdit()
        self.comment_label = QLabel('Комментарий:')
        self.comment_entry = QLineEdit()

        self.group_button = QPushButton('Выбрать группу')
        self.favorite_button = QPushButton('★ Избранное')
        self.share_button = QPushButton('🔗 Поделиться')
        self.edit_button = QPushButton('✎ Редактировать')
        self.photo_button = QPushButton('📸 Добавить фото')
        self.add_button = QPushButton('+ Добавить контакт')

        # Создаем таблицу для отображения контактов
        self.contact_table = QTableWidget()
        self.contact_table.setColumnCount(len(self.contacts.columns))
        self.contact_table.setHorizontalHeaderLabels(self.contacts.columns)

        self.delete_button = QPushButton('× Удалить контакт')
        self.load_button = QPushButton('🢁 Загрузить из файла')
        self.sort_button = QPushButton('⇕ Сортировать по группам')

        # Создаем кнопки для сохранения и загрузки контактов
        self.save_button = QPushButton('Сохранить в файл')
        self.load_excel_button = QPushButton('Загрузить из файла (Excel)')
        self.load_word_button = QPushButton('Загрузить из файла (Word)')

        # Размещаем элементы интерфейса в компоновке
        vbox = QVBoxLayout()
        vbox.addWidget(self.name_label)
        vbox.addWidget(self.name_entry)
        vbox.addWidget(self.phone_label)
        vbox.addWidget(self.phone_entry)
        vbox.addWidget(self.birthdate_label)
        vbox.addWidget(self.birthdate_entry)
        vbox.addWidget(self.address_label)
        vbox.addWidget(self.address_entry)
        vbox.addWidget(self.email_label)
        vbox.addWidget(self.email_entry)
        vbox.addWidget(self.comment_label)
        vbox.addWidget(self.comment_entry)
        vbox.addWidget(self.group_button)
        vbox.addWidget(self.favorite_button)
        vbox.addWidget(self.share_button)
        vbox.addWidget(self.edit_button)
        vbox.addWidget(self.photo_button)
        vbox.addWidget(self.add_button)
        vbox.addWidget(self.contact_table)
        vbox.addWidget(self.delete_button)
        vbox.addWidget(self.load_button)
        vbox.addWidget(self.sort_button)
        vbox.addWidget(self.save_button)
        vbox.addWidget(self.load_excel_button)
        vbox.addWidget(self.load_word_button)

        # Назначаем компоновку виджету
        self.setLayout(vbox)

        # Подключаем обработчики событий
        self.add_button.clicked.connect(self.add_contact)
        self.delete_button.clicked.connect(self.delete_contact)
        self.load_button.clicked.connect(self.load_contacts)
        self.sort_button.clicked.connect(self.sort_contacts)
        self.group_button.clicked.connect(self.choose_group)
        self.favorite_button.clicked.connect(self.toggle_favorite)
        self.share_button.clicked.connect(self.share_contact)
        self.edit_button.clicked.connect(self.edit_contact)
        self.photo_button.clicked.connect(self.add_photo)
        self.save_button.clicked.connect(self.save_contacts)

    def add_photo(self):
        # Добавляем фото к выбранному контакту
        selected_item = self.contact_table.currentItem()
        if selected_item:
            row = selected_item.row()
            file_path, _ = QFileDialog.getOpenFileName(self, 'Выбрать изображение', '',
                                                       'Images (*.png *.jpg *.bmp *.gif *.jpeg)')
            if file_path:
                # Обновляем путь к фото в данных контакта
                self.contacts.at[row, 'Photo Path'] = file_path
                self.update_contact_table()

    def add_contact(self):
        # Добавляем новый контакт
        name = self.name_entry.text()
        phone = self.phone_entry.text()
        birthdate = self.birthdate_entry.text()
        address = self.address_entry.text()
        email = self.email_entry.text()
        comment = self.comment_entry.text()
        group = self.group_button.text()
        favorite = '★' if self.favorite_button.isChecked() else ''
        photo_path = None

        if name:
            new_contact = pd.DataFrame({'Name': [name],
                                        'Phone': [phone],
                                        'Birthdate': [birthdate],
                                        'Address': [address],
                                        'Email': [email],
                                        'Comment': [comment],
                                        'Group': [group],
                                        'Favorite': [favorite],
                                        'Photo Path': [photo_path]})

            self.contacts = pd.concat([self.contacts, new_contact], ignore_index=True)
            self.update_contact_table()

            # Очищаем поля ввода после добавления контакта
            self.clear_input_fields()

    def delete_contact(self):
        # Удаляем выбранный контакт
        selected_item = self.contact_table.currentItem()
        if selected_item:
            row = selected_item.row()
            self.contacts = self.contacts.drop(index=row)
            self.update_contact_table()

    def save_contacts(self):
        # Сохраняем контакты в файл
        file_path, _ = QFileDialog.getSaveFileName(self, 'Сохранить файл', '', 'All files (*)')

        if file_path:
            # Определяем расширение файла
            file_extension = file_path.split('.')[-1].lower()

            if file_extension == 'json':
                self.save_contacts_json(file_path)
            elif file_extension in ['xlsx', 'xls']:
                self.save_contacts_excel(file_path)
            elif file_extension in ['doc', 'docx']:
                self.save_contacts_word(file_path)

    def save_contacts_json(self, file_path):
        # Сохраняем контакты в формате JSON
        self.contacts.to_json(file_path, orient='records', lines=True)

    def save_contacts_excel(self, file_path):
        # Сохраняем контакты в формате Excel
        self.contacts.to_excel(file_path, index=False)

    def save_contacts_word(self, file_path):
        # Сохраняем контакты в формате Word
        doc = Document()

        # Добавляем заголовок
        doc.add_heading('Contact List', level=1)

        # Добавляем контакты
        for _, contact in self.contacts.iterrows():
            doc.add_paragraph(f"Name: {contact['Name']}")
            doc.add_paragraph(f"Phone: {contact['Phone']}")
            doc.add_paragraph(f"Birthdate: {contact['Birthdate']}")
            doc.add_paragraph(f"Address: {contact['Address']}")
            doc.add_paragraph(f"Email: {contact['Email']}")
            doc.add_paragraph(f"Comment: {contact['Comment']}")
            doc.add_paragraph(f"Group: {contact['Group']}")
            doc.add_paragraph(f"Favorite: {contact['Favorite']}")
            doc.add_paragraph(f"Photo Path: {contact['Photo Path']}")

            # Добавляем пустую строку между контактами
            doc.add_paragraph()

        doc.save(file_path)

    def load_contacts(self):
        # Загружаем контакты из файла
        file_path, _ = QFileDialog.getOpenFileName(self, 'Выберите файл', '', 'All files (*)')

        if file_path:
            # Определяем расширение файла
            file_extension = file_path.split('.')[-1].lower()

            if file_extension == 'json':
                self.load_contacts_json(file_path)
            elif file_extension in ['xlsx', 'xls']:
                self.load_contacts_excel(file_path)
            elif file_extension in ['doc', 'docx']:
                self.load_contacts_word(file_path)

    def load_contacts_json(self, file_path):
        # Загружаем контакты из файла JSON
        self.contacts = pd.read_json(file_path, orient='records', lines=True)
        self.update_contact_table()

    def load_contacts_excel(self, file_path):
        # Загружаем контакты из файла Excel
        self.contacts = pd.read_excel(file_path)
        self.update_contact_table()

    def load_contacts_word(self, file_path):
        # Загружаем контакты из файла Word
        doc = Document(file_path)

        # Очищаем текущие контакты
        self.contacts = pd.DataFrame(
            columns=['Name', 'Phone', 'Birthdate', 'Address', 'Email', 'Comment', 'Group', 'Favorite', 'Photo Path'])

        # Загружаем контакты из файла
        for paragraph in doc.paragraphs:
            if paragraph.text.startswith('Name:'):
                contact_info = {
                    'Name': paragraph.text.split(': ')[1],
                    'Phone': doc.paragraphs.pop(0).text.split(': ')[1],
                    'Birthdate': doc.paragraphs.pop(0).text.split(': ')[1],
                    'Address': doc.paragraphs.pop(0).text.split(': ')[1],
                    'Email': doc.paragraphs.pop(0).text.split(': ')[1],
                    'Comment': doc.paragraphs.pop(0).text.split(': ')[1],
                    'Group': doc.paragraphs.pop(0).text.split(': ')[1],
                    'Favorite': doc.paragraphs.pop(0).text.split(': ')[1],
                    'Photo Path': doc.paragraphs.pop(0).text.split(': ')[1]
                }
                self.contacts = pd.concat([self.contacts, pd.DataFrame([contact_info])], ignore_index=True)

        self.update_contact_table()

    def sort_contacts(self):
        # Сортируем контакты по группам
        self.contacts.sort_values(by='Group', inplace=True)
        self.update_contact_table()

    def choose_group(self):
        # Выбираем группу для контакта
        group, _ = QInputDialog.getText(self, 'Выбор группы', 'Введите название группы:')
        if group:
            self.group_button.setText(group)

    def toggle_favorite(self):
        # Переключаем состояние избранного
        if self.favorite_button.text() == '★':
            self.favorite_button.setText('')
        else:
            self.favorite_button.setText('★')

    def share_contact(self):
        # Действия при "поделиться" контактом
        selected_item = self.contact_table.currentItem()
        if selected_item:
            row = selected_item.row()
            contact_info = self.contacts.iloc[row]
            # Здесь может быть код для "поделиться" контактом, например, открытие почтового клиента

    def edit_contact(self):
        # Редактируем выбранный контакт
        selected_item = self.contact_table.currentItem()
        if selected_item:
            row = selected_item.row()
            contact_info = self.contacts.iloc[row]

            # Здесь вы можете использовать информацию из contact_info
            # для открытия окна редактирования контакта с предварительным заполнением полей.

    def update_contact_table(self):
        # Обновляем отображение контактов в таблице
        self.contact_table.setRowCount(0)
        for index, contact in self.contacts.iterrows():
            self.contact_table.insertRow(index)
            for col_index, value in enumerate(contact):
                self.contact_table.setItem(index, col_index, QTableWidgetItem(str(value)))

    def clear_input_fields(self):
        # Очищаем поля ввода после добавления контакта
        self.name_entry.clear()
        self.phone_entry.clear()
        self.birthdate_entry.clear()
        self.address_entry.clear()
        self.email_entry.clear()
        self.comment_entry.clear()


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        window = ContactListApp()
        window.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"An exception occurred: {e}")
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Инициализация библиотек:
'''
import sys
import pandas as pd
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit,
                             QPushButton, QLabel, QFileDialog, QInputDialog, QTableWidget, QTableWidgetItem)
from PyQt6.QtGui import QPixmap
from PIL import Image
'''
sys - стандартный модуль Python для взаимодействия с интерпретатором Python.
pandas - используется для работы с данными в виде таблицы (DataFrame).
PyQt6 - библиотека для создания графических пользовательских интерфейсов.
PIL.Image - модуль для обработки изображений.
'''
'''
Класс ContactListApp:
'''
class ContactListApp(QWidget):
    def __init__(self):
        super().__init__()
        self.contacts = pd.DataFrame(columns=['Name', 'Phone', 'Birthdate', 'Address',
                                              'Email', 'Comment', 'Group', 'Favorite', 'Photo Path'])
        self.init_ui()
'''
Создается класс ContactListApp, который наследуется от QWidget.
В конструкторе инициализируется пустая таблица контактов с помощью библиотеки pandas.
'''
'''
Метод init_ui:
'''
def init_ui(self):
    # ... (создание виджетов)
    self.setLayout(vbox)
    self.add_button.clicked.connect(self.add_contact)
    self.delete_button.clicked.connect(self.delete_contact)
    # ... (подключение обработчиков событий)
'''
Создается метод init_ui, который отвечает за создание элементов пользовательского интерфейса
 и их размещение в компоновке.
Создаются виджеты (метки, поля ввода, кнопки, таблица) и размещаются в компоновке vbox.
Устанавливаются обработчики событий для кнопок.
'''
'''
Методы для действий пользователя:
'''
'''
add_photo: позволяет добавить фото к выбранному контакту.
add_contact: добавляет новый контакт на основе введенных данных.
delete_contact: удаляет выбранный контакт.
save_contacts: сохраняет контакты в файл разного формата (JSON, Excel, Word).
load_contacts: загружает контакты из файла.
sort_contacts: сортирует контакты по группам.
choose_group: позволяет выбрать группу для контакта.
toggle_favorite: переключает состояние избранного.
share_contact: выполняет действия при "поделиться" контактом.
edit_contact: редактирует выбранный контакт.
'''
'''
Метод update_contact_table:
'''
def update_contact_table(self):
    self.contact_table.setRowCount(0)
    for index, contact in self.contacts.iterrows():
        self.contact_table.insertRow(index)
        for col_index, value in enumerate(contact):
            self.contact_table.setItem(index, col_index, QTableWidgetItem(str(value)))
'''
Метод update_contact_table обновляет отображение контактов в таблице QTableWidget.
Для этого он очищает таблицу (setRowCount(0)) и затем добавляет строки с контактами из DataFrame.
'''
'''
Метод clear_input_fields:
'''
def clear_input_fields(self):
    self.name_entry.clear()
    self.phone_entry.clear()
    self.birthdate_entry.clear()
    self.address_entry.clear()
    self.email_entry.clear()
    self.comment_entry.clear()
'''
clear_input_fields очищает поля ввода после добавления контакта.
'''
'''
Блок выполнения приложения:
'''
if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        window = ContactListApp()
        window.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"An exception occurred: {e}")
'''
Если код выполняется как самостоятельный скрипт, создается объект приложения (QApplication),
 создается и отображается главное окно приложения, и запускается цикл событий (app.exec()).
В случае возникновения исключения, оно будет выведено в консоль.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~