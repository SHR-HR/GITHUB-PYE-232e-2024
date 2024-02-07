from tkinter import Tk, Label, Button

def change_label(tk_label: Label) -> None:
    tk_label.configure(text="Привет")
    tk_label.configure(bg="red")

def change_back_label(tk_label: Label) -> None:
    tk_label.configure(text="Hello 123")
    tk_label.configure(bg="#0487D9")

def change_btn_state(state):
    if state == 'disabled':
        button["state"] = "disabled"
    elif state == 'enabled':
        button["state"] = "normal"

def button_click_handler():
    change_label(hello_label)
    change_btn_state('disabled')
    window.after(3000, lambda: change_back_label(hello_label))
    window.after(3000, lambda: change_btn_state('enabled'))

# start init
window = Tk()
window.title("Kaлькyлятop")
window.geometry('650x250')

hello_label = Label(window, text="Hello 123", font=("Trajan pro", 50), bg="#0487D9", foreground="#333")
hello_label.grid(column=0, row=0)

goodbye_label = Label(window, text="Hello 123", font=("Trajan Pro", 50), bg="red")
goodbye_label.grid(column=0, row=1)

# Изменение вида кнопки
button = Button(window, text="Нажми меня", command=button_click_handler, relief="ridge", borderwidth=4, highlightthickness=2)
button.grid(column=0, row=2)

window.mainloop()
