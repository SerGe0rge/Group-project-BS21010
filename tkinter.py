

import random
import string
from itertools import permutations
import math
from tkinter import *


class number_of_controls:
    
    def __init__(self, controls, treatments, totalsample, tcl_codes_list, logtotalsample, roundedtotal):
        
        if self.check_controls(controls):
            self.controls = controls
        else:
             print("Invalid input. Please enter a whole number.")
                
                
        if self.check_treatments(treatments):
            self.treatments = treatments
        else:
             print("Invalid input. Please enter a whole number.")
                
        self.totalsample = totalsample
        self.tcl_codes_list = tcl_codes_list
        self.logtotalsample = logtotalsample
        self.roundedtotal = roundedtotal
        
                               
    def get_valid_controls(self,controls):
        
       
        try:
            value=int(self.controls)
            
            if value>0 and value<17576:
                return True
            
        except:
            return False
            
    def get_valid_treatments(self,treatments):
        
       
        try:
            value=int(self.treatments)
            
            if value>0 and value<17576:
                return True 
            
        except:
            return False
                
                
             
    def codegenerator(self, totalsample, logtotalsample, roundedtotal, tcl_codes_list): 
        
        self.totalsample = self.controls + self.treatments 
        
        
        if totalsample <= 17576:
            
            self.logtotalsample = math.log(totalsample,26)

            self.roundedtotal = math.ceil(logtotalsample)

        
            letters_lc = list(string.ascii_lowercase)
            self.tcl_codes = list(permutations(letters_lc, 3))
            
            self.tcl_codes_list = []
            for c in range(roundedtotal):
                self.tcl_codes_list.append(''.join(random.choice(self.tcl_codes)))
                return self.tcl_codes_list

        else:

            print("Please make sure that control and treatment experiments do not exceed 17576 experiments")

    



root = Tk()
root.geometry("800x800")
root.title("Experimental design")



def set_controls():
    label_c = Label(root, text="Enter number of controls: ")
    label_c.grid(row=1, column= 0)
    controls_eb = Entry(root, width= 50)
    controls_eb.grid(row=1, column= 1)
    controls = controls_eb.get()
    c_button = Button(root, text="Press to check value of controls", command=self.get_valid_controls)
    c_button.grid(row=1, column=2)
        
    
    
def set_treatments():
    label_t = Label(root, text="Enter number of treatments: ")
    label_t.grid(row=2, column=0)
    treatments_eb = Entry(root, width=50)
    treatments_eb.grid(row=2, column=1)
    treatments = treatments_eb.get()
    t_button = Button(root, text= "Press to check value of treatments", command=self.get_valid_treatments)
    t_button.grid(row=2, column=2)
            
        
                
def cd_gen():
   cd_button = Button(root, text="Press to generate codes", command=self.codegenerator)
   cd_button.grid(row=3, column=1)
        
def dis_cd():
    label_dis = Label(root, text="Here are your codes")
    label_dis.grid(row=4, column=0)
    dis_button = Button(root, text="Press to show your codes", command=self.displaycode)
    dis_button.grid(row=4, column=2)
    
def table():
    table_b = Button(root, text= "Press to view your timetable", command = self.tabulateblind)
    table_b.grid(row=5, column=2)



set_controls()
set_treatments()
cd_gen()        




root.mainloop()
