import tkinter as tk
from tkinter import filedialog
from pscript import py2js

def convert_to_js():
    python_code = code_text.get("1.0", tk.END)
    js_code = py2js(python_code)
    js_output.delete("1.0", tk.END)
    js_output.insert(tk.END, f"Javascript Code:\n{js_code}")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
    if file_path:
        with open(file_path, "r") as file:
            code_text.delete("1.0", tk.END)
            code_text.insert(tk.END, file.read())

# GUI Setup
root = tk.Tk()
root.title("Python to JavaScript Converter")

# Text Widget for Python Code
code_text = tk.Text(root, wrap=tk.WORD, width=50, height=10)
code_text.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Button to Convert
convert_button = tk.Button(root, text="Convert to JavaScript", command=convert_to_js)
convert_button.grid(row=1, column=0, padx=10, pady=10)

# Button to Browse Python File
browse_button = tk.Button(root, text="Browse Python File", command=browse_file)
browse_button.grid(row=1, column=1, padx=10, pady=10)

# Text Widget for JavaScript Code
js_output = tk.Text(root, wrap=tk.WORD, width=50, height=10)
js_output.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

root.mainloop()
