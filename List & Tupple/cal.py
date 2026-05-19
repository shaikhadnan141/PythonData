import tkinter as tk
import math

# Create main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("1980x1080")
root.resizable(False, False)

# Entry box for display
entry = tk.Entry(root, width=20, font=('Arial', 24), borderwidth=5, relief='ridge', justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Function to update expression
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            expression = entry.get().replace("√", "math.sqrt").replace("^", "**")
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Button labels
buttons = [
    "7", "8", "9", "/", 
    "4", "5", "6", "*", 
    "1", "2", "3", "-", 
    "0", ".", "=", "+",
    "(", ")", "√", "^",
    "C"
]

# Create buttons dynamically
row, col = 1, 0
for btn_text in buttons:
    btn = tk.Button(root, text=btn_text, width=5, height=2, font=('Arial', 18))
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
