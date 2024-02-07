from tkinter import *
from TkFunctions import *
from Buttons import *

#start init
window = Tk()
window.title("Калькулятор")

window.geometry('650x250')


hello_label = Label(window, text="Hello 123", font=("Trajan Pro", 50), bg="#0487D9", foreground="#333")
hello_label.grid(column=0, row=0)


goodbye_label = Label(window, text="Hello 123", font=("Trajan Pro", 50), bg="#eee")
goodbye_label.grid(column=0, row=1)

button = Button(window, text="Нажми меня", command=lambda: button_click_handler(hello_label, button), height=2, width=20)
button.grid(column=0, row=3)

#end init
window.mainloop()

