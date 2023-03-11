import tkinter as tk
from tkinter import *
import tkinter.scrolledtext as ScrolledText
global input_string
#creating a class called MyApp
class MyApp(tk.Tk):
    #first window gets created where we can type the input text to be analyzed
    def __init__(self):
        tk.Tk.__init__(self)
        #setting the size of the tkinter box that appears
        self.geometry('600x600+0+0')
        #creating a label to instruct the user what to do
        w = tk.Label(self, text="Enter your text here:")
        w.pack(anchor=CENTER, side=TOP)
        #creating a scrollable input text box
        self.ScrolledText = ScrolledText.ScrolledText(self)
        self.ScrolledText.pack(anchor=W, side=TOP, fill=X, expand = YES)
        #pressing the submit button calls the win2 method
        close_button = tk.Button(self, text="Submit", command=self.win2)
        close_button.pack(anchor=CENTER)
        self.string = ""
    #second text window called win2 gets created below first window and shows the required result in it    
    def win2(self):
        #obtaining the input string
        self.string = self.ScrolledText.get('1.0',END)
        #assigning the input string to a variable 'input_string'
        input_string= self.string
        #creating a scrollable text box where the result is shown
        self.ScrolledText = ScrolledText.ScrolledText(self)
        self.ScrolledText.pack(anchor=E, side=BOTTOM, fill=X, expand = YES)
        #Groups of bloom's taxonomy keywords and signal words stored as separate lists
        Description_Concept_Definition=["adapt","above","an example","appears to be","behind","belongs to","characteristics","defined as","for example","for instance","identified as","Imagine that","including","is a characteristic of","is a feature of","is like","looks like","most important","refers to","such as","to illustrate"]
        Procedure_Sequence=["after","afterward","at last","at the same time","before","during","eventually","finally","first","first of all","following","immediately","In the first place","initially","last","later","meanwhile","next","not long after","now","preceding","previously","recently","second","since","soon","then","third","to begin with","when","whenever"]
        Comparison_Contrast=["alike","also","although","as opposed to","as well as","both","comparatively","compared with","different from","Either","or","however","in common","in comparison","in contrast","in the same way","instead of","just as", "just like", "less than","like","likewise", "much as","nevertheless","on the other hand","opposite","same as","similar","similar too", "similarly","though","unlike","whereas","yet" ]
        Cause_Effect=["accordingly","as a consequence","as a result of","as illustrated by","because","because of","consequently","due to","effect of","for","for this reason","hence","if.... then","in conclusion","in order","is caused by","leads to","reasons why","since,.... therefore","so that","therefore","thus"]
        Problem_Solution_Presentation=["Dilemma is","For the given question","One solution can be","problem is","Question is","response","solution","The puzzle is","The result would be","to fix the problem","To solve this"] 
        Remember_Knowledge=["choose","define","find","how","label","list","match","name","omit","recall","relate","select","show","spell","tell","what","when","where","which","who","why"]
        Comprehension_Understand=["classify","compare","contrast","demonstrate","explain","extend","illustrate","infer","interpret","outline","relate","rephrase","show","summarize","translate"]
        Application=["apply","build","choose","construct","develop","experiment with","identify","interview","make use of","model","organize","plan","select","solve","utilize"]
        Analysis=["analyze","assume","categorize","classify","compare","conclusion","contrast","discover","dissect","distinguish","divide","examine","function","inference","inspect","list","motive","relationships","simplify","survey","take part in","test for","theme"]
        Evaluation=["agree","appraise","assess","award","choose","compare","conclude","criteria","criticize","decide","deduct","defend","determine","disprove","estimate","evaluate","explain","importance","influence","interpret","judge","justify","mark","measure","opinion","perceive","prioritize","prove","rate","recommend","rule on","select","support","value"]
        Synthesis_Create=["adapt","build","change","choose","combine","compile","compose","construct","create","delete","design","develop","discuss","elaborate","estimate","formulate","happen","imagine","improve","invent","make up","maximize","minimize","modify","original","originate","plan","predict","propose","solution","solve","suppose","test","theory"] 
        #initializing counter variables for each group as zero
        DCDco=0
        PSco=0
        CCco=0
        CEco=0
        PSolco=0
        Rco=0
        Uco=0
        Apco=0
        Anco=0
        Eco=0
        Crco=0
        #counting the number of words from each group present in the input string
        for i in range(0,len(Description_Concept_Definition)):
            if Description_Concept_Definition[i] in input_string:
                DCDco=DCDco+1
        for i in range(0,len(Procedure_Sequence)):
            if Procedure_Sequence[i] in input_string:
                PSco=PSco+1
        for i in range(0,len(Comparison_Contrast)):
            if Comparison_Contrast[i] in input_string:
                CCco=CCco+1
        for i in range(0,len(Cause_Effect)):
            if Cause_Effect[i] in input_string:
                CEco=CEco+1
        for i in range(0,len(Problem_Solution_Presentation)):
            if Problem_Solution_Presentation[i] in input_string:
                PSolco=PSolco+1
        for i in range(0,len(Remember_Knowledge)):
            if Remember_Knowledge[i] in input_string:
                Rco=Rco+1
        for i in range(0,len(Comprehension_Understand)):
            if Comprehension_Understand[i] in input_string:
                Uco=Uco+1
        for i in range(0,len(Application)):
            if Application[i] in input_string:
                Apco=Apco+1
        for i in range(0,len(Analysis)):
            if Analysis[i] in input_string:
                Anco=Anco+1
        for i in range(0,len(Evaluation)):
            if Evaluation[i] in input_string:
                Eco=Eco+1
        for i in range(0,len(Synthesis_Create)):
            if Synthesis_Create[i] in input_string:
                Crco=Crco+1
        #finding the total number of bloom's taxonomy keywords present        
        blsum=Rco+Uco+Apco+Anco+Eco+Crco
        #if the total number of bloom's taxonomy keywords is greater than zero the further operations on bloom's taxonomy keywords are carried out 
        if blsum>0:
            #calculating the percentage of each group present in the input string
            Rcop=Rco/blsum*100
            Ucop=Uco/blsum*100
            Apcop=Apco/blsum*100
            Ancop=Anco/blsum*100
            Ecop=Eco/blsum*100
            Crcop=Crco/blsum*100
            #printing the output in a tabular form
            data = [["Bloom's Taxonomy Keywords", "Count", "Percentage(%)"],['Remember Knowledge', Rco, Rcop],['Comprehension Understand', Uco, Ucop],['Application', Apco, Apcop],['Analysis', Anco, Ancop],['Evaluation', Eco, Ecop],['Synthesis Create', Crco, Crcop]]
            dash = '-' * 60

            for i in range(len(data)):
                if i == 0:
                    self.ScrolledText.insert(END, dash)
                    self.ScrolledText.insert(END, '\n')
                    self.ScrolledText.insert(END, '{:<35s}{:<15s}{:<12s}'.format(data[i][0],data[i][1],data[i][2]))
                    self.ScrolledText.insert(END, '\n')
                    self.ScrolledText.insert(END, dash)
                    self.ScrolledText.insert(END, '\n')
                else:
                    self.ScrolledText.insert(END, '{:<35s}{:<15d}{:<12f}'.format(data[i][0],data[i][1],data[i][2]))
                    self.ScrolledText.insert(END, '\n')
        #total number of signal words is calculated
        sigsum=DCDco+PSco+CCco+CEco+PSolco 
        #if the total number of signal words is greater than zero then further operations on signal words are carried out
        if sigsum>0:
            #calculating the percentage of each group present in the input string
            DCDp=DCDco/sigsum*100
            PSp=PSco/sigsum*100            
            CCp=CCco/sigsum*100
            CEp=CEco/sigsum*100
            PSolp=PSolco/sigsum*100
            #printing the output in a tabular form
            data2 = [["Signal words", "Count", "Percentage(%)"],['Description Concept Definition', DCDco, DCDp],['Procedure of Sequence', PSco, PSp],['Comparison Contrast', CCco, CCp],['Cause Effect Explanation', CEco, CEp],['Problem solution presentation', PSolco, PSolp]]
            dash = '-' * 60

            for j in range(len(data2)):
                if j == 0:
                    self.ScrolledText.insert(END, dash)
                    self.ScrolledText.insert(END, '\n')
                    self.ScrolledText.insert(END, '{:<35s}{:<15s}{:<12s}'.format(data2[j][0],data2[j][1],data2[j][2]))
                    self.ScrolledText.insert(END, '\n')
                    self.ScrolledText.insert(END, dash)
                    self.ScrolledText.insert(END, '\n')
                else:
                    self.ScrolledText.insert(END, '{:<35s}{:<15d}{:<12f}'.format(data2[j][0],data2[j][1],data2[j][2]))
                    self.ScrolledText.insert(END, '\n')
            

    #defining the mainloop method
    def mainloop(self):
        tk.Tk.mainloop(self)
        return self.string
#creating an instance of class called MyApp
MyApp()
#calling mainloop 
mainloop()
