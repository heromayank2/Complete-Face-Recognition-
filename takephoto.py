import PIL
from PIL import Image,ImageTk
import pytesseract
import os
import cv2
from tkinter import *
from tkinter.messagebox import *


root = Tk()
frame = Frame(root, relief=RIDGE, borderwidth=2)
root.configure(background='light green')
root.title('Face Recognition by Mayank')
root.geometry("700x600")
root.bind('<Escape>', lambda e: root.quit())
root.resizable(0,0)
lmain = Label(root)
lmain.pack()

def show_frame(name):
    capture =cv2.VideoCapture(0)
    path="./img/known/"+name+".jpg"
    showinfo("Important", "Press 'c' to save the image")
    while True:
        ret,frame=capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF ==ord('c'):
            _, image = capture.read()
            cv2.imwrite(path,image)
            break
    showinfo("Congrats", "Your Image is Saved with "+name+".jpg")
    capture.release()
    cv2.destroyAllWindows()
    root.quit()

def save_name():
    st=e.get() 
    l.destroy()
    e.destroy()
    click_button.destroy() 
    show_frame(st)

l =Label(root, text="Please Enter your Name ")
l.pack()
e = Entry(root)
e.pack()
e.focus_set()
click_button = Button(master=root, text='Start',bg="green",fg="white", command=save_name)
click_button.pack(side="top")


root.mainloop()