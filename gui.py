import tkinter as tk
from tkinter import filedialog
import os
from converter import convert


# window
window = tk.Tk()
window.title("Image to ASCII")
window.geometry("500x600")
window.configure(pady=10)

file_name = tk.Variable()
file_path: str = ""
output_size: int = 100


# updates file_path and file_name
def open_file():
  global file_path
  file_path = filedialog.askopenfilename()
  file_name.set(os.path.basename(file_path))

# used for updating the size when the input changes
def update_size(event=None):
    global output_size
    new_size = select_size.get()
    try:
        output_size = int(new_size)
    except ValueError:
        # TODO: handle this
        ...

# button that opens the file dialog
select_file = tk.Button(
  master = window,
  text = "Select file",
  width = 30,
  command = open_file,
)

select_file.pack()

# frame to display current file
selected_file_frame = tk.Frame(
  master=window,
)
selected_file_frame.pack(fill='x', padx=10, pady=10)

selected_file_label = tk.Label(
  master = selected_file_frame,
  text = "Selected file: ",
  font = "halvetica 10 bold",
)
selected_file_label.pack(side="left")


# displays current selected file
selected_file = tk.Label(
  master = selected_file_frame,
  textvariable = file_name,
  font = "halvetica 8",

)
selected_file.pack(side="right")

select_size_frame = tk.Frame(
  master=window,
  
)
select_size_frame.pack(fill='x', padx=10, pady=10)

select_size_label = tk.Label(
  master = select_size_frame,
  text = "Size: ",
  font = "halvetica 10 bold",
)
select_size_label.pack(side="left")

select_size = tk.Entry(
  master = select_size_frame,
  width = 35,
)
select_size.pack()

select_size.bind("<Return>", update_size) # when input changes
select_size.bind("<FocusOut>", update_size) # when user clicks away



convert_button = tk.Button(
  master = window,
  text = "Convert",
  width = 30,
  command = lambda: convert(file_path, output_size),
)
convert_button.pack()





window.mainloop()
