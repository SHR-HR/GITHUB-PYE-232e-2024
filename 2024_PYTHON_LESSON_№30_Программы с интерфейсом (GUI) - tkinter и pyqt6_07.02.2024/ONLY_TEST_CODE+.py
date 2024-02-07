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
