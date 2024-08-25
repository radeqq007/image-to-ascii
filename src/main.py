import tkinter as tk
from tkinter import filedialog
import os
from converter import convert

def main():
  # window
  window = tk.Tk()
  window.title("Image to ASCII")
  window.geometry("650x400")
  window.configure(pady=10)

  file_name = tk.StringVar()
  file_path: str = ""
  output_size: int = 100

  output_path = tk.StringVar(value=os.getcwd())

  error_message = tk.StringVar()

  def image_to_ascii():
      update_size()

      error_message.set(convert(file_path, output_size, output_path.get()))

  # asks for new file and updates file_path and file_name
  def open_file():
    nonlocal file_path
    file_path = filedialog.askopenfilename()
    file_name.set(os.path.basename(file_path))



  def new_output_path():
    output_path.set(filedialog.askdirectory())


  def update_size(event = None):
      nonlocal output_size
      new_size = select_size.get()
      try:
          output_size = int(new_size)
      except ValueError:
          error_message.set("Please enter correct size.")

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
    font = "Helvetica 10 bold",
  )
  selected_file_label.pack(side="left")


  # displays current selected file
  selected_file = tk.Label(
    master = selected_file_frame,
    textvariable = file_name,
    font = "Helvetica 8",

  )
  selected_file.pack(side="right")

  select_size_frame = tk.Frame(
    master=window,
    
  )
  select_size_frame.pack(fill='x', padx=10, pady=10)

  select_size_label = tk.Label(
    master = select_size_frame,
    text = "Size: ",
    font = "Helvetica 10 bold",
  )
  select_size_label.pack(side="left")

  select_size = tk.Entry(
    master = select_size_frame,
    width = 35,
  )
  select_size.pack(side="left")


  # button that opens the file dialog
  select_output_path = tk.Button(
    master = window,
    text = "Select output path",
    width = 30,
    command = new_output_path,
  )
  select_output_path.pack()


  # frame to display current file
  selected_output_path_frame = tk.Frame(
    master=window,
    pady = 40
  )
  selected_output_path_frame.pack(fill='x', padx=10, pady=10)

  selected_output_path_label = tk.Label(
    master = selected_output_path_frame,
    text = "Output will be saved at: ",
    font = "Helvetica 10 bold",
  )
  selected_output_path_label.pack(side="left")


  selected_output_path = tk.Label(
    master = selected_output_path_frame,
    textvariable = output_path,
    font = "Helvetica 8",

  )
  selected_output_path.pack(side="right")


  convert_button = tk.Button(
    master = window,
    text = "Convert",
    width = 30,
    command = image_to_ascii,
  )
  convert_button.pack()

  error = tk.Label(
      master = window,
      fg = "red",
      font = "Helvetica 10",
      pady = 20,
      textvariable = error_message
  )
  error.pack()




  window.mainloop()


if __name__ == "__main__":
   main()