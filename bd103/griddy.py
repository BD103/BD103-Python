from tkinter import *
from tkinter import ttk

ttkWidgets = ["Button", "Checkbutton", "Entry", "Frame", "Label", "LabelFrame", "Menubutton", "PanedWindow", "Radiobutton", "Scale", "Scrollbar", "Spinbox", "Combobox", "Notebook", "Progressbar", "Separator", "Sizegrip", "Treeview"] # ttk only starting at combobox

def runProgram(path):
  grid = parseCSV(path)
  code = createCode(grid)
  root = Tk()
  exec(code)

def parseCSV(path):
  f = open(path, "rt")
  file = f.read()
  f.close()
  file = file.splitlines()
  grid = []
  for i in file:
    grid.append(i.split(","))
  return grid

def createCode(grid):
  heightOn = 0
  widthOn = 0
  code = ""
  for i in grid:
    for ii in i:
      tempii = ii.split("|")
      code += tempii[0].capitalize() + "(root, text=\"" + str(tempii[1:len(tempii)]).strip("[]'',") + "\").grid(column=" + str(widthOn) + ", row=" + str(heightOn) + ")\n"
      widthOn += 1
    heightOn += 1
    widthOn = 0
  return code