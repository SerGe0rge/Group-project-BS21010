#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import string
from itertools import permutations
import math


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

    def displaycode():
        
        count = 0
        for x in controllist:
            count += 1
            print("Control Code {}: {}".format(count, x))

        count1 = 0
        for y in treatmentlist: 
            count1 += 1 
            print("Treatment Code {}: {}".format(count1, y))
  

        compiledlist = []
        for x in codes:
            for y in x:
                return compiledlist.append(y)
