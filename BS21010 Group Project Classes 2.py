#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import string
from itertools import permutations


class number_of_controls:
    
    def __init__(self):
        return
        
     def get_valid_controls(self):
        
        while true:
            controls = input("Number of controls: ")
       
            if controls.isdigit():
                controls = int(controls)
                return controls
                
            else:
                print("Invalid input. Please enter a whole number.")
                
                
    def get_valid_treatments(self):
        
        while true:
            treatments = input("Number of treatments: ")
       
            if treatments.isdigit():
                treatments = int(treatments)
                return treatments
                
            else:
                print("Invalid input. Please enter a whole number.")
    
                
    def codegenerator(self): 
    
        letters_lc = list(string.ascii_lowercase)
        letters_uc = list(string.ascii_uppercase)

        control_codes = list(permutations(letters_lc, 3))
        controllist = []
        for c in range(controls):
            controllist.append(''.join(random.choice(control_codes)))

        treatment_codes = list(permutations(letters_uc, 3))
        treatmentlist = []
        for t in range(treatments):
            treatmentlist.append(''.join(random.choice(treatment_codes)))

        return controllist, treatmentlist   
    

    def displaycodes(self):
    
        controllist, treatmentlist = codes

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

