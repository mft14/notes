#pip install 

from PIL import Image
from pathlib import Path  #core python module
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

width = 100
height = 100
baseWidth = ""
baseHeight = ""

image = Image.open(file_path)
newimg = image.resize((200,100))
newimg = newimg.save("pegy.png")
print("Saving done")