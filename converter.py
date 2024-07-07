from PIL import Image
from math import floor
from os import path

def convert(file_path: str, size: int = 0) -> str:
  if file_path == "":
    return "Select correct file."
  
  if size <= 0:
    return "Please select correct size."
  
  if not path.exists(file_path):
    return "File doesn't exist." 
  
  
  output: str = ""


  i = Image.open(file_path)

  width, height = (size, size)

  i.thumbnail((width, height))

  i.thumbnail((width, height))
  i = i.convert("L")

  data = i.getdata()

  # TODO: add more characters because this is stupid
  # characters, from lightest to darkest
  chars = ".,:;ox%#@"

  # this sucks
  for index, pixel in enumerate(data):
    #print(f"index: {index}, pixel: {pixel} data[pixel]: {data[pixel]} / 10", end="   ")
    brightness_index = floor(pixel / 256 * (len(chars) - 1))
    #print(f"Brightness: {brightness_index}")
    output += chars[brightness_index] + " "

    # Not sure if this is working or not
    if (index + 1 )% width == 0:
      output += "\n"


  with open("output.txt", "w") as f:
    f.write(output)

  return ""