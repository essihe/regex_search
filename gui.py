import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import scrolledtext
import os
from os import path
import sys
from haku import regex_search
import re

from custom import CustomText

window = Tk()
window.title("GUI")
window.geometry('800x600')	

class Gui:
	def __init__(self):	
		
		lbl = Label(window, text="Search for a file ->")
		lbl.grid(column=0, row=0)

		self.txt1 = Entry(window, width=10)
		self.txt1.grid(column=0, row=3)

		self.txt = CustomText(window, width=80, height=30)
		self.txt.tag_configure('red', foreground='#ff0000')
		self.txt.grid(column=0, row=2)

		btn1 = Button(window, text='Regex search', command=self.search)
		btn1.grid(column=2, row=3)

		btn = Button(window, text='Open', command=self.openfile)
		btn.grid(column=2, row=0)



	def openfile(self):
		self.file_path = filedialog.askopenfilename()
		with open(self.file_path, 'r') as f:
			self.txt.insert(INSERT, f.read())


		
	def search(self):
		self.txt.highlight_pattern(self.txt1.get(), 'red', regexp=True)
		
			
gui = Gui()
window.mainloop()

	
