'''
Scrolling Text Module for the BD103 Package
'''

import time

def scroll(text, delay=0.03):
	i = 0
	length = len(text)
	output = ""
	while length != i:
		output = output+text[i]
		print(output, end="\r")
		i = i+1
		time.sleep(delay)
	print()