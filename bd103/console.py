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
    list = {
        "reset": "\033[0m",
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
    }

    def cprint(text, color):
        if color in list:
            full_color_cmd = "full_color = color.list." + color
            exec(full_color_cmd)
        else:
            full_color = color.list.reset
        print(full_color + text + color.list.reset)

    def paint(color):
        if color in list:
            full_color_cmd = "full_color = color.list." + color
            exec(full_color_cmd)
        else:
            full_color = color.list.reset
        print(full_color, end="")


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
    # Also getting deprecated because its so simple
    def grid(text):
        return text.split("\n")


"""
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
"""
