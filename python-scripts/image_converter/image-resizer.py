#pip install

from PIL import Image
from pathlib import Path  #core python module
import tkinter as tk
from tkinter import filedialog

ask = ""
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

width = input("Please give the images a new size. \nWidth: ")
height = input("Height: ")
width = int(width)
height = int(height)
newname = input("New name? (without file extension): ")
if(newname == ""):
    newname = "newfile"

baseWidth = ""
baseHeight = ""

image = Image.open(file_path)
newimg = image.resize((width,height))
newimg = newimg.save(newname+".png")
print("Saving done")
