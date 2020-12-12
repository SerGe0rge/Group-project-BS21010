# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 15:26:48 2020

@author: Devin
"""
import random
import string
from itertools import permutations
import itertools
#import math
import copy

#PLEASE READ THIS FIRST TO UNDERSTAND WHAT THE CLASS DOES:
#1) codegenerator(): generate a list of 3 letter codes for both controls and treatments 

#2) assigncodes(): codes are assigned to controls(lowercase) and treatments(uppercase) list 
#                  unblinded for easier when creating a unblinded file

#3) tabulateblind(): treatment list codes are then all changed to lower case so it cannot be differentiated which is a
#                    control code and which is a treatment code. This is displayed as an output since all codes are in
#                    lowercase. Save option is provided. 

#4) tabulateunblind(): function can be called to create a unblinded table which will not be displayed as an output 
#                      to ensure unbiasness if a scientist conducting the experiment is using this program. 
#                      save option is provided. 
#                      saved file can be opened and viewed by the one not conducting the experiment.  

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
        
        
        
#Example(without inputs): 
treatments = 15
controls = 15
days = 6
numexpt = 5

d = CodeGenerator(controls,treatments,days,numexpt)
d.codegenerator()
d.assigncodes()
d.tabulateblind()
d.tabulateunblind()

