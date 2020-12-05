# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 12:26:26 2020

@author: user
"""

#Programming Project:

#Input:

#• Number of controls
#• Number of treatments 
#• Time taken to do one control/treatment 
#• How many days user has to do experiment 

#Programme:

#• Assign (randomly) each control and treatment to a letter - Save this file 
#• Assign (randomly) each letter to a day - Save this file 

#Output:

#• A file containing the control and treatments and the letters they are assigned to
#	◦  Only for 1 person to see, this person should not participate in the experiment 

#• A file containing the letters and the day they are assigned to 
#	◦ Only for experimenter to see, they should not know whether the letters are signed to control or treatment


def code_generator():
    """Creates code for each sample(sample) in the trial"""
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

    letters_lc = list(string.ascii_lowercase)
    letters_uc = list(string.ascii_uppercase)

    control_codes = list(permutations(letters_lc, 3))
    for c in range(controls):
        print("Control number {} Code: {}".format(c+1, ''.join(random.choice(control_codes))))

    treatment_codes = list(permutations(letters_uc, 3))
    for t in range(treatments):
        print("Treatment number {} Code: {}".format(t+1, ''.join(random.choice(treatment_codes))))   
        
code_generator()