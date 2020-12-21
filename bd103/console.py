import os
import time

def clear():
  os.system("clear")

def scroll(text, delay=0.03):
    for i in text:
      print(i, end="", flush=True)
      time.sleep(delay)
    print()

class color:
  def cprint(text, color):
    if color == "reset":
        print("\u001b[0m" + text)
    elif color == "red":
        print("\u001b[31m" + text + "\u001b[0m")
    elif color == "yellow":
        print("\u001b[33m" + text + "\u001b[0m")
    elif color == "green":
        print("\u001b[32m" + text + "\u001b[0m")
    elif color == "cyan":
        print("\u001b[36m" + text + "\u001b[0m")
    elif color == "blue":
        print("\u001b[34m" + text + "\u001b[0m")
    elif color == "magenta":
        print("\u001b[35m" + text + "\u001b[0m")
    elif color == "black":
        print("\u001b[30m" + text + "\u001b[0m")
    elif color == "white":
        print("\u001b[37m" + text + "\u001b[0m")


  def paint(color):
    if color == "reset":
        color.cprint("", "reset")
    elif color == "red":
        color.cprint("", "red")
    elif color == "yellow":
        color.cprint("", "yellow")
    elif color == "green":
        color.cprint("", "green")
    elif color == "cyan":
        color.cprint("", "cyan")
    elif color == "blue":
        color.cprint("", "blue")
    elif color == "magenta":
        color.cprint("", "magenta")
    elif color == "black":
        color.cprint("", "black")
    elif color == "white":
        color.cprint("", "white")

class load:
  def loadbar(value, length=100):
    sample = "[{}]"
    if value <= length:
      bars = round(value / length * 10)
    elif value > length:
      bars = round(length / length * 10)
    hash = ""
    for i in range(0, bars):
        hash += "#"
    hash += (10 - len(hash)) * " "
    return sample.format(hash)


  def load(length=100):
    i = 0
    while i <= length:
        print(load.loadbar(i, length=length), end="\r")
        i += 1
        time.sleep(0.1)
    print()

class parser:
  def grid(path):
    final = []
    f = open(path, "r")
    for i in f:
        final.append(i)
    f.close()
    return final

'''
Deprecated, use split() function
  def space(text, identifier=" "):
    tempCmdSection = ""
    returnArray = []
    i2 = 0
    for i in text:
        if text[i2] != identifier:
            tempCmdSection = tempCmdSection + text[i2]
        else:
            returnArray.append(tempCmdSection)
            tempCmdSection = ""
        i2 += 1
    returnArray.append(tempCmdSection)
    return returnArray
'''