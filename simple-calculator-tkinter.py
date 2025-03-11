import tkinter as tk

def cal():
    def on_button_click(value):
        """افزودن عدد یا عملگر به ورودی."""
        entry.insert(tk.END, value)

    def clear_entry():
        """پاک کردن ورودی."""
        entry.delete(0, tk.END)

    def calculate():
        """محاسبه نتیجه و نمایش آن."""
        try:
            result = eval(entry.get())
            label_result.config(text=f"Result: {result}")
        except Exception as e:
            label_result.config(text=f"Error: {e}")

    # تنظیم پنجره
    window = tk.Tk()
    window.title("Calculator")
    window.configure(bg="#d3d3d3")

    # ویجت‌های ورودی و نتیجه
    entry = tk.Entry(window, width=30)
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    label_result = tk.Label(window, text="Result: ", bg="#d3d3d3")
    label_result.grid(row=1, column=0, columnspan=4)

    # دکمه‌های اعداد و عملیات
    buttons = [
        ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
        ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
        ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
        ('0', 5, 0), ('.', 5, 1), ('+', 5, 2), ('=', 5, 3),
    ]

    for (text, row, col) in buttons:
        if text == '=':
            button = tk.Button(window, text=text, command=calculate)
        else:
            button = tk.Button(window, text=text, command=lambda t=text: on_button_click(t))
        button.grid(row=row, column=col, padx=5, pady=5)

    # دکمه‌های اضافی
    button_clear = tk.Button(window, text="C", command=clear_entry)
    button_clear.grid(row=6, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

    window.mainloop()

cal()