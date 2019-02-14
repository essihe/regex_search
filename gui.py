import tkinter as tk
from custom import CustomText

window = tk.Tk()
window.title("GUI")
window.geometry('800x600')	

class Gui:
	def __init__(self):	
		
		lbl = tk.Label(window, text="Search for a file ->")
		lbl.grid(column=0, row=0)

		self.matches = tk.Label(window)
		self.matches.grid(column=0, row=4)

		lbl2 = tk.Label(window, text="Type the pattern you want to search ↓")
		lbl2.grid(column=0, row=3)

		self.txt1 = tk.Entry(window, width=10)
		self.txt1.grid(column=0, row=4)

		self.txt = CustomText(window, width=80, height=30)
		self.txt.tag_configure('red', foreground='#ff0000')
		self.txt.grid(column=0, row=2)

		btn1 = tk.Button(window, text='Regex search', command=self.search)
		btn1.grid(column=2, row=4)

		btn = tk.Button(window, text='Open', command=self.openfile)
		btn.grid(column=2, row=0)


	def openfile(self):
		self.file_path = tk.filedialog.askopenfilename()
		with open(self.file_path, 'r') as f:
			self.txt.insert(tk.INSERT, f.read())
		
	def search(self):
		freq = self.txt.highlight_pattern(self.txt1.get(), 'red', regexp=True)
		self.matches['text'] = "Number of matches: {}".format(freq)

			
gui = Gui()
window.mainloop()

	
