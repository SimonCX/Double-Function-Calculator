import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        
        self.entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='solid')
        self.entry.grid(row=0, column=0, columnspan=4)
        
        self.current_entry = ""
        
        self.create_buttons()
        
    def create_buttons(self):
        button_texts = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            '0', '.', '=', '+'
        ]
        
        row = 1
        col = 0
        for text in button_texts:
            button = tk.Button(self.root, text=text, font=('Arial', 18), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10)
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        all_clear_button = tk.Button(self.root, text="AC", font=('Arial', 18), command=self.all_clear)
        all_clear_button.grid(row=row, column=0, padx=5, pady=5, ipadx=10, ipady=10)
        
        clear_entry_button = tk.Button(self.root, text="CE", font=('Arial', 18), command=self.clear_entry)
        clear_entry_button.grid(row=row, column=1, padx=5, pady=5, ipadx=10, ipady=10)
        
    def on_button_click(self, char):
        if char == '=':
            try:
                result = str(eval(self.current_entry))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
                self.current_entry = result
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        else:
            self.current_entry += str(char)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.current_entry)
    
    def all_clear(self):
        self.current_entry = ""
        self.entry.delete(0, tk.END)
    
    def clear_entry(self):
        self.current_entry = self.current_entry[:-1]
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.current_entry)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
    