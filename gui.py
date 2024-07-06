import tkinter as tk
from tkinter import filedialog
import converter


# window
window = tk.Tk()
window.title("Image to ASCII")
window.geometry("500x600")

window.mainloop()

def open_file():
  file_path = filedialog.askopenfilename()
  print(file_path)

file_dir = tk.Button(
  master = window,
  text = "Select file",
  command = open_file
)

file_dir.pack()


