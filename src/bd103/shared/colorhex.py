from .hex import Hex


class ColorHex(object):
  def __init__(self, string: str):
    self.og = Hex.make_safe(string)

    self.red = None
    self.green = None
    self.blue = None

    self.convert()
    
  def convert(self):
    if len(self.og) == 3:
      self.red = Hex(self.og[0]).to_decimal() * 16
      self.green = Hex(self.og[1]).to_decimal() * 16
      self.blue = Hex(self.og[2]).to_decimal() * 16
    elif len(self.og) == 6:
      self.red = Hex(self.og[0:2]).to_decimal()
      self.green = Hex(self.og[2:4]).to_decimal()
      self.blue = Hex(self.og[4:6]).to_decimal()
    else:
      raise Exception("Invalid length of hex")
  
  def to_rgb(self) -> tuple:
    self.convert()
    return (self.red, self.green, self.blue)


if __name__ == "__main__":
  x = ColorHex("#0ff")
  print(x.og)
  print(x.to_rgb())
