import tkinter as tk

class MobileCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Mobile Calculator")
        self.root.geometry("330x480")
        self.root.configure(bg="#f0f0f0")

        self.equation = ""
        self.input_text = tk.StringVar()

        # Entry Field
        self.entry = tk.Entry(root, textvariable=self.input_text, font=("Arial", 24), bd=5, relief="flat", 
                              bg="#ffffff", fg="#333333", justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, padx=10, pady=15, sticky="nsew")

        # Buttons
        button_layout = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
            ('=', 5, 0)
        ]

        for text, row, col in button_layout:
            self.create_button(text, row, col)

    def create_button(self, text, row, col):
        button_style = {
            "font": ("Arial", 16, "bold"),
            "width": 5,
            "height": 2,
            "bd": 2,
            "relief": "ridge",
            "bg": "#ffffff" if text.isdigit() or text == "." else "#ff9f43",
            "fg": "#000000" if text.isdigit() or text == "." else "#ffffff",
            "activebackground": "#ff6f00",
            "activeforeground": "#ffffff",
        }
        if text == "=":
            button_style["bg"] = "#28a745"
            button_style["fg"] = "#ffffff"
            button_style["width"] = 24  # Make it larger
            button_style["height"] = 2
        
        btn = tk.Button(self.root, text=text, **button_style, command=lambda: self.on_button_click(text))
        btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew", columnspan=(4 if text == "=" else 1))

    def on_button_click(self, char):
        if char == "C":
            self.equation = ""
        elif char == "=":
            try:
                self.equation = str(eval(self.equation))
            except:
                self.equation = "Error"
        else:
            self.equation += char
        self.input_text.set(self.equation)

# Run the Calculator
if __name__ == "__main__":
    root = tk.Tk()
    calculator = MobileCalculator(root)
    root.mainloop()