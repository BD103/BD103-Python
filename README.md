# BD103's Personal Coding Package
A bunch of random developer related functions and modules that I use.

![PyPI - Downloads](https://img.shields.io/pypi/dm/BD103) ![PyPI - License](https://img.shields.io/pypi/l/BD103) ![Lines of code](https://img.shields.io/tokei/lines/github/BD103/Package) ![GitHub commit activity](https://img.shields.io/github/commit-activity/y/BD103/Package) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Usage
`pip install bd103`

Go to [Github](https://github.com/BD103/Package/wiki) for the docs. :)

## Patch Notes
### 0.1.5
Fixed link in Usage section of `README.md`, as well as implemented some happiness. Added `requirements.txt`. Implemented Black formatting. Created `griddy.py` module. Check docs for more. Adjusted `__init__.py`. Importing bd103 no longer imports the contents of other modules. Added `bd103.help()` command in `__init__.py`.

### 0.1.4
Fixed link. Main website is no longer being hosted on [repl.it](https://repl.it), it is now being hosted through Github Pages. Updated some other links, as well as put package in a repository. You can find it [here](https://github.com/BD103/Package).

### 0.1.3
_Hopefully_ fixed the `color.py` module.

### 0.1.2
Fixed link in `README.md`.

### 0.1.1
**Panik.** I keep on making these silly mistakes in the `color.py` module, but _thankfully_ it should be fixed now. The `print(text, color)` function is renamed to `cprint(text, color)`.

### **0.1.0**
Fixed the `paint(color)` function in `color.py` module, as it refered to the color print function, not base print.

We are now in the Beta stage. Yay! :7

### 0.0.10
Small adjustment, made the delay between printing characters in the `scroll.py` module customizable. Also made a `clear.py` module, that clears the console screen.

### 0.0.9
Created the `scroll.py` module, as well as adjusted `__init__.py` to import functions from modules, not just the modules themselves.

### 0.0.8
As `0.0.7` failed to fix `engine/textdump.py`, we finally found and fixed the issue. :P

### 0.0.7
Fixed extra `"` in `engine/textdump.py`. Updated `0.0.6` description.

### 0.0.6
Edited 0.0.3 description of `README.md` to fix recurrent module creation. Created a comment at the top of each module that says it's part of the package. Removed color variables, as they are only handy for local modules. Fixed `engine/textdump.py` trying to save to a non-existant folder.

### 0.0.5
Edited `README.md` to fix spacing issues. Made the `engine` sub-module. Created `engine/textdump.py`.

### 0.0.4
Fixed `LICENSE`.

### 0.0.3
Updated short description. Added `__all__` variable in `__init__.py`. Updated `README.md` to have full module names. Renamed `color()` function to `print()`. Updated 0.0.1 description. Added `load.py` module. Created the `parser.py` module.
```python
''' Parser '''
bd103.parser.grid(path) # Loads a text file and creates a list. Each item is a sepperate line of the file. Returns the list (array)
bd103.parser.space(text, identifier=" ") # Parses given string and returns an array. Each item is sepperated by spaces. "hi there" would return ["hi", "there"]
''' Load Bar '''
bd103.load.load(length=100) # Automatically makes a useless loading bar
bd103.load.loadbar(value, length=100) # Allows you to manually create a load bar that syncs with data.
```

### 0.0.2
Emptied `__init__.py` to fix error. Updated `setup.py` and redid `README.md`.

### 0.0.1
Initial package. Contains a basic color formatting module.
```python
''' Functions '''
bd103.color.print(text, color) # Prints with text then resets formatting
bd103.color.paint(color) # Sets color permanently until reset

''' Colors '''
reset = "reset
red = "red"
yellow = "yellow"
green = "green"
cyan = "cyan"
blue = "blue"
magenta = "magenta"
black = "black"
white = "white"
```
