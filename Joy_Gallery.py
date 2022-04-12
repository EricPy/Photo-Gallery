from itertools import count
import pdb
import os
import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()
root.title("Joy Gallery")

#Create list, counter variable to keep track of images
folder = os.listdir("/Users/Eric/Desktop/Joy-folder")
counter = 0
current_img = folder[counter]

#Open image based on the counter using canvas
label = tk.Label(root, text=current_img)
label.grid(column=2,row=0) #Image name header

raw_img = Image.open('/Users/Eric/Desktop/Joy-folder/'+current_img)
width, height = raw_img.size

img = ImageTk.PhotoImage(raw_img.resize((int(width/3),int(height/3))))

pic = tk.Label(root, image=img,justify='center')
pic.grid(row=1,column=0,columnspan=5)

#Create button functions

def forward():
    global folder
    global counter
    global current_img
    global raw_img
    global width
    global height
    global img
    global pic

    del raw_img,width,height,img,pic

    counter+=1

    current_img = folder[counter]

    label = tk.Label(root, text=current_img)
    label.grid(column=2,row=0) #Image name header

    raw_img = Image.open('/Users/Eric/Desktop/Joy-folder/'+current_img)
    width, height = raw_img.size

    img = ImageTk.PhotoImage(raw_img.resize((int(width/3),int(height/3))))

    pic = tk.Label(root, image=img,justify='center')
    pic.grid(row=1,column=0,columnspan=5)

def backward():
    global folder
    global counter
    global current_img
    global raw_img
    global width
    global height
    global img
    global pic

    del raw_img,width,height,img,pic

    counter -= 1

    current_img = folder[counter]

    label = tk.Label(root, text=current_img)
    label.grid(column=2,row=0) #Image name header

    raw_img = Image.open('/Users/Eric/Desktop/Joy-folder/'+current_img)
    width, height = raw_img.size

    img = ImageTk.PhotoImage(raw_img.resize((int(width/3),int(height/3))))

    pic = tk.Label(root, image=img,justify='center')
    pic.grid(row=1,column=0,columnspan=5)

#Create buttons
button_backw = tk.Button(root,text="<<",padx=12,pady=12,command=backward).grid(row=2,column=0)
button_quit = tk.Button(root,text="Exit",padx=50,pady=12,command=root.quit,justify='center').grid(row=2,column=1,columnspan=3)
button_forw = tk.Button(root,text=">>",padx=12,pady=12,command=forward).grid(row=2,column=4)




root.mainloop()