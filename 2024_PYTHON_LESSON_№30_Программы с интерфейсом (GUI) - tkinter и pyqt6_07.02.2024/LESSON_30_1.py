import tkinter as tk
from tkinter import ttk

def on_click(button_value):
    current = entry_var.get()
    
    if button_value == "=":
        try:
            result = eval(current)
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif button_value == "C":
        entry_var.set("")
    else:
        entry_var.set(current + button_value)

def on_mode_change(event):
    selected_mode = mode_var.get()
    print(f"Selected mode: {selected_mode}")
    # Добавьте здесь логику для изменения режима калькулятора, если нужно

# Создание главного окна
window = tk.Tk()
window.title("Красивый Калькулятор")

# Переменные для хранения введенных данных и выбранного режима
entry_var = tk.StringVar()
mode_var = tk.StringVar()

# Поле ввода
entry = ttk.Entry(window, textvariable=entry_var, font=("Arial", 14), justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Кнопки для первого ряда
buttons_row1 = ["7", "8", "9", "/"]
for col, button in enumerate(buttons_row1):
    ttk.Button(window, text=button, command=lambda b=button: on_click(b)).grid(row=1, column=col, sticky="nsew", padx=5, pady=5)

# Кнопки для второго ряда
buttons_row2 = ["4", "5", "6", "*"]
for col, button in enumerate(buttons_row2):
    ttk.Button(window, text=button, command=lambda b=button: on_click(b)).grid(row=2, column=col, sticky="nsew", padx=5, pady=5)

# Кнопки для третьего ряда
buttons_row3 = ["1", "2", "3", "-"]
for col, button in enumerate(buttons_row3):
    ttk.Button(window, text=button, command=lambda b=button: on_click(b)).grid(row=3, column=col, sticky="nsew", padx=5, pady=5)

# Кнопки для четвертого ряда
buttons_row4 = ["0", ".", "=", "+"]
for col, button in enumerate(buttons_row4):
    ttk.Button(window, text=button, command=lambda b=button: on_click(b)).grid(row=4, column=col, sticky="nsew", padx=5, pady=5)

# Кнопка "C" для очистки
ttk.Button(window, text="C", command=lambda: on_click("C")).grid(row=5, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# Добавление эмодзи в качестве иконки
emoji_label = tk.Label(window, text="🧮", font=("Arial", 20))
emoji_label.grid(row=0, column=4, rowspan=5, sticky="nsew")

# ComboBox для выбора режима
modes = ["Обычный", "Научный", "Продвинутый"]
mode_combo = ttk.Combobox(window, textvariable=mode_var, values=modes, state="readonly")
mode_combo.grid(row=6, column=0, columnspan=4, sticky="nsew", pady=5)
mode_combo.bind("<<ComboboxSelected>>", on_mode_change)

# Установка параметров расширения строк и столбцов
for i in range(7):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)

# Запуск главного цикла
window.mainloop()
