from tkinter import *
from PIL import ImageTk,Image 

root =Tk()

root.title("Rotating Image")
root.geometry("500x500")
root.configure(background="black")

Rapunzel = ImageTk.PhotoImage(Image.open("th.jpg"))

image = Label(root,bg="gold",highlightthickness=5,borderwidth=2,relief=SOLID)
image.place(relx=0.5,rely=0.5,anchor=CENTER)

def rotate():
    image.rotate(angle)

def chooseimage():
    image['image']=Rapunzel
    
btn = Button(root,text="Choose Image",command=chooseimage)
btn.place(relx=0.5,rely=0.1,anchor=CENTER)

btn = Button(root,text="Rotate",command=rotate)
btn.place(relx=0.5,rely=0.18,anchor=CENTER)

root.mainloop()
