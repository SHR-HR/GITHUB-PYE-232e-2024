# библиотека

def change_label(tk_label, tk_btn) -> None:
    label_text = tk_label['text']
    label_bg = tk_label['background']

    tk_label.configure(text="Привет", bg="red")
    
    tk_label.after(1000, lambda: tk_label.configure(text=label_text, bg=label_bg))
    tk_btn.after(1000, lambda: change_btn_state(tk_btn, "enabled"))

def change_btn_state(tk_btn, state):
    if state == 'disabled':
        tk_btn["state"] = "disabled"
    elif state == 'enabled':
        tk_btn["state"] = "normal"

def button_click_handler(tk_label, tk_btn):
    change_label(tk_label, tk_btn)
    change_btn_state(tk_btn, 'disabled')