import tkinter as tk
import os
import pdb
from PIL import ImageTk,Image

root = tk.Tk()
root.title("Photo Viewer")

contents = os.listdir('/Users/Eric/Desktop/images')
folder = [Image.open("/Users/Eric/Desktop/images/"+x) for x in contents]
counter = 0
#pdb.set_trace()
width, height = folder[counter].size

img = ImageTk.PhotoImage(folder[counter].resize((int(width/4),int(height/4))))
pic = tk.Label(image=img) 
pic.grid(row=0,column=0,columnspan=3)

def forward():
    global pic
    global button_forward
    global button_back
    global counter
    global img

    pic.grid_forget()

    counter+=1

    if counter == (len(folder)-1):
        button_forward.grid_forget()
        button_forward = tk.Button(root, text = ">>", state=tk.DISABLED)
        button_forward.grid(row=1,column=2)
    elif counter > 0:
        button_back.grid_forget()
        button_back = tk.Button(root,text="<<",command=back)
        button_back.grid(row=1, column=0)


    width, height = folder[counter].size
    img = ImageTk.PhotoImage(folder[counter].resize((int(width/4),int(height/4))))
    pic = tk.Label(image=img)
    pic.grid(row=0,column=0,columnspan=3)


def back():
    global pic
    global button_forward
    global button_back
    global counter
    global img

    pic.grid_forget()

    counter-=1

    if counter == 0:
        button_back.grid_forget()
        button_back = tk.Button(root,text="<<",state=tk.DISABLED)
        button_back.grid(row=1, column=0)
    elif counter < (len(folder)-1):
        button_forward.grid_forget()
        button_forward = tk.Button(root,text=">>",command=forward)
        button_forward.grid(row=1,column=2)

    width, height = folder[counter].size
    img = ImageTk.PhotoImage(folder[counter].resize((int(width/4),int(height/4))))
    pic = tk.Label(image=img)
    pic.grid(row=0,column=0,columnspan=3)

button_back = tk.Button(root,text="<<",state=tk.DISABLED)
button_exit = tk.Button(root,text="Exit", command=root.quit)
button_forward = tk.Button(root,text=">>",command=forward)

button_back.grid(row=1, column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)

root.mainloop()