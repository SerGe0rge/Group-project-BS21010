# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
import string
from itertools import permutations
  
flag = True
while flag:
    controls = input("Number of controls: ")
    
    if controls.isdigit():
        controls = int(controls)
        flag = False
        
    else:
        print("Invalid input. Please enter a whole number.")

flag1 = True
while flag1:
    treatments = input("Number of treatments: ")

    if treatments.isdigit():
        treatments = int(treatments)
        flag1 = False

    else:
        print("Invalid input. Please enter a whole number.") 
        
        
def codegenerator(): 
    
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

codes = codegenerator()

def displaycodes():
    
    controllist, treatmentlist = codes
          
    count = 0
    for x in controllist:
        count += 1
        print("Control Code {}: {}".format(count, x))
    
    count1 = 0
    for y in treatmentlist: 
        count1 += 1 
        print("Treatment Code {}: {}".format(count1, y))
            
display = displaycodes()  
   
compiledlist = []
for x in codes:
    for y in x:
        compiledlist.append(y)

sorted(compiledlist)#combine treatmentlist and controllist
random.shuffle(compiledlist)
random.shuffle(compiledlist)
print(compiledlist)

#to do: 
#check if controls and treatments are shuffled properly
#middle position checking, variable beside are all not lower/uppercase. 
#prevents consecutive testing of either controls or treatments
#after that then proceed to break out of loop


#days = int(input("How many day(s) will these experiments be conducted over? "))
#dayslist = [d for d in range(1, days+1)]

#totaltime = time * (len(treatmentlist) + len(controllist))
#numexpt = totaltime / days

#print("{} experiment(s) will be conducted over {} days. Duration of each experiment is {} hour(s)."
      #.format(numexpt, days, time))

