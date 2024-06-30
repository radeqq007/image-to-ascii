from PIL import Image
import math

def main():
  fname = "cat"

  # TODO: handle the possibility of file not existing
  i = Image.open(f"./images/{fname}.png")

  width, height = (100, 100)

  i.thumbnail((width, height))

  i.thumbnail((width, height))
  i = i.convert("L")

  data = i.getdata()

  # TODO: add more characters because this is stupid
  # characters, from lightest to darkest
  chars = " .º•ø:;▒'\"^-=(]+*O©%&$@#8▓█"

  # this sucks
  for index, pixel in enumerate(data):
    #print(f"index: {index}, pixel: {pixel} data[pixel]: {data[pixel]} / 10", end="   ")
    brightness_index   = math.floor(data[pixel]/10)
    #print(f"Brightness: {brightness_index}")
    print(chars[brightness_index], end="")

    # Not sure if this is working or not
    if (index + 1 )% width == 0:
      print("")


  i.save(f"./{fname}.png")

if __name__ == "__main__":
  main()