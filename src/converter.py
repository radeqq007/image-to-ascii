from PIL import Image
from math import floor
from os import path

def convert(file_path: str, size: int = 0, output_path: str = "./") -> str:
  if file_path == "":
    return "Select correct file."
  
  if size <= 0:
    return "Please select correct size."
  
  if not path.exists(file_path):
    return "File doesn't exist." 
  
  
  output: str = ""

  try:
    i = Image.open(file_path)
  except OSError:
    return "Please select correct file."
  
  width, height = (size, size)

  i.thumbnail((width, height))

  i.thumbnail((width, height))

  data = i.getdata()

  # characters, from darkest to lightest
  chars = "&@%#*+=-:. "

  for index, pixel in enumerate(data):
    brightness_index = floor(((pixel[0] + pixel[1] + pixel[2]) / 3) / 256 * (len(chars) - 1))
    output += chars[brightness_index] + " "

    if (index + 1 )% width == 0:
      output += "\n"


  with open(f"{output_path}/output.txt", "w") as f:
    f.write(output)

  return ""