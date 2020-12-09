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
random.shuffle(compiledlist)#shuffled 2 times to ensure randomness

days = int(input('How many days will this experiment be conducted over? '))
#from stackoverflow, converting the number input into a list of days 
dayslist = ['Day ' + str(num) for num in range(1, days+1)]


numexpt = int(input('How many experiments do you plan to do in a day? '))
#from stackoverflow, to break into multiple list of desired number of experiments
compiles = [compiledlist[x:x+numexpt] for x in range(0, len(compiledlist), numexpt)]

combine = itertools.zip_longest(dayslist, compiles)
daysdict = dict(combine)

for key,value in daysdict.items():
    print(key, value)

def save(result):
    """this function provides the user an option to save their report under a name of their choice
       e.g. save(report)
       check your directory to locate the saved file"""
    
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
            

        yes = 'Your report has been saved. Thank you very much for using this program.'
        return yes


    if savefile == 2:
        no = 'Your report has not been saved. Thank you very much for using this program.'
        return no  

save(daysdict)

#to do: 
#error checking needed to assign values to keys in dictionary
#ensure that all lists are assigned to a particular day, if not put the remaining into None key
#if not enough keys for each value, i.e. not enough number of days for the number of sets of experiments
#print out your experiments cannnot be completed in the assigned number of days. 
