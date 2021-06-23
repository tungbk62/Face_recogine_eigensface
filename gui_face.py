from tkinter import *
import os

root = Tk(className = 'face_recognition_gui')
svalue = StringVar() 

w = Entry(root,textvariable=svalue) 
w.pack()

def train_eigen_btn_load():
    name = svalue.get()
    os.system('python face_train_eigen.py %s'%name)

def recog_eigen_btn_load():
    os.system('python face_recog_eigen.py')


trainE_btn = Button(root,text="Train", command=train_eigen_btn_load)
trainE_btn.pack()

recogE_btn = Button(root,text="Recognize", command=recog_eigen_btn_load)
recogE_btn.pack()

root.mainloop()