import os

initpy = '''import json

functionformat = "def {funcname}():\\n"
textformat = "\\tprint(\\"{text}\\")\\n\\tinput()\\n"

f = open("engine/textdump.json", "rt")

textdump = json.loads(f.read())

f.close()

f = open("engine/text.py", "wt")
f.write("")
f.close()

f = open("engine/text.py", "at")

for i in textdump:
	function = ""
	text = ""
	function += functionformat.format(funcname = i)
	
	for ii in textdump[i]:
		text += textformat.format(text = ii)
	
	f.write(function + text)

f.close()'''

textdumpjson = '''{
  "key": [
    "Value 1",
    "Value 2"
  ],
  "functionname": [
    "Text being printed",
    "Text being printed after pressing return"
  ]
}'''
try:
  os.mkdir("engine")
except:
	pass

f = open("engine/__init__.py", "wt")
f.write(initpy)
f.close()

f = open("engine/textdump.json", "wt")
f.write(textdumpjson)
f.close()