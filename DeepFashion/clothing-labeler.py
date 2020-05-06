import os, random
from tkinter import *
from PIL import ImageTk,Image
import pyautogui
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import re
import csv

def set_User(root, clicked):
    user = clicked.get()
    myLabel = Label(root, text=('You are ' + user)).pack()
    root.quit()

def prompt_User():
    root = Tk()
    root.title('User Screen')
    root.geometry('400x400')
    options = ["Matt", "Chihiro"]
    clicked = StringVar()
    clicked.set(options[0])
    drop = OptionMenu(root, clicked, *options)
    drop.pack()
    myButton = Button(root, text="This is me!", command= lambda: set_User(root, clicked)).pack()
    root.mainloop()
    user = clicked.get()
    root.destroy()
    check_or_create_user_CSV(user)
    return user

def show_image(user):
    def label_Image(label, image, root, user, img):
        print(user,label, image)
        append_list_as_row(user+'.csv',[label, image])
        show_image(user)
    def leftKey(event):
        print("Left key pressed")
        label_Image("dislike", image, root, user, img)
    def rightKey(event):
        print("Right key pressed")
        label_Image("like", image, root, user, img)
    root = Tk()
    root.title('Do you like this?')
    root.geometry('400x400')
    root.bind('<Left>', leftKey)
    root.bind('<Right>', rightKey)
    img = ImageTk.PhotoImage(Image.open(get_Image()))
    panel = Label(root, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    root.mainloop()

def get_Image():
    directory = "Category and Attribute Prediction Benchmark/"
    random_image = load_image_Names()
    return directory + random_image

def load_image_Names():
    filename = "Category and Attribute Prediction Benchmark/Anno/list_category_img.txt"
    with open(filename) as f:
        lines = f.readlines()
    random_number = random.randrange(3, 289224)
    string = lines[random_number]
    regex_simplified_string = re.search( r'(\S+)\s+\d+$', string)
    first_Match = regex_simplified_string.group(1)
    return first_Match

def check_or_create_user_CSV(username):
    csv_filename = username + '.csv'
    if os.path.isfile(csv_filename):
        print ("File exist")
    else:
        print ("File not exist")
        with open(csv_filename, 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['Username', username])

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = csv.writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

def main():
    print('Starting Clothing Labeler Lord Fisher')
    user = prompt_User()
    show_image(user)

main()
