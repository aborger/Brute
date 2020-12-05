import time
import random
import tkinter as tk
from pynput.keyboard import Key, Controller

root = tk.Tk()
keyboard = Controller()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
			'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
			'u', 'v', 'w', 'x', 'y', 'z']

			
def type(letter):
	keyboard.type(letter)
	time.sleep(.1)
	
def press(key):
	keyboard.press(key)
	time.sleep(.1)
	
def main():
	time.sleep(3)
	label1 = tk.Label(root, text= 'Running...', fg='green', font=('helvetica', 12, 'bold'))
	while True:
		for i in range(0, 4):
			type(random.choice(letters))
		press(Key.enter)
		for i in range(0, 4):
			press(Key.backspace)
			

button1 = tk.Button(text='Start',command=main, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()