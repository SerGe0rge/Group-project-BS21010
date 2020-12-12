# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 13:39:12 2020

@author: user
"""
from tkinter import *
root = Tk()
root.geometry("800x800")
root.title("Experimental design")


def set_controls():
    label_c = Label(root, text="Enter number of controls: ")
    label_c.grid(row=1, column= 0)
    controls_eb = Entry(root, width= 50)
    controls_eb.grid(row=1, column= 1)
    controls = controls_eb.get()
    c_button = Button(root, text="Press to check value of controls", command=get_valid_controls)
    c_button.grid(row=1, column=2)


def set_treatments():        
    label_t = Label(root, text="Enter number of treatments: ")
    label_t.grid(row=2, column=0)
    treatments_eb = Entry(root, width=50)
    treatments_eb.grid(row=2, column=1)
    treatments = treatments_eb.get()
    t_button = Button(root, text= "Press to check value of treatments", command=get_valid_treatments)
    t_button.grid(row=2, column=2)

            
def cd_gen():
    cd_button = Button(root, text="Press to generate codes", command=code_generator)
    cd_button.grid(row=3, column=1)
    
def dis_cd():
    label_dis = Label(root, text="Here are your codes")
    label_dis.grid(row=4, column=0)
    dis_button = Button(root, text="Press to show your codes", command=displaycodes)
    dis_button.grid(row=4, column=2)
     
        
set_controls()
set_treatments()
cd_gen()
dis_cd()
       
       

root.mainloop()


