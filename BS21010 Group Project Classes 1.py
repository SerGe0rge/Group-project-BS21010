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
        while True:
            controls = input("Number of controls: ")
            
            if controls.isdigit():
                controls = int(controls)
                return controls
                
            else:
                print("Invalid input. Please enter a whole number.")
                
    def get_valid_treatments(self):
        while True:
            treatments = input("Number of treatments: ")
            
            if treatments.isdigit():
                treatments = int(treatments)
                return treatments
            else:
                print("Invalid input. Please enter a whole number.")
                
                
                

