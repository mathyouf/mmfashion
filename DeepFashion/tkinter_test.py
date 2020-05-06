import os, random
from tkinter import *
from PIL import ImageTk,Image
import pyautogui
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import re
import csv


class Testi():
    def __init__(self):
        image_path = "Category and Attribute Prediction Benchmark/img/2-in-1_Space_Dye_Athletic_Tank/img_00000001.jpg"
        self.canvas = Canvas(root, width = 300, height = 100)
        self.img = PhotoImage(Image.open(image_path))
        self.imgArea = self.canvas.create_image(0, 0, anchor = NW, image = self.img)
        self.canvas.pack()
        self.but1 = Button(root, text="press me", command=lambda: self.changeImg())
        self.but1.place(x=10, y=500)
    def changeImg(self):
        self.img = PhotoImage(Image.open(image_path))
        self.canvas.itemconfig(self.imgArea, image = self.img)

root = Tk()
root.title('User Screen')
root.geometry('400x400')
app = Testi()

root.mainloop()