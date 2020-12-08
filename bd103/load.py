'''
Loadbar Module for the BD103 Package
'''
import time
import os

def loadbar(value, length=100):
	loading = "[{}]"
	bars = round(value / length * 10)
	hash = ""
	for i in range(0, bars):
		hash += "#"
	hash += (10 - len(hash)) * " "
	return loading.format(hash)

def load(length=100):
	i = 0
	while i <= length:
		print(loadbar(i, length=length), end="\r")
		i += 1
		time.sleep(0.1)
	print()