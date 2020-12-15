# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 15:17:15 2020

@author: jenni
"""

import random
import string
from itertools import permutations
import math
from tkinter import *


class CodeGenerator():
    
    def __init__(self, controls, treatments, days, numexpt):
        self.controls = controls
        self.treatments = treatments
        self.days = days
        self.numexpt = numexpt
        self.tcl_codes_list = None
        self.treatmentlist = None
        self.controllist = None
        self.joinedshuffle = None
        
        
    def codegenerator(self): 
        """generates lowercase 3 letter codes for the total number of controls and treatments to be conducted"""

        totalsample = self.controls + self.treatments       

        #checking is done first to fulfill that total number of samples does not exceed 17576.
        #17576 = 26^3(total number of permutations of 3-letter codes before repeats can occur)
        if totalsample >= 17576:

            print("Please make sure that control and treatment experiments do not exceed 17576 experiments")

        else:
            #operations below is not necessary as logtotalsample returns an increasingly small value(=1) as the size of  
            #totalsample increase, hence I have comment out the formulas below. 
            #logtotalsample = math.log(totalsample,26)
            #roundedtotal = math.ceil(logtotalsample)

            letters_lc = list(string.ascii_lowercase)
            tcl_codes = list(permutations(letters_lc, 3))

            self.tcl_codes_list = []
            for c in range(totalsample):
                self.tcl_codes_list.append(''.join(random.choice(tcl_codes)))

            return self.tcl_codes_list
        

    def assigncodes(self):
        """assigning codes from the codegenerator to the treatments and controls list"""
        
        nums = [self.controls, self.treatments]
        it = iter(self.tcl_codes_list)
        separate = [[next(it) for _ in range(num)] for num in nums]
        
        #assigning first portion of codes to treatmentlist
        #treatment codes are capitalised first to provide an unblinded version of table.
        self.treatmentlist = copy.deepcopy(separate[0])
        self.treatmentlist = [t.upper() for t in self.treatmentlist]
        
        #assigning remaining portion of codes to controllist
        self.controllist = copy.deepcopy(separate[1])
        
        #compiling the codes in "joinedshuffle" again to reshuffle 
        self.joinedshuffle = self.treatmentlist + self.controllist 

        #shuffling the new list after assigning codes to treatment and control list so the assigned codes are jumbled
        random.shuffle(self.joinedshuffle)
        
    def tabulateblind(self):
        """this table is displayed in the output, since it is blinded. 
           it is available for viewing as an output for everyone.
           table can then be saved if the user wished to."""
        
        #.lower() is used to blind the uppercase treatments before displaying as an output
        #"mimics" list will divide the "joinedshuffle" list of controls and treatments into equal chunks as decided by the user.
        lowerlist = [y.lower() for y in self.joinedshuffle]
        dayslist = ['Day ' + str(num) for num in range(1, days+1)]
        mimics = [lowerlist[x:x+self.numexpt] for x in range(0, len(lowerlist), self.numexpt)]

        if len(mimics) == len(dayslist):
            combine = itertools.zip_longest(dayslist, mimics)
            daysdict = dict(combine)

            for key,value in daysdict.items():
                print(key, value)
                
            print("-Assignment is Complete-")

        if len(mimics) < len(dayslist):
            
            combine = itertools.zip_longest(dayslist, mimics)
            daysdict = dict(combine)

            for key,value in daysdict.items():
                print(key, value)
                
            print("You have extra day(s) left for experiment.")

        if len(mimics) > len(dayslist):
            combine = itertools.zip_longest(dayslist, mimics)
            daysdict = dict(combine)

            for key,value in daysdict.items():
                print(key, value)

            print("Sorry, all of your experiments cannot be accommodated in the given timeframe.")
            
        flag1 = True
        while flag1: 

            savefile = input('\nWould you like to save the report:\n1. Yes\n2. No\n?')
        
            if savefile.isdigit():
                savefile = int(savefile)
            
            if savefile in range(1,3):
                flag1 = False

            else: 
                print('Please enter a valid number')

        if savefile == 1:

            filename = input('Enter a file name: ')
            with open(filename, 'w') as wf:
            
                for key,value in daysdict.items():
                    print(key, value, file = wf)
            

            yes = 'Your table has been saved. Thank you very much for using this program.'
            return yes


        if savefile == 2:
            no = 'Your table has not been saved. Thank you very much for using this program.'
            return no  

        
        
    def tabulateunblind(self):
        """this table is not displayed in the output, it is saved directly into a file to prevent viewing. 
           it should not be seen by scientists conducting the experiments.
           table should only be viewed by scientist planning and assigning roles to the ones conducting experiments."""
           #this table is only set to being saved to a document and not produced as an output for user to see
           #user can choose to see the table in the saved file
        
        dayslist = ['Day ' + str(num) for num in range(1, days+1)]
        mimics = [self.joinedshuffle[x:x+self.numexpt] for x in range(0, len(self.joinedshuffle), self.numexpt)]
        
        flag = True
        while flag: 

            savefile = input('This is a unblinded table and can only be viewed after saving\nWould you like to save the table:\n1. Yes\n2. No\n?')

            if savefile.isdigit():
                savefile = int(savefile)

            if savefile in range(1,3):
                flag = False

            else: 
                print('Please enter a valid number')

        if savefile == 1:
            
            filename = input('Enter a file name: ')

            if len(mimics) == len(dayslist):
                combine = itertools.zip_longest(dayslist, mimics)
                daysdict = dict(combine)
                
                with open(filename, 'w') as wf:
                    for key,value in daysdict.items():
                        print(key, value, file = wf)

                return "-Table has been saved-"

            if len(mimics) < len(dayslist):

                combine = itertools.zip_longest(dayslist, mimics)
                daysdict = dict(combine)

                with open(filename, 'w') as wf:
                    for key,value in daysdict.items():
                        print(key, value, file = wf)
                        print("You have extra day(s) left for experiment.", file = wf)
                        
                return "-Table has been saved-"

            if len(mimics) > len(dayslist):
                combine = itertools.zip_longest(dayslist, mimics)
                daysdict = dict(combine)

                with open(filename, 'w') as wf:
                    for key,value in daysdict.items():
                        print(key, value, file = wf)
                        print("Sorry, all of your experiments cannot be accommodated in the given timeframe.", file = wf)
                        
                return "-Table has been saved-"
        
        if savefile == 2:
            
            no = 'Your table has not been saved. Thank you very much for using this program.'
            return no 
        

class number_of_controls:
    

    def __init__(self):
        
        self.controls = 0
        self.treatments = 0
        self.days = 0
        self.numexpt = 0
        
        # initialising functions, instance object will call on functions 
        # variables first set to 0 as they are yet to be defined 
                               
    def get_valid_controls(self, controls):
        
        """ 
        makes sure the number of controls inputed are valid and can be used to generate 3 letter codes for the randomisation process
        """
        
        try:
            value=int(controls)
            
            if value>0 and value<26**3:
                self.controls = int(controls)
                messagebox.showinfo("Valid", "This is a valid control value")
                return True
            # if the value inputed for controls is a number below the maxmimum number of codes that can be generated by 3 letter codes,
            # above 0 and not a string
            # variable control is validated and set 
            # message box will be shown to tell the experimenter that the number of controls given has been validated 
            
        except:
            messagebox.showerror("Error", "This is not a valid control value")
            return False
            # if value inputed for controls is not valid  
            # a message box is shown to ask the experimenter to give another value
            
        
    def get_valid_treatments(self, treatments):
        
        """ 
        makes sure the number of treatments inputed are valid and can be used to generate 3 letter codes for the randomisation process
        """
        
        try:
            value=int(treatments)
            
            if value>0 and value<26**3:
                self.treatments = int(treatments)
                messagebox.showinfo("Valid", "This is a valid treatment value")
                return True 
            # if the value inputed for treatments is a number below the maxmimum number of codes that can be generated by 3 letter codes,
            # above 0 and not a string
            # variable treatments is validated and set 
            # message box will be shown to tell the experimenter that the number of treatments given has been validated  
            
        except:
            messagebox.showerror("Error", "This is not a valid treatments value")
            return False
            # if value inputed for treatments is not valid  
            # a message box is shown to ask the experimenter to give another value
                
        
    def get_valid_days(self, days):
        
        """ 
        makes sure the number of days inputed are valid 
        """
        
        try:
            value=int(days)
            
            if value>0:
                self.days = int(days)
                messagebox.showinfo("Valid", "This is a valid day value")
                return True 
            # if the value inputed for number of days is a number above 0 and not a string
            # variable days is validated and set 
            # message box will be shown to tell the experimenter that the number of days given has been validated  
            
        except:
            messagebox.showerror("Error", "This is not a valid day value")
            return False
             # if value inputed for number of days is not valid  
             # a message box is shown to ask the experimenter to give another value

    def get_valid_numexpt(self, numexpt):
        
        """ 
        makes sure the number inputed for the number of experiments that the experimenter does in 1 day is a valid number
        """
        
        try:
            value=int(numexpt)
            
            if value>0:
                self.numexpt = int(numexpt)
                messagebox.showinfo("Valid", "This is a valid number of experiments value")
                return True 
            # if the value inputed for the number of experiments that the experimenter does in 1 day is above 0 and not a string
            # variable numexpt is validated and set 
            # message box will be shown to tell the experimenter that the numexpt has been validated
            
        except:
            messagebox.showerror("Error", "This is not a valid number of experiments value")
            return False
             # if value inputed for the number of experiments that the experimenter does in 1 day is not valid  
             # a message box is shown to ask the experimenter to give another value

           
    def codegenerator(self): 
        
        """
        generates 3 random letter codes for treatments and controls and 
        displays the codes with the days they are assigned to for the experimenter to complete 
        """
        if self.days * self.numexpt < self.controls + self.treatments:
            messagebox.showerror("Error", "Not enough days to complete experiment/Not enough experiments carried out per day")
            # if the number of controls plus number of treatments exceeds
            # the number of days multiplied by the number of experiments the experimenter completes in 1 day
            # a message box will appear to tell the user that the experiment is not possible to carry out 
            
        else:
            cg = CodeGenerator(self.controls, self.treatments, self.days, self.numexpt)
            code_list = cg.codegenerator()
            experiment_dict = {}
            for i in range(1, self.days+1):
                experiment_dict[i] = code_list[(i-1) * self.numexpt: (i-1) * self.numexpt + self.numexpt]
                            
            messagebox.showinfo("List", str(experiment_dict))
            

    
noc = number_of_controls()


root = Tk()
root.geometry("800x800")
root.title("Experimental design")
      


def set_controls():
    label_c = Label(root, text="Enter number of controls: ")
    label_c.grid(row=1, column= 0)
    controls_eb = Entry(root, width= 50)
    controls_eb.grid(row=1, column= 1)
    c_button = Button(root, text="Press to check value of controls", command= lambda: noc.get_valid_controls(controls_eb.get()))
    c_button.grid(row=1, column=2)
    
def set_treatments():
    label_t = Label(root, text="Enter number of treatments: ")
    label_t.grid(row=2, column=0)
    treatments_eb = Entry(root, width=50)
    treatments_eb.grid(row=2, column=1)
    t_button = Button(root, text= "Press to check value of treatments", command= lambda: noc.get_valid_treatments(treatments_eb.get()))
    t_button.grid(row=2, column=2)   

def set_days():
    label_d = Label(root, text="Enter number of days: ")
    label_d.grid(row=3, column=0)
    days_eb = Entry(root, width=50)
    days_eb.grid(row=3, column=1)
    d_button = Button(root, text= "Press to check value of days", command= lambda: noc.get_valid_days(days_eb.get()))
    d_button.grid(row=3, column=2)

def set_numexpt():
    label_n = Label(root, text="Enter number of experiments: ")
    label_n.grid(row=4, column=0)
    numexpt_eb = Entry(root, width=50)
    numexpt_eb.grid(row=4, column=1)
    t_button = Button(root, text= "Press to check value of number of experiments", command= lambda: noc.get_valid_numexpt(numexpt_eb.get()))
    t_button.grid(row=4, column=2)    
                
def cd_gen():
   cd_button = Button(root, text="Press to generate codes", command= lambda: noc.codegenerator())
   cd_button.grid(row=5, column=1)
        
def dis_cd():
    label_dis = Label(root, text="Here are your codes")
    label_dis.grid(row=4, column=0)
    dis_button = Button(root, text="Press to show your codes", command=noc.displaycode)
    dis_button.grid(row=4, column=2)
    
def table():
    table_b = Button(root, text= "Press to view your timetable", command = noc.tabulateblind)
    table_b.grid(row=5, column=2)

set_controls()
set_treatments()
set_days()
set_numexpt()
cd_gen()
# dis_cd()
# table()
root.mainloop()
