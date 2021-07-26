class Hex(object):
  key = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "a": 10,
    "b": 11,
    "c": 12,
    "d": 13,
    "e": 14,
    "f": 15
  }

  def __init__(self, string: str):
    self.og = string.lower();

  def _convert(self, char: str) -> int:
    return self.key.get(char)

  def to_decimal(self) -> int:
    sum = self._convert(self.og[0])
    
    if len(self.og) == 1:
      return sum
    
    for i in self.og[1:]:
      sum *= 16
      sum += self._convert(i)
    
    return sum


if __name__ == "__main__":
  print(Hex("e4").to_decimal())
