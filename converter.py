from PIL import Image
from math import floor

def image_to_ascii():
  output: str = ""
  fname: str = "a"


  # TODO: handle the possibility of file not existing
  i = Image.open(f"./images/{fname}.png")

  width, height = (100, 100)

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


  i.save(f"./{fname}.png")

  with open("output.txt", "w") as f:
    f.write(output)