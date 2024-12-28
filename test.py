import tkinter as tk
from tkinter import messagebox

class Calculator:
  def __init__(self, root):
    self.root = root
    self.root.title("Calculator")
    self.root.geometry("400x500")
    self.expression = ""

    self.input_text = tk.StringVar()
    self.input_frame = tk.Frame(self.root, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
    self.input_frame.pack(side=tk.TOP)

    self.input_field = tk.Entry(self.input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
    self.input_field.grid(row=0, column=0)
    self.input_field.pack(ipady=10)

    self.buttons_frame = tk.Frame(self.root, width=400, height=450, bg="grey")
    self.buttons_frame.pack()

    self.create_buttons()

  def create_buttons(self):
    buttons = [
      '7', '8', '9', '/', 'C',
      '4', '5', '6', '*', 'CE',
      '1', '2', '3', '-', '=',
      '0', '.', '+'
    ]

    row = 0
    col = 0
    for button in buttons:
      if button == "=":
        btn = tk.Button(self.buttons_frame, text=button, fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: self.evaluate())
        btn.grid(row=row, column=col, columnspan=4)
      else:
        btn = tk.Button(self.buttons_frame, text=button, fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda button=button: self.click(button))
        btn.grid(row=row, column=col)
      col += 1
      if col > 4:
        col = 0
        row += 1

  def click(self, item):
    if item == 'C':
      self.expression = ""
    elif item == 'CE':
      self.expression = self.expression[:-1]
    else:
      self.expression += str(item)
    self.input_text.set(self.expression)

  def evaluate(self):
    try:
      result = str(eval(self.expression))
      self.input_text.set(result)
      self.expression = result
    except:
      messagebox.showerror("Error", "Invalid Input")
      self.expression = ""

if __name__ == "__main__":
  root = tk.Tk()
  calculator = Calculator(root)
  root.mainloop()