import unittest
import pytest

import bd103


class Init(unittest.TestCase):
    pass


import bd103.console


class Console(unittest.TestCase):
    def test_loadbar_10(self):
        assert bd103.console.load.loadbar(10) == "[#         ]"

    def test_loadbar_1(self):
        assert bd103.console.load.loadbar(1) == "[          ]"

    def test_loadbar_length_10(self):
        assert bd103.console.load.loadbar(5, length=10) == "[#####     ]"

    def test_loadbar_length_1(self):
        assert bd103.console.load.loadbar(1, length=1) == "[##########]"

    def test_loadbar_overflow(self):
        assert bd103.console.load.loadbar(2, length=1) == "[##########]"

    def test_grid_with_escape(self):
        result = bd103.console.parser.grid("Hi there\nmy friend")
        expected = ["Hi there", "my friend"]
        assert result == expected

    def test_grid_with_newline(self):
        string = """
Hello there.
How are you?    
"""
        result = bd103.console.parser.grid(string.strip())
        expected = ["Hello there.", "How are you?"]
        assert result == expected


import bd103.griddy


class Griddy(unittest.TestCase):
    def test_parseCSV(self):
        result = bd103.griddy.parseCSV("hey,there\nuwu")
        expected = [["hey", "there"], ["uwu"]]
        assert result == expected

    def test_createCode(self):
        result = bd103.griddy.createCode(
            [["label|uwu", "button|ok"], ["button|no kay"]]
        )
        expected = """
Label(root, text="uwu").grid(column=0, row=0)
Button(root, text="ok").grid(column=1, row=0)
Button(root, text="no kay").grid(column=0, row=1)
"""
        assert result.strip() == expected.strip()
