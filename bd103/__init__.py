import platform
if platform.system() == "Windows":
    from colorama import init as colorinit
    colorinit()

def help():
    print("\033[94m", end="")
    print("BD103 Python Package\n")
    print("X~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~X")
    print("| Github:                                  |")
    print("|    https://github.com/BD103/Package      |")
    print("| Docs:                                    |")
    print("|    https://github.com/BD103/Package/wiki |")
    print("| PyPI:                                    |")
    print("|    https://pypi.org/project/BD103        |")
    print("| Website:                                 |")
    print("|    https://bd103.github.io               |")
    print("X~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~X\n")
    print("\033[0m", end="")
