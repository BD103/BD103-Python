'''
Parser Module for the BD103 Package
'''

def grid(path):
	final = []
	f = open(path, "r")
	for i in f:
		final.append(i)
	f.close()
	return final

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