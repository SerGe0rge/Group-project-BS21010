import random
import string
from itertools import permutations
import math
from tkinter import *
from tkinter import filedialog


class main_code:
    

    def __init__(self):
        
        self.controls = 0
        self.treatments = 0
        self.days = 0
        self.numexpt = 0
        self.experiment_dict = {}
        self.assigneddays=None
        self.final_list = []
        self.tcl_codes_list = []
        self.treatmentlist = None
        self.controllist = None
        self.joinedshuffle = None
        self.unblindedcode_list = []
        self.blindedcode_list = []
        
        
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
        
        if len(self.tcl_codes_list) == 0 :

            self.codegenerator()
            
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
            self.final_list = copy.deepcopy(random.shuffle(self.joinedshuffle))  
            draftlist =  random.shuffle(self.joinedshuffle)
            final_list = copy.deepcopy(draftlist)
            return self.final_list     
    

           
    def codedisplays_blind(self): 
        
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
            cg = self.codegenerator()
            code_list = cg
            self.experiment_dict = {}
            for day in range(1, self.days+1):
                self.experiment_dict[day] = code_list[(day-1) * self.numexpt : (day-1) * self.numexpt + self.numexpt]
               
                # CodeGenerator class in called upon and a list of 3 letter codes is created using codegenerator function
                # for every day a dictionary is created 
                # the code list is spliced according to the number of experiments per day the experimenter has inputed 
                # e.g  if the number of experiments done per day is 3 and it is for the first day
                # code_list[(1-1) * 3 : (1-1) * 3 + 3]
                # code_list[0:3]
                # in dictionary for the key day 1, the first 3 codes from the list of codes is taken and put into the dictionary as a value pair to the key
                
            messagebox.showinfo("List", str(self.experiment_dict))
            # a message box will appear showing the days and the 3 letter codes assigned to the days  

        
        
    
noc = main_code()

root = Tk() #root acts as our main window, all widgets need the parameter root to appear in this GUI window
root.geometry("1200x1200") #creates a GUI window with the arbitrary values specified
root.title("Experimental design") #creates a title for the GUI window
#Label() places a piece of text on the GUI window 
#.grid() places any GUI widget on the GUI window in the position specified with row and column parameters in .grid()
#Button() places a button on the GUI that when pressed initiates the command in the parameters
#command parameter in Button() allows us to call functions from the class main_code when a button is pressed
#Entry() creates an entry box on the GUI window for the user to input values into it 
#.get() retrieves the value the user put in the entry box

def set_controls():
    '''Generates GUI to allow the user to input the number of controls in the trial taking place and check if its an acceptable value to be stored so that the sample codes can be generated later'''
    label_c = Label(root, text="Enter number of controls: ")  
    label_c.grid(row=1, column= 0)
    controls_eb = Entry(root, width= 50)  
    controls_eb.grid(row=1, column= 1)
    c_button = Button(root, text="Press to check value of controls", command= lambda: noc.get_valid_controls(controls_eb.get()))
    c_button.grid(row=1, column=2)
    
def set_treatments():
    '''Generates GUI to allow the user to input the number of treatments in the trial taking place and check if its an acceptable value to be stored so that the sample codes can be generated later'''
    label_t = Label(root, text="Enter number of treatments: ")
    label_t.grid(row=2, column=0)
    treatments_eb = Entry(root, width=50)
    treatments_eb.grid(row=2, column=1)
    t_button = Button(root, text= "Press to check value of treatments", command= lambda: noc.get_valid_treatments(treatments_eb.get()))
    t_button.grid(row=2, column=2)   

def set_days():
    '''Generates GUI to allow the user to input the number of days over which the experiment will take place and store it by checking the value so that a timetable can be produced later'''
    label_d = Label(root, text="Enter number of days: ")
    label_d.grid(row=3, column=0)
    days_eb = Entry(root, width=50)
    days_eb.grid(row=3, column=1)
    d_button = Button(root, text= "Press to check value of days", command= lambda: noc.get_valid_days(days_eb.get()))
    d_button.grid(row=3, column=2)

def set_numexpt():
    '''Generates GUI to allow the user to input the number of experiments that will take place per day and store it by checking the value so that a timetable can be produced later'''
    label_n = Label(root, text="Enter number of experiments: ")
    label_n.grid(row=4, column=0)
    numexpt_eb = Entry(root, width=50)
    numexpt_eb.grid(row=4, column=1)
    t_button = Button(root, text= "Press to check value of number of experiments", command= lambda: noc.get_valid_numexpt(numexpt_eb.get()))
    t_button.grid(row=4, column=2)    
                
def cd_gen_blind():
   '''Creates a button in the GUI to allow the user to press it and show the blind codes generated for their experiment'''
   cd_button = Button(root, text="Press to generate blind codes", command= lambda: noc.codedisplays_blind())
   cd_button.grid(row=5, column=1)

def cd_gen_unblind():
    '''Creates a button in the GUI to allow the user to press it and show the unblinded codes generated for their experiment'''
    cd_button = Button(root, text="Press to generate unblind codes", command= lambda: noc.codedisplays_unblind())
    cd_button.grid(row=6, column=1)
    
   
def file_store_blind():
    '''Creates a save button in the GUI to allow the user to save the blinded timetable created'''
    fsb_button = Button(root, text="Press to start saving blind timetable", command = file_save_blind)
    fsb_button.grid(row=7, column=1)

def file_store_unblind():
    '''Creates a save button in the GUI to allow the user to save the unblinded timetable created'''
    fsu_button = Button(root, text="Press to start saving unblind timetable", command = file_save_unblind)
    fsu_button.grid(row=8, column=1)

def file_save_blind():
    '''Creates the option for the user to save the blind timetable under a file name of their choice'''
    mb = messagebox.askquestion('Save','Would you like to save your blind timetable?') #provides option for user to save or not
        
    if mb == 'yes':
       filesave = filedialog.asksaveasfilename( 
                defaultextension='.txt', filetypes=[("txt files", '*.txt')], 
                title="Choose filename") #filedialog.asksaveasfilename allows the user to choose a name for their file and save it where they want to on their device
       with open(filesave, 'w') as wf:
           for key in noc.experiment_dict:
              print(key, noc.experiment_dict[key], file = wf) #saves the blind timetable under filename specified before
       messagebox.showinfo('Save', 'Thank you! Your file has been saved') #confirms the file has been saved

    else:
            messagebox.showinfo('Save', "Your blind timetable has not been saved") #specifies file will not be saved

def file_save_unblind():
    '''Creates the option for the user to save the unblind timetable under a file name of their choice'''
    mb = messagebox.askquestion('Save','Would you like to save your unblind timetable?') #provides option for user to save or not
        
    if mb == 'yes':
       filesave = filedialog.asksaveasfilename(
                defaultextension='.txt', filetypes=[("txt files", '*.txt')],
                title="Choose filename") #filedialog.asksaveasfilename allows the user to choose a name for their file and save it where they want to on their device
       with open(filesave, 'w') as wf: 
              print(noc.assigncodes(final_list), file = wf) #saves the unblind timetable under filename specified before
       messagebox.showinfo('Save', 'Thank you! Your file has been saved') #confirms the file has been saved

    else:
            messagebox.showinfo('Save', "Your unblind timetable has not been saved") #specifies file will not be saved
    

            
         
             


   
set_controls()
set_treatments()
set_days()
set_numexpt()
cd_gen_blind()
cd_gen_unblind()
file_store_blind()
file_store_unblind()


root.mainloop()


