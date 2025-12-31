import tkinter as tk
from tkinter import *
import math
class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("420x600")
        self.root.resizable(False, False)
        self.expression = ""
        self.input_text = StringVar()
        self.create_display()
        self.create_buttons()
        self.bind_keys()
    def create_display(self):
        entry = Entry(self.root, font=("Arial", 22), textvariable=self.input_text,
                      bd=10, insertwidth=4, bg="#000", fg="#0f0", justify="right")
        entry.grid(row=0, column=0, columnspan=5, ipadx=8, ipady=25)
    def btn_click(self, value):
        self.expression += str(value)
        self.input_text.set(self.expression)
    def clear(self):
        self.expression = ""
        self.input_text.set("")
    def delete(self):
        self.expression = self.expression[:-1]
        self.input_text.set(self.expression)
    def equal(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except:
            self.input_text.set("Error")
            self.expression = ""
    def bind_keys(self):
        self.root.bind("<Return>", lambda event: self.equal())
        self.root.bind("<BackSpace>", lambda event: self.delete())
    def create_buttons(self):
        buttons = [
            ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3), ("C",1,4),
            ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3), ("⌫",2,4),
            ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3), ("(",3,4),
            ("0",4,0), (".",4,1), ("=",4,2), ("+",4,3), (")",4,4),
            ("sin",5,0), ("cos",5,1), ("tan",5,2), ("log",5,3), ("sqrt",5,4),
            ("π",6,0), ("e",6,1), ("x²",6,2), ("x^y",6,3), ("fact",6,4),
        ]
        for (text, r, c) in buttons:
            Button(self.root, text=text, width=8, height=3,
                   font=("Arial", 12),
                   command=lambda txt=text: self.process(txt)
                   ).grid(row=r, column=c, padx=3, pady=3)
    def process(self, btn):
        if btn == "C":
            self.clear()
        elif btn == "⌫":
            self.delete()
        elif btn == "=":
            self.equal()
        elif btn == "sin":
            self.btn_click("math.sin(")
        elif btn == "cos":
            self.btn_click("math.cos(")
        elif btn == "tan":
            self.btn_click("math.tan(")
        elif btn == "log":
            self.btn_click("math.log10(")
        elif btn == "sqrt":
            self.btn_click("math.sqrt(")
        elif btn == "π":
            self.btn_click(str(math.pi))
        elif btn == "e":
            self.btn_click(str(math.e))
        elif btn == "x²":
            self.btn_click("**2")
        elif btn == "x^y":
            self.btn_click("**")
        elif btn == "fact":
            self.btn_click("math.factorial(")
        else:
            self.btn_click(btn)
root = tk.Tk()
calculator = ScientificCalculator(root)
root.mainloop()
