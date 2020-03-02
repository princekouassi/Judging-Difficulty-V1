from __future__ import print_function
from __future__ import division
from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import time
import copy
import math
import random
import numpy
from array import array
import datetime
from psychopy import prefs
prefs.general['audioLib'] = ['pygame']
from psychopy import visual,core,data,event,gui
from psychopy import sound
from psychopy.constants import *  # things like STARTED, FINISHED
import csv

########################################################################################
# Draw a box to get experiment and participant information
########################################################################################
expName = u'Flashing_grid_task'  # Name the experiment
expInfo = {u'Session': u'001', u'Participant': u'001'} # What the box should ask for
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName) # Draw the bloody box!
if dlg.OK == False: core.quit() # If "cancel" is clicked end the whole thing
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
########################################################################################
########################################################################################


########################################################################################
# Where To Write File
########################################################################################
# Setup files for saving
if not os.path.isdir('JD_task_results'): # Create this folder wherever this script is saved
    os.makedirs('JD_task_results')  # If this fails (e.g. permissions) we will get error
filename = 'JD_Task_' + '%s_%s' %(expInfo['Participant'], expInfo['date'])+'.txt'
print('filename used for data is ' +filename)
########################################################################################
########################################################################################


########################################################################################
# Define the window
########################################################################################
# flag for 'escape' or other condition => quit the exp
endExpNow = False

# Setup the Window
win = visual.Window(fullscr=True, screen=0, allowGUI=True, allowStencil=False,
    monitor='testMonitor', color='grey', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='cm')
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess 
########################################################################################
########################################################################################


########################################################################################
# Changeable experimental parameters
########################################################################################
# Number of experimental trials
singletrials = 2     # **Number of single grid trials per colour_order block which should be set to 40 in the real experiment**
pairedtrials = 4     #320   # **Number of TOTAL paired grid trials should be set to 320 in the real experiment!**
practicetrials = 6    # Number of practice trials for single AND paired grid trials
pairedtrialsreal = 4 #80    # **Number of ACTUAL paired grid trials per block and should be set to 80 in the real experiment!**
numtrials = practicetrials+singletrials # The calculated TOTAL amount of practice and experimental single grid trials 
numtrials2 = practicetrials+pairedtrials# The calculated TOTAL amount of practice and experimental paired grid trials
block_split = pairedtrials/2

# Text size:
textsize = 0.7

# Fixation cross:
fcross = visual.TextStim(win, text="+")

# The total number of tirals for the paired grid coniditons:
sumtotal = 2 # This should be the same number as pairedtrials

# Block seperation text
sep_text ='''The last block of the experiment will now begin'''
seperation_text = visual.TextStim(win, text=sep_text, height=textsize)

####################
# Single trials text s1
####################
# Introduction text
one01 = '''During the experiment you will be presented with single and paired grid trials. During single grid trials, you will be presented with a sequence of trials each containing one flashing grid made up of a random number of blue and orange patches. An example grid is shown below.'''
introtext01 = visual.TextStim(win, text=one01,pos=(0.9, 11), height=textsize)  
one111 = '''Before each set of single grid tirals you will be asked if there are either more Blue or Orange patches in the grid, which you must then answer on subsequent trials.'''
introtext019 = visual.TextStim(win, text=one111,pos=(0.9, 6), height=textsize) 
one1112 = '''E.g. for the example grid below you may be asked: "Does the grid have more Blue than Orange patches? Press 'z' for YES or 'm' for NO."'''
introtext0191 = visual.TextStim(win, text=one1112,pos=(0.5, 2), height=textsize) 
one1113 = '''Press the spacebar to continue...'''
introtext0192 = visual.TextStim(win, text=one1113,pos=(0.3, -9), height=textsize) 
# Introduction text 2.0
one0001 = '''For section 2 of the block, on each trial you will be shown two flashing grids with varying distances between the grids. Both grids will have a randomly assigned proportion of blue to orange patches. Your task on each tiral of this section of the block is to make a judgement on the proportion of colours in both grids. You will be given practice trials before each section. PRESS ANY KEY ON THE KEYBOARD TO CONTINUE...'''
introtext0001 = visual.TextStim(win, text=one0001, height=textsize)
# Practice text:
practice01 = '''Practice for single grid trials will now begin. For these practice trials you must answer the following question on each trial: Does the grid have more Blue than Orange Patches? Press "z" for YES or "m" for NO.'''
practicetext1 = visual.TextStim(win, text=practice01,pos=(0,3), height=textsize) 
# Practice text:
practice0199 = '''Press any key on the keyboard to begin the practice trials...'''
practicetext17 = visual.TextStim(win, text=practice0199,pos=(-0.5,-0.5), height=textsize)
# End of first part of the experiment text
two01 = '''Single grid trials have now finished.'''
endtext01 = visual.TextStim(win, text=two01,pos=(-2.8,1.5), height=textsize)  
two010 = '''Press any key on the keyboard to continue...'''
endtext010 = visual.TextStim(win, text=two010,pos=(-1.4,0), height=textsize) 





# Practice trials for blue
prac001bf = '''Practice trials for single grid trials have now finished.'''
endspractice_bf = visual.TextStim(win, text=prac001bf,pos=(-0.7,3), height=textsize) 
prac001b1 = '''On the next set of trials you must answer the following question: Does the grid have more Blue than Orange Patches? Press "z" for YES or "m" for NO.'''
endspractice_b1 = visual.TextStim(win, text=prac001b1,pos=(-0.5,0), height=textsize) 
prac001b2 = '''Press any key on the keyboard to begin the actual trials...'''
endspractice_b2 = visual.TextStim(win, text=prac001b2,pos=(-0.8,-3), height=textsize) 
# Practice trials for orange
prac001of = '''Practice trials for single grid trials have now finished.'''
endspractice_of = visual.TextStim(win, text=prac001of,pos=(-0.7,3), height=textsize) 
prac001o1 = '''On the next set of trials you must answer the following question: Does the grid have more Orange than Blue Patches? Press "z" for YES or "m" for NO.'''
endspractice_o1 = visual.TextStim(win, text=prac001o1,pos=(-0.5,0), height=textsize) 
prac001o2 = '''Press any key on the keyboard to begin the actual trials...'''
endspractice_o2 = visual.TextStim(win, text=prac001o2,pos=(-0.8,-3), height=textsize) 
# Break text
breaktext01 = '''You are now on a break. Press any key on the keyboard to end your break and continue with the task immediately ...'''
breaktext = visual.TextStim(win, text=breaktext01, height=textsize) 
# Text on each trial for single grid trials
sttextb = '''Does the grid have more Blue than Orange patches? Press "z" for YES or "m" for NO.'''
strialtextb =blockonetext = visual.TextStim(win, text=sttextb, pos=(0, 6), height=textsize)
# Text on each trial for single grid trials
sttexto = '''Does the grid have more Orange than Blue patches? Press "z" for YES or "m" for NO.'''
strialtexto =blockonetext = visual.TextStim(win, text=sttexto, pos=(0, 6), height=textsize)
# Correct practice trial text:
cres = '''CORRECT'''
correct_res =blockonetext = visual.TextStim(win, text=cres, pos=(0,0), height=1)
# Inccorect practice trial text:
icres = '''INCORRECT'''
incorrect_res =blockonetext = visual.TextStim(win, text=icres, pos=(0,0), height=1)

####################
####################

####################
# Paired trials text s1
####################
# Introduction text
one = '''Introduction text here.'''
introtext = visual.TextStim(win, text=one, height=textsize)  

# End of experiment text
two = '''Please wait...'''
endtext = visual.TextStim(win, text=two, height=textsize)  

# End of the whole experiment text 
two22 = '''The experiment has now finished!'''
endtext1 = visual.TextStim(win, text=two22, height=textsize)  

# Section 2 practice trials text:
section2prac = '''Practice trials for paired grid trials will now begin. PRESS ANY KEY ON THE KEYBOARD TO BEGIN THE PRACTICE TRIALS...'''
section2practice = visual.TextStim(win, text=section2prac, height=textsize)

# Text on each trial for paired grid BLUE trials
ttext = '''Are there more Blue than Orange patches in both grids?  Press "z" for YES or "m" for NO.'''
trialtextb =blockonetext = visual.TextStim(win, text=ttext, pos=(0, 6), height=textsize)

# Text on each trial for paired grid ORANGE trials
ttexto = '''Are there more Orange than Blue patches in both grids?  Press "z" for YES or "m" for NO.'''
trialtexto =blockonetext = visual.TextStim(win, text=ttexto, pos=(0, 6), height=textsize)

####################
####################

####################
# Paired trials text
####################

# Seperation text after block 1:
sep_text ='''The last block of the experiment will now begin. Press any key on the keyboard to start the last block of the experiment...'''
seperation_text = visual.TextStim(win, text=sep_text, height=textsize)

####################
####################

####################
# Single trials text s2
####################
# Introduction text
one01e = '''On the next set of trials you must answer the following question: Does the grid have more Blue than Orange Patches? Press "z" for Yes or "m" for NO.'''
introtext0122b = visual.TextStim(win, text=one01e,pos=(0.3,2.5), height=textsize)  
one01ee = '''Press any key on the keyboard to begin the trials...'''
introtext0122bb = visual.TextStim(win, text=one01ee,pos=(-0.2,-1), height=textsize)  
one01et = '''On the next set of trials you must answer the following question: Does the grid have more Orange than Blue Patches? Press "z" for Yes or "m" for NO.'''
introtext0122o = visual.TextStim(win, text=one01et,pos=(0.3,2.5), height=textsize)  
one01eet = '''Press any key on the keyboard to begin the trials...'''
introtext0122oo = visual.TextStim(win, text=one01eet,pos=(-0.2,-1), height=textsize)  
# Practice text:
practice01 = '''Practice trials for section 1 of block 2 will now begin. PRESS ANY KEY ON THE KEYBOARD TO BEGIN THE PRACTICE TRIALS...'''
practicetext122 = visual.TextStim(win, text=practice01, height=textsize) 
# End of first part of the experiment text
two01 = '''Single grid trials have now finshed.'''
endtext0122 = visual.TextStim(win, text=two01,pos=(-1.7,0.5), height=textsize)  
two019 = '''Press any key on the keyboard to continue...'''
endtext01229 = visual.TextStim(win, text=two019,pos=(-0.2,-1), height=textsize)  
# Practice trials
prac001 = '''Practice trials for Section 1 of block 2 have now ended. Press any key on the keyboard to begin the actual trials for section 1 of block 2...'''
endspractice22 = visual.TextStim(win, text=prac001, height=textsize) 
# Break text
breaktext01 = '''You are now on a break. Press any key on the keyboard to end your break and continue with the task immediately...'''
breaktext = visual.TextStim(win, text=breaktext01, height=textsize) 
# Text on each trial for single grid trials
sttextb = '''Does the grid have more Blue than Orange patches? Press "z" for YES or "m" for NO.'''
strialtextb =blockonetext = visual.TextStim(win, text=sttextb, pos=(0, 6), height=textsize)
# Text on each trial for single grid trials
sttexto = '''Does the grid have more Orange than Blue patches? Press "z" for YES or "m" for NO.'''
strialtexto =blockonetext = visual.TextStim(win, text=sttexto, pos=(0, 6), height=textsize)
# Correct practice trial text:
cres = '''CORRECT'''
correct_res =blockonetext = visual.TextStim(win, text=cres, height=1)
# Inccorect practice trial text:
icres = '''INCORRECT'''
incorrect_res =blockonetext = visual.TextStim(win, text=icres, height=1)
# Practice trials
prac002 = '''Practice for paired grid trials has now finished.'''
endspractice2 = visual.TextStim(win, text=prac002,pos=(0,1.8), height=textsize) 

prac0020 = '''Press any key on the keyboard to begin the actual paired grid trials...'''
endspractice20 = visual.TextStim(win, text=prac0020, pos=(-0.3,0), height=textsize) 

####################
####################

####################
# Paired trials text s2
####################
# Introduction text
one = '''Introduction text here.'''
introtext = visual.TextStim(win, text=one, height=textsize)  

# End of experiment text
two = '''Please take a short break now, before continuing ...'''
endtext = visual.TextStim(win, text=two, height=textsize)  
# End of the whole experiment text 
two22 = '''The experiment has now finished!'''
endtext1 = visual.TextStim(win, text=two22, height=textsize)  
# Section 2 practice trials text:
section2prac = '''During paired grid trials, you will be presented with a sequence of trials each containing two flashing grids made up of a random number of blue and orange patches. Example grids are shown below.'''
section2practice22i = visual.TextStim(win, text=section2prac,pos=(0.9, 11), height=textsize)
one111t = '''Before each set of tirals you will be asked if there are either more Blue or Orange patches in both grids, which you must then answer on subsequent trials.'''
section2practice22ii = visual.TextStim(win, text=one111t,pos=(1.2, 6), height=textsize) 
one1112t = '''E.g. for the example grids below you may be asked: "Are there more Orange than Blue patches in both grids? Press "z" for YES or "m" for NO."'''
section2practice22iii = visual.TextStim(win, text=one1112t,pos=(1.2, 2), height=textsize) 
one1113t = '''Press the spacebar to continue...'''
section2practice22iiii = visual.TextStim(win, text=one1113t,pos=(0.3, -10), height=textsize) 
practice01r = '''Practice trials for paired grids will now begin. For these practice trials you must answer the following question on each trial: Do both grids seperately have more Orange than Blue Patches? Press "z" for YES and "m" for NO.'''
practicetext1q = visual.TextStim(win, text=practice01r,pos=(0,3), height=textsize) 
# Practice text:
practice0199r = '''Press any key on the keyboard to begin the practice trials...'''
practicetext1qq = visual.TextStim(win, text=practice0199r,pos=(-0.5,0), height=textsize)
# Text on each trial for paired grid BLUE trials
ttext = '''Are there more Blue than Orange patches in both grids?  Press "z" for YES or "m" for NO.'''
trialtextb =blockonetext = visual.TextStim(win, text=ttext, pos=(0, 6), height=textsize)
# Text on each trial for paired grid ORANGE trials
ttexto = '''Are there more Orange than Blue patches in both grids?  Press "z" for YES or "m" for NO.'''
trialtexto =blockonetext = visual.TextStim(win, text=ttexto, pos=(0, 6), height=textsize)

# Block one intro text
bb1 = '''During the next set of trials two grids will be presented on screen with a moderate amount of seperation between them. On each trial you must answer the following question: Are there more Blue than Orange patches in both grids?  Press "z" for YES or "m" for NO.'''
blockonetext = visual.TextStim(win, text=bb1,pos=(0.3,2.5), height=textsize) 

# Block three intro text
bb3 = '''During the next set of trials two grids will be presented on screen with a moderate amount of seperation between them. On each trial you must answer the following question: Are there more Orange than Blue patches in both grids?  Press "z" for YES or "m" for NO.'''
blockthirdtext = visual.TextStim(win, text=bb3,pos=(0.3,2.5), height=textsize) 

# Block two intro text
bb2 = '''During the next set of trials two grids will be presented on screen close together. On each trial you must answer the following question: Are there more Orange than Blue patches in both grids?  Press "z" for YES or "m" for NO.'''
blocktwotext = visual.TextStim(win, text=bb2,pos=(0,2.5), height=textsize)

# Block four intro text
bb4 = '''During the next set of trials two grids will be presented on screen close together. On each trial you must answer the following question: Are there more Blue than Orange patches in both grids?  Press "z" for YES or "m" for NO.'''
blockfourthtext = visual.TextStim(win, text=bb4,pos=(0,2.5), height=textsize)

# Practice trials
prac002 = '''Practice trials for Section 2 of block 2 have now finished. Press any key on the keyboard to begin the actual trials for Section 2...'''
endspractice222 = visual.TextStim(win, text=prac002,pos=(0,0), height=textsize)  
# introduction to section 2 of block 2
sec2sec = '''Another set of paired grid trials will now begin.'''
sec_2 = visual.TextStim(win, text=sec2sec,pos=(0,2), height=textsize) 
sec2sec9 = '''Press any key on the key board to begin the trials...'''
sec_29 = visual.TextStim(win, text=sec2sec9,pos=(-0.3,0), height=textsize) 
# Block one intro text
bb150 = '''Press any key on the keyboard to begin the trials...'''
blockonetext150 = visual.TextStim(win, text=bb150,pos=(-0.3,-1), height=textsize) 
####################
####################


# Orange:
color1 = [0.9686,0.6392,0.0353]
# Blue:
color2 = [-0.8980,1.0000,1.0000] 

# Define some clocks
checkclock01 = core.Clock() # For single grid trials     S1
checkclock = core.Clock() # For paired grid trials       P1
checkclock01s2 = core.Clock() # For single grid trials   S2
checkclock = core.Clock() # For paired grid trials       P2
########################################################################################
########################################################################################


########################################################################################
# List That Will Record Responses & RTs
########################################################################################
# For single grid trials s1
keyspressed = []*singletrials
correctresponse = []*singletrials
RT =[]*singletrials
trialNo = []*singletrials
conused = []*singletrials
difflevel = []*singletrials
colourcolour1 = []*singletrials

# For single grid trials s2
keyspressed2 = []*singletrials
correctresponse2 = []*singletrials
RT2 =[]*singletrials
trialNo2 = []*singletrials
conused2 = []*singletrials
difflevel2 = []*singletrials
colourcolour2 = []*singletrials

# For single grid trials s3
keyspressed3 = []*singletrials
correctresponse3 = []*singletrials
RT3 =[]*singletrials
trialNo3 = []*singletrials
conused3 = []*singletrials
difflevel3 = []*singletrials
colourcolour3 = []*singletrials

# For single grid trials s4
keyspressed4 = []*singletrials
correctresponse4 = []*singletrials
RT4 =[]*singletrials
trialNo4 = []*singletrials
conused4 = []*singletrials
difflevel4 = []*singletrials
colourcolour4 = []*singletrials

# Initilise the colour variable:
colour = []
########################################################################################
########################################################################################

########################################################################################
# Set the conditions for the single grid trials - JUDGING PROPORTIONS:
########################################################################################
con1 = (1)
con2 = (2)
con3 = (3)
con4 = (4)
con5 = (5)

# Define the blue and orange block signle grid trials:
single_proportions = []


for i in range(10):
# The single grid trials for the blue block:
    single_proportions.append(con1)
    single_proportions.append(con2)
    single_proportions.append(con3)
    single_proportions.append(con4)
np.random.shuffle(single_proportions)

# Conditions for practice trials:
singlegridpractice = [1,5,3,4,7,8]
np.random.shuffle(singlegridpractice) # Randomly shuffle single grid practice trials


# Create and shuffle which colour block participants will see first:
colour_order = [1,2] # 1 is the colour blue and 2 is the colour orange
np.random.shuffle(colour_order)
########################################################################################
########################################################################################


########################################################################################
########################################################################################
########################################################################################
# Paired Grid INTRODUCTION
########################################################################################
########################################################################################
########################################################################################
# Initialize components for Routine "init_experiment"
init_experimentClock = core.Clock()
# set_colors()
# Colors used during the experiment.s
def set_colors():
    global sc_c # screen color
    global f_c # frame color
    global sq_c # square color
    # 1 = white
    # -0.06 = grey 80
    # -0.37 = grey 120
    # -1 = black
    sc_c = 1
    f_c = -0.06
    sq_c = -0.37
    t_c = -0.06

# set_sizes()
# Sizes used during the experiment
def set_sizes():
    global f_s # frame size (square) (frame surrounding the stimulus)
    global sq_s # square size (square where the stimulus is shown)
    global l_s # line size (the width of the line surrounding the stimulus)
    f_s = 540
    sq_s = 800
    l_s = 100


########################################################################################
########################################################################################

########################################################################################
# Set main conditions and loop
########################################################################################
for i in range(1):
     
    p1=.70 # How much orange for the first grid (we want more blue here for easy trials: 70/30)
    p2=.48 # How much orange for the second grid (we want more orange here for hard trials: 52/48)

    leftside  = [-6,-5]
    rightside = [6,-5]
    
    # Set the position of left stimulus
    def set_positions():
        global fl_p # Where should the flash be drawn
        fl_p = leftside
            
    # Set the position of right stimulus
    def set_positions2():
        global fl_p2 # Where should the flash be drawn
        fl_p2 = rightside
        
    # flash stimulus functions
    # flash initialization
    def flash_init(win, position=[0,0], position2=[0,0], square_size=10, columns=20, rows=20, percent_color1=p1, percent_color2=p2): # Colour 1 being manipulated
        global flash # The flash stimulus (an array of flashing squares)
        global flash2
        color_set = [color2, color1]   # BLUE
        color_set2 = [color2, color1]  # BLUE
        cell_number = columns * rows
    
        num_color1 = int(np.floor(float(cell_number)*percent_color1)) # First colour
        num_color2 = int(np.floor(float(cell_number)*(1-percent_color1))) # Second f
    
        num_color3 = int(np.floor(float(cell_number)*percent_color2)) # First colour
        num_color4 = int(np.floor(float(cell_number)*(1-percent_color2))) # Second f
        
        #print(cell_number,num_color1,num_color2)
        
        # fill an array with colors. Each color should appear approximatively the same number of times.
        f_colors = []
        for i in range(num_color1):
            f_colors.append(color_set[0])
        for i in range(num_color2):
            f_colors.append(color_set[1])
        numpy.random.shuffle(color_set)
        i = cell_number - len(f_colors)
        while i > 0:
            f_colors.append(color_set[i])
            i -= 1
        
        f_colors2 = []
        for i in range(num_color3):
            f_colors2.append(color_set2[0])
        for i in range(num_color4):
            f_colors2.append(color_set2[1])
        numpy.random.shuffle(color_set2)
        i = cell_number - len(f_colors2)
        while i > 0:
            f_colors2.append(color_set2[i])
            i -= 1
        
        # randomize color order.
        shuffle(f_colors)
        shuffle(f_colors2)
        
        # fill an array with coordinate for each color square. First square should be at the upper left
        # and next should follow from left to right and up to down.
        xys = []
        x_left = (1 - columns) * square_size / 2
        y_top = (1 - rows) * square_size / 2
        for l in range(rows):
            for c in range(columns):
                xys.append((x_left + c * square_size, y_top + l * square_size))
        
        
        # fill an array with coordinate for each color square. First square should be at the upper left
        # and next should follow from left to right and up to down.
        xys2 = []
        x_left = (1 - columns) * square_size / 2
        y_top = (1 - rows) * square_size / 2
        for l in range(rows):
            for c in range(columns):
                xys2.append((x_left + c * square_size, y_top + l * square_size))
        
        # MAIN FUNCTION TO CREATE FIRST GRID
        flash = visual.ElementArrayStim(win=win,
                            fieldPos=position,
                            fieldShape='sqr',
                            nElements=cell_number,
                            sizes=square_size,
                            xys=xys,
                            colors=f_colors,
                            elementTex=None,
                            elementMask=None,
                            name='flash',
                            autoLog=False)
                            
        # MAIN FUNCTION TO CREATE SECOND GRID
        flash2 = visual.ElementArrayStim(win=win,
                        fieldPos=position2,
                        fieldShape='sqr',
                        nElements=cell_number,
                        sizes=square_size,
                        xys=xys2,
                        colors=f_colors2,
                        elementTex=None,
                        elementMask=None,
                        name='flash',
                        autoLog=False)
                            
                            
    
    # flash stimulus change
    def flash_change():
        global flash
        shuffle(flash.colors)
        flash.setColors(flash.colors)
    
    def flash2_change():
        global flash2
        shuffle(flash2.colors)
        flash2.setColors(flash2.colors)
    
    # Time variables used during the experiment
    def set_timing():
        global f_t 
        f_t = 5 # The duration (in frame) of a flash image presentation
    
    # data_init
    set_colors()
    set_sizes()
    set_positions()
    set_positions2()
    set_timing()
    
    #############################
    # MAIN FUNCTION HERE
    flash_init(win, fl_p, fl_p2, square_size=0.3, columns=20, rows=20) # set the parameters here for the function!!
    #############################
    
    # Initialize components for Routine "show_flash"
    show_flashClock = core.Clock()
    frame_fl = visual.ImageStim(win=win, name='frame_fl',
        image=None, mask=None,
        ori=0, pos=fl_p, size=f_s,
        color=f_c, colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=0.0)
    
    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 
    
    #------Prepare to start Routine "init_experiment"-------
    t = 0
    frameN = -1
    
    #------Prepare to start Routine "show_flash"-------
    t = 0
    show_flashClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    # flash begin routine
    f_change = 0
    
    # keep track of which components have finished
    show_flashComponents = []
    show_flashComponents.append(frame_fl)
    for thisComponent in show_flashComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    ########################################################################################
    ########################################################################################

    #---Start Routine "show_flash"-------
    continueRoutine = True
    while continueRoutine:
        # Hides mouse
        mouse = event.Mouse(visible=0)
        
        # get current time
        t = show_flashClock.getTime()
        #print("t =", t)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        
        # update/draw components on each frame
        #print(frameN)
        
        # *frame_fl* updates
        if t >= 0.0 and frame_fl.status == NOT_STARTED:
            # keep track of start time/frame for later
            frame_fl.tStart = t  # underestimates by a little under one frame
            frame_fl.frameNStart = frameN  # exact frame index
            frame_fl.draw()
        # flash each frame
        if frameN >= f_change:
            flash_change()
            flash2_change()
            f_change += f_t
        
        section2practice22i.draw() # Draw ending message here
        section2practice22ii.draw() # Draw ending message here
        section2practice22iii.draw() # Draw ending message here
        section2practice22iiii.draw() # Draw ending message here
        flash.draw()  # First stimulus is drawn here
        flash2.draw() # Second stimulus is drawn here
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in show_flashComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        if event.getKeys(keyList=["space"]):
            break
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
            
#-------Ending Routine "show_flash"-------
for thisComponent in show_flashComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
        
win.flip()
practicetext1q.draw()
practicetext1qq.draw()
win.flip()
keypressed = event.waitKeys(timeStamped=False)
########################################################################################
########################################################################################


########################################################################################
########################################################################################
########################################################################################
# Single Grid Trials - JUDGING PROPORTIONS - BLOCK 1:
########################################################################################
########################################################################################
########################################################################################
# Initialize components for Routine "init_experiment"
init_experimentClock = core.Clock()
# set_colors()
# Colors used during the experiment.s
def set_colors():
    global sc_c # screen color
    global f_c # frame color
    global sq_c # square color
    # 1 = white
    # -0.06 = grey 80
    # -0.37 = grey 120
    # -1 = black
    sc_c = 1
    f_c = -0.06
    sq_c = -0.37
    t_c = -0.06

# set_sizes()
# Sizes used during the experiment
def set_sizes():
    global f_s # frame size (square) (frame surrounding the stimulus)
    global sq_s # square size (square where the stimulus is shown)
    global l_s # line size (the width of the line surrounding the stimulus)
    f_s = 540
    sq_s = 800
    l_s = 100
    
# Set the position of left stimulus
def set_positions01():
    global fl_p3 # Where should the flash be drawn
    fl_p3 = [0, 0]

########################################################################################
# Set main conditions and loop
########################################################################################

# Counter to keep track of things
counter = 0
thecount = 0
counter01 = 0
thecount01 = 0
pcounter = 1
pcounter2 = 1

# Set the colour order for the first colour block:
colour_order1 = colour_order[0]
for j in range(numtrials): # Should be set to 40 to make 80 in total over the whole experiment
    
    if pcounter <= practicetrials:
        singleconditionsx = singlegridpractice[pcounter-1]
        if singleconditionsx is 5 or singleconditionsx is 7 or singleconditionsx is 8:
            colour_order1 ==2
        else:
            colour_order1 == 1
    else:
        # Select what condition is to be performed on experimental trials:
        if colour_order1 == 1:
            singleconditionsx = single_proportions[counter01]
        elif colour_order1 == 2:
            singleconditionsx = single_proportions[counter01]
    
    
    if pcounter > practicetrials:
        # Append the condition we're on:
        if singleconditionsx == 1:
            conused.append('b,o')
            difflevel.append('Exp - Hard 1')
        elif singleconditionsx == 2:
            conused.append('B,o')
            difflevel.append('Con - Easy 1')
        elif singleconditionsx == 3:
            conused.append('o,b')
            difflevel.append('Exp - Hard 1')
        elif singleconditionsx == 4:
            conused.append('O,b') 
            difflevel.append('Con - Easy 1')
    
    # Set the conditions here:
    if singleconditionsx == 1:
        p01 = .52#(52/48) more blue
    elif singleconditionsx == 2:
        p01 = .70#(70/30) a lot more blue
    elif singleconditionsx == 3:
        p01 = .52#(52/48) more blue orange
    elif singleconditionsx == 4:
        p01 = .70#(70/30) a lot more orange
        
        
    # flash stimulus functions
    # flash initialization
    def flash_init(win, position01=[0,0], square_size=10, columns=20, rows=20, percent_color01=p01): # Colour2 being manipulated whic is BLUE
        global flash01 # The flash stimulus (an array of flashing squares)
        
        if singleconditionsx <= 2:
            color_set01 = [color2, color1] # color2 is being manipulated which is the BLUE
        elif singleconditionsx >= 3:
            color_set01 = [color1, color2] # colour1 is being manipulated which is the ORANGE
        cell_number = columns * rows
    
        num_color4 = int(np.floor(float(cell_number)*percent_color01)) # First colour
        num_color5 = int(np.floor(float(cell_number)*(1-percent_color01))) # Second colour
        
        # fill an array with colors. Each color should appear approximatively the same number of times.
        f_colors3 = []
        for i in range(num_color4):
            f_colors3.append(color_set01[0])
        for i in range(num_color5):
            f_colors3.append(color_set01[1])
        numpy.random.shuffle(color_set01)
        i = cell_number - len(f_colors3)
        while i > 0:
            f_colors3.append(color_set01[i])
            i -= 1
        
        # randomize color order.
        shuffle(f_colors3)
        
        # fill an array with coordinate for each color square. First square should be at the upper left
        # and next should follow from left to right and up to down.
        xys = []
        x_left = (1 - columns) * square_size / 2
        y_top = (1 - rows) * square_size / 2
        for l in range(rows):
            for c in range(columns):
                xys.append((x_left + c * square_size, y_top + l * square_size))
        
        
        # fill an array with coordinate for each color square. First square should be at the upper left
        # and next should follow from left to right and up to down.
        xys2 = []
        x_left = (1 - columns) * square_size / 2
        y_top = (1 - rows) * square_size / 2
        for l in range(rows):
            for c in range(columns):
                xys2.append((x_left + c * square_size, y_top + l * square_size))
        
        # MAIN FUNCTION TO CREATE FIRST GRID
        flash01 = visual.ElementArrayStim(win=win,
                            fieldPos=position01,
                            fieldShape='sqr',
                            nElements=cell_number,
                            sizes=square_size,
                            xys=xys,
                            colors=f_colors3,
                            elementTex=None,
                            elementMask=None,
                            name='flash',
                            autoLog=False)
                            
                            
                            
    
    # flash stimulus change
    def flash_change():
        global flash01
        shuffle(flash01.colors)
        flash01.setColors(flash01.colors)
    
    # Time variables used during the experiment
    def set_timing():
        global f_t 
        f_t = 5 # The duration (in frame) of a flash image presentation
    
    # data_init
    set_colors()
    set_sizes()
    set_positions01()
    set_timing()
    
    #############################
    # MAIN FUNCTION HERE
    flash_init(win, fl_p3, square_size=0.3, columns=20, rows=20) # set the parameters here for the function!!
    #############################
    
    # Initialize components for Routine "show_flash"
    show_flashClock01 = core.Clock()
    frame_fl = visual.ImageStim(win=win, name='frame_fl',
        image=None, mask=None,
        ori=0, pos=fl_p3, size=f_s,
        color=f_c, colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=0.0)
    
    # Create some handy timers
    globalClock01 = core.Clock()  # to track the time since experiment started
    routineTimer01 = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 
    
    #------Prepare to start Routine "init_experiment"-------
    t = 0
    frameN = -1
    
    #------Prepare to start Routine "show_flash"-------
    t = 0
    show_flashClock01.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    # flash begin routine
    f_change = 0
    
    # keep track of which components have finished
    show_flashComponents01 = []
    show_flashComponents01.append(frame_fl)
    for thisComponent in show_flashComponents01:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    ########################################################################################
    ########################################################################################
    
    
    ########################################################################################
    # MAIN EXPERIMENT
    ########################################################################################
    
    # Put up the introduction text 
    if pcounter == 1:
        
        win.flip()
        practicetext1.draw()
        practicetext17.draw()
        win.flip()
        keypressed = event.waitKeys(timeStamped=False)
        checkclock01.reset()
                    
                    
    if pcounter == practicetrials+1:
        if colour_order1 == 1:
            win.flip()
            endspractice_b1.draw()
            endspractice_b2.draw()
            endspractice_bf.draw()
            win.flip()
        elif colour_order1 == 2:
            win.flip()
            endspractice_o1.draw()
            endspractice_o2.draw()
            endspractice_of.draw()
            win.flip()
            
        keypressed = event.waitKeys(timeStamped=False)
        checkclock01.reset()
    
    #---Start Routine "show_flash"-------
    continueRoutine = True
    while continueRoutine:
            
        # Hides mouse
        mouse = event.Mouse(visible=0)
        
        # get current time
        t = show_flashClock01.getTime()
        #print("t =", t)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        
        # *frame_fl* updates
        if t >= 0.0 and frame_fl.status == NOT_STARTED:
            # keep track of start time/frame for later
            frame_fl.tStart = t  # underestimates by a little under one frame
            frame_fl.frameNStart = frameN  # exact frame index
            frame_fl.draw()
        # flash each frame
        if frameN >= f_change:
            flash_change()
            f_change += f_t
        flash01.draw()  # First stimulus is drawn here
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer01.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in show_flashComponents01:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        if pcounter <= practicetrials:
            if event.getKeys(keyList=["z"]):
                pcounter = pcounter+1
                if singleconditionsx is 5 or singleconditionsx is 7 or singleconditionsx is 8:
                    win.flip()
                    incorrect_res.draw()
                    win.flip()
                    core.wait(1.5) # Keep the cross on screen for 2 seconds
                else:
                    win.flip()
                    correct_res.draw()
                    win.flip()
                    core.wait(1.5) # Keep the cross on screen for 2 seconds
                win.flip() # Clears the window
                fcross.draw() # Draw the fixation cross
                win.flip() # Clears the window
                core.wait(1.5) # Keep the cross on screen for 2 seconds
                checkclock01.reset()
                break
            elif event.getKeys(keyList=["m"]):
                pcounter = pcounter+1
                if singleconditionsx is 5 or singleconditionsx is 7 or singleconditionsx is 8:
                    win.flip()
                    correct_res.draw()
                    win.flip()
                    core.wait(1.5) # Keep the cross on screen for 2 seconds
                else:
                    win.flip()
                    incorrect_res.draw()
                    win.flip()
                    core.wait(1.5) # Keep the cross on screen for 2 seconds
                win.flip() # Clears the window
                fcross.draw() # Draw the fixation cross
                win.flip() # Clears the window
                core.wait(1.5) # Keep the cross on screen for 2 seconds
                checkclock01.reset()
                break
        # For experimental trials:
        elif pcounter > practicetrials:
            # RESPONSE 1:
            if event.getKeys(keyList=["escape"]):
                win.flip()
                breaktext.draw()
                win.flip()
                keypressed = event.waitKeys(timeStamped=False)
                checkclock01.reset()
            if event.getKeys(keyList=["6"]):
                win.close()
                core.quit()
            if event.getKeys(keyList=["z"]): # MORE key
            
                # Update practice trial counter
                pcounter = pcounter+1
                
                # print the condition we did
                print("actual single trial done =", singleconditionsx)
                
                # Track response times
                #rt = rtclock.getTime()
                time01 = checkclock01.getTime()
                RT.append(time01)
                
                if colour_order1 == 1:
                    if singleconditionsx <= 2:
                        correctresponse.append('1')
                        print('response ===========  correct')
                    elif singleconditionsx >= 3:
                        correctresponse.append('0')
                        print('response ===========  incorrect')
                elif colour_order1 == 2:
                    if singleconditionsx <= 2:
                        correctresponse.append('0')
                        print('response ===========  incorrect')
                    elif singleconditionsx >= 3:
                        correctresponse.append('1')
                        print('response ===========  correct')
                # Append which colour question was being asked:
                colourcolour1.append(colour_order1)
                
                # Keep track of keys pressed
                keyspressed.append('left')
                
                # Update the counter
                counter01 = counter01+1
                
                # Keep track of trial number to be saved 
                trialNo.append(counter01)
                
                
                # DRAW FIXATION CROSS AFTER EACH TRIAL
                win.flip() # Clears the window
                fcross.draw() # Draw the fixation cross
                win.flip() # Clears the window
                core.wait(1.5) # Keep the cross on screen for 2 seconds
                checkclock01.reset()
                
                # END THE EXPERIMENT HERE AND SAVE DATA
                if counter01 == singletrials:
                    win.flip() # Clears the window
                    endtext01.draw() # Draw ending message here
                    endtext010.draw()
                    win.flip() # Clears the window
                    keypressed = event.waitKeys(timeStamped=False)
                break # End the expriment
                
             # RESPONSE 2: (Right Side)
            if event.getKeys(keyList=["m"]): # LESS key
                
                
                # Update practice trial counter
                pcounter = pcounter+1
                
                # print the condition we did
                print("actual single trial done =", singleconditionsx)
                
                time01 = checkclock01.getTime()
                RT.append(time01)
                
                if colour_order1 == 1:
                    if singleconditionsx <= 2:
                        correctresponse.append('0')
                        print('response ===========  incorrect')
                    elif singleconditionsx >= 3:
                        correctresponse.append('1')
                        print('response ===========  correct')
                elif colour_order1 == 2:
                    if singleconditionsx <= 2:
                        correctresponse.append('1')
                        print('response ===========  correct')
                    elif singleconditionsx >= 3:
                        correctresponse.append('0')
                        print('response ===========  incorrect')
                # Append which colour question was being asked:
                colourcolour1.append(colour_order1)
                
                # Keep track of keys pressed
                keyspressed.append('right')
                
                # Update the counter
                counter01 = counter01+1
                
                # Keep track of trial number to be saved 
                trialNo.append(counter01)
                
                
                # DRAW FIXATION CROSS AFTER EACH TRIAL
                win.flip() # Clears the window
                fcross.draw() # Draw the fixation cross
                win.flip() # Clears the window
                core.wait(1.5) # Keep the cross on screen for 2 seconds
                checkclock01.reset()
                
                # END THE EXPERIMENT HERE AND SAVE DATA
                if counter01 == singletrials:
                    win.flip() # Clears the window
                    endtext01.draw() # Draw ending message here
                    endtext010.draw()
                    win.flip() # Clears the window
                    keypressed = event.waitKeys(timeStamped=False)
                break # End the expriment
            
            
            
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
        
        # END THE EXPERIMENT HERE
        if counter01 == singletrials:
            win.flip() # Clears the window
            endtext01.draw() # Draw ending message here
            endtext010.draw()
            win.flip() # Clears the window
            keypressed = event.waitKeys(timeStamped=False)
            break
            
#-------Ending Routine "show_flash"-------
for thisComponent in show_flashComponents01:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
########################################################################################
########################################################################################

# Shuffle the single grid conditions again:
np.random.shuffle(single_proportions)

########################################################################################
########################################################################################
########################################################################################
# Single Grid Trials - JUDGING DIFFICULTY - BLOCK 1:
########################################################################################
########################################################################################
########################################################################################
# Initialize components for Routine "init_experiment"
init_experimentClock = core.Clock()
# set_colors()
# Colors used during the experiment.s
def set_colors():
    global sc_c # screen color
    global f_c # frame color
    global sq_c # square color
    # 1 = white
    # -0.06 = grey 80
    # -0.37 = grey 120
    # -1 = black
    sc_c = 1
    f_c = -0.06
    sq_c = -0.37
    t_c = -0.06

# set_sizes()
# Sizes used during the experiment
def set_sizes():
    global f_s # frame size (square) (frame surrounding the stimulus)
    global sq_s # square size (square where the stimulus is shown)
    global l_s # line size (the width of the line surrounding the stimulus)
    f_s = 540
    sq_s = 800
    l_s = 100
    
# Set the position of left stimulus
def set_positions01():
    global fl_p3 # Where should the flash be drawn
    fl_p3 = [0, 0]

########################################################################################
# Set main conditions and loop
########################################################################################

# Counter to keep track of things
counter = 0
thecount = 0
counter01 = 0
thecount01 = 0
pcounter = 1
pcounter2 = 1

# Set the colour order for the first colour block:
colour_order1 = colour_order[0]
for j in range(numtrials): # Should be set to 40 to make 80 in total over the whole experiment
    
    if pcounter <= practicetrials:
        singleconditionsx = singlegridpractice[pcounter-1]
        if singleconditionsx is 5 or singleconditionsx is 7 or singleconditionsx is 8:
            colour_order1 ==2
        else:
            colour_order1 == 1
    else:
        # Select what condition is to be performed on experimental trials:
        if colour_order1 == 1:
            singleconditionsx = single_proportions[counter01]
        elif colour_order1 == 2:
            singleconditionsx = single_proportions[counter01]
    
    
    if pcounter > practicetrials:
        # Append the condition we're on:
        if singleconditionsx == 1:
            conused2.append('b,o')
            difflevel2.append('Exp - Hard 1')
        elif singleconditionsx == 2:
            conused2.append('B,o')
            difflevel2.append('Con - Easy 1')
        elif singleconditionsx == 3:
            conused2.append('o,b')
            difflevel2.append('Exp - Hard 1')
        elif singleconditionsx == 4:
            conused2.append('O,b') 
            difflevel2.append('Con - Easy 1')
    
    # Set the conditions here:
    if singleconditionsx == 1:
        p01 = .52#(52/48) more blue
    elif singleconditionsx == 2:
        p01 = .70#(70/30) a lot more blue
    elif singleconditionsx == 3:
        p01 = .52#(52/48) more blue orange
    elif singleconditionsx == 4:
        p01 = .70#(70/30) a lot more orange
        
        
        
    # flash stimulus functions
    # flash initialization
    def flash_init(win, position01=[0,0], square_size=10, columns=20, rows=20, percent_color01=p01): # Colour2 being manipulated whic is BLUE
        global flash01 # The flash stimulus (an array of flashing squares)
        
        if singleconditionsx <= 2:
            color_set01 = [color2, color1] # color2 is being manipulated which is the BLUE
        elif singleconditionsx >= 3:
            color_set01 = [color1, color2] # colour1 is being manipulated which is the ORANGE
        cell_number = columns * rows
    
        num_color4 = int(np.floor(float(cell_number)*percent_color01)) # First colour
        num_color5 = int(np.floor(float(cell_number)*(1-percent_color01))) # Second colour
        
        # fill an array with colors. Each color should appear approximatively the same number of times.
        f_colors3 = []
        for i in range(num_color4):
            f_colors3.append(color_set01[0])
        for i in range(num_color5):
            f_colors3.append(color_set01[1])
        numpy.random.shuffle(color_set01)
        i = cell_number - len(f_colors3)
        while i > 0:
            f_colors3.append(color_set01[i])
            i -= 1
        
        # randomize color order.
        shuffle(f_colors3)
        
        # fill an array with coordinate for each color square. First square should be at the upper left
        # and next should follow from left to right and up to down.
        xys = []
        x_left = (1 - columns) * square_size / 2
        y_top = (1 - rows) * square_size / 2
        for l in range(rows):
            for c in range(columns):
                xys.append((x_left + c * square_size, y_top + l * square_size))
        
        
        # fill an array with coordinate for each color square. First square should be at the upper left
        # and next should follow from left to right and up to down.
        xys2 = []
        x_left = (1 - columns) * square_size / 2
        y_top = (1 - rows) * square_size / 2
        for l in range(rows):
            for c in range(columns):
                xys2.append((x_left + c * square_size, y_top + l * square_size))
        
        # MAIN FUNCTION TO CREATE FIRST GRID
        flash01 = visual.ElementArrayStim(win=win,
                            fieldPos=position01,
                            fieldShape='sqr',
                            nElements=cell_number,
                            sizes=square_size,
                            xys=xys,
                            colors=f_colors3,
                            elementTex=None,
                            elementMask=None,
                            name='flash',
                            autoLog=False)
                            
                            
                            
    
    # flash stimulus change
    def flash_change():
        global flash01
        shuffle(flash01.colors)
        flash01.setColors(flash01.colors)
    
    # Time variables used during the experiment
    def set_timing():
        global f_t 
        f_t = 5 # The duration (in frame) of a flash image presentation
    
    # data_init
    set_colors()
    set_sizes()
    set_positions01()
    set_timing()
    
    #############################
    # MAIN FUNCTION HERE
    flash_init(win, fl_p3, square_size=0.3, columns=20, rows=20) # set the parameters here for the function!!
    #############################
    
    # Initialize components for Routine "show_flash"
    show_flashClock01 = core.Clock()
    frame_fl = visual.ImageStim(win=win, name='frame_fl',
        image=None, mask=None,
        ori=0, pos=fl_p3, size=f_s,
        color=f_c, colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=0.0)
    
    # Create some handy timers
    globalClock01 = core.Clock()  # to track the time since experiment started
    routineTimer01 = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 
    
    #------Prepare to start Routine "init_experiment"-------
    t = 0
    frameN = -1
    
    #------Prepare to start Routine "show_flash"-------
    t = 0
    show_flashClock01.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    # flash begin routine
    f_change = 0
    
    # keep track of which components have finished
    show_flashComponents01 = []
    show_flashComponents01.append(frame_fl)
    for thisComponent in show_flashComponents01:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    ########################################################################################
    ########################################################################################
    
    
    ########################################################################################
    # MAIN EXPERIMENT
    ########################################################################################
    
    # Put up the introduction text 
    if pcounter == 1:
        
        win.flip()
        practicetext1.draw()
        practicetext17.draw()
        win.flip()
        keypressed = event.waitKeys(timeStamped=False)
        checkclock01.reset()
                    
                    
    if pcounter == practicetrials+1:
        if colour_order1 == 1:
            win.flip()
            endspractice_b1.draw()
            endspractice_b2.draw()
            endspractice_bf.draw()
            win.flip()
        elif colour_order1 == 2:
            win.flip()
            endspractice_o1.draw()
            endspractice_o2.draw()
            endspractice_of.draw()
            win.flip()
            
        keypressed = event.waitKeys(timeStamped=False)
        checkclock01.reset()
    
    #---Start Routine "show_flash"-------
    continueRoutine = True
    while continueRoutine:
            
        # Hides mouse
        mouse = event.Mouse(visible=0)
        
        # get current time
        t = show_flashClock01.getTime()
        #print("t =", t)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        
        # *frame_fl* updates
        if t >= 0.0 and frame_fl.status == NOT_STARTED:
            # keep track of start time/frame for later
            frame_fl.tStart = t  # underestimates by a little under one frame
            frame_fl.frameNStart = frameN  # exact frame index
            frame_fl.draw()
        # flash each frame
        if frameN >= f_change:
            flash_change()
            f_change += f_t
        flash01.draw()  # First stimulus is drawn here
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer01.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in show_flashComponents01:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        if pcounter <= practicetrials:
            if event.getKeys(keyList=["z"]):
                pcounter = pcounter+1
                if singleconditionsx is 5 or singleconditionsx is 7 or singleconditionsx is 8:
                    win.flip()
                    incorrect_res.draw()
                    win.flip()
                    core.wait(1.5) # Keep the cross on screen for 2 seconds
                else:
                    win.flip()
                    correct_res.draw()
                    win.flip()
                    core.wait(1.5) # Keep the cross on screen for 2 seconds
                win.flip() # Clears the window
                fcross.draw() # Draw the fixation cross
                win.flip() # Clears the window
                core.wait(1.5) # Keep the cross on screen for 2 seconds
                checkclock01.reset()
                break
            elif event.getKeys(keyList=["m"]):
                pcounter = pcounter+1
                if singleconditionsx is 5 or singleconditionsx is 7 or singleconditionsx is 8:
                    win.flip()
                    correct_res.draw()
                    win.flip()
                    core.wait(1.5) # Keep the cross on screen for 2 seconds
                else:
                    win.flip()
                    incorrect_res.draw()
                    win.flip()
                    core.wait(1.5) # Keep the cross on screen for 2 seconds
                win.flip() # Clears the window
                fcross.draw() # Draw the fixation cross
                win.flip() # Clears the window
                core.wait(1.5) # Keep the cross on screen for 2 seconds
                checkclock01.reset()
                break
        # For experimental trials:
        elif pcounter > practicetrials:
            # RESPONSE 1:
            if event.getKeys(keyList=["escape"]):
                win.flip()
                breaktext.draw()
                win.flip()
                keypressed = event.waitKeys(timeStamped=False)
                checkclock01.reset()
            if event.getKeys(keyList=["6"]):
                win.close()
                core.quit()
            if event.getKeys(keyList=["z"]): # MORE key
            
                # Update practice trial counter
                pcounter = pcounter+1
                
                # print the condition we did
                print("actual single trial done =", singleconditionsx)
                
                time01 = checkclock01.getTime()
                RT2.append(time01)
                
                if colour_order1 == 1:
                    if singleconditionsx <= 2:
                        correctresponse2.append('1')
                        print('response ===========  correct')
                    elif singleconditionsx >= 3:
                        correctresponse2.append('0')
                        print('response ===========  incorrect')
                elif colour_order1 == 2:
                    if singleconditionsx <= 2:
                        correctresponse2.append('0')
                        print('response ===========  incorrect')
                    elif singleconditionsx >= 3:
                        correctresponse2.append('1')
                        print('response ===========  correct')
                # Append which colour question was being asked:
                colourcolour2.append(colour_order1)
                
                # Keep track of keys pressed
                keyspressed2.append('left')
                
                # Update the counter
                counter01 = counter01+1
                
                # Keep track of trial number to be saved 
                trialNo2.append(counter01)
                
                
                # DRAW FIXATION CROSS AFTER EACH TRIAL
                win.flip() # Clears the window
                fcross.draw() # Draw the fixation cross
                win.flip() # Clears the window
                core.wait(1.5) # Keep the cross on screen for 2 seconds
                checkclock01.reset()
                
                # END THE EXPERIMENT HERE AND SAVE DATA
                if counter01 == singletrials:
                    win.flip() # Clears the window
                    endtext01.draw() # Draw ending message here
                    endtext010.draw()
                    win.flip() # Clears the window
                    keypressed = event.waitKeys(timeStamped=False)
                break # End the expriment
                
             # RESPONSE 2: (Right Side)
            if event.getKeys(keyList=["m"]): # LESS key
                
                
                # Update practice trial counter
                pcounter = pcounter+1
                
                # print the condition we did
                print("actual single trial done =", singleconditionsx)
                
                time01 = checkclock01.getTime()
                RT2.append(time01)
                
                if colour_order1 == 1:
                    if singleconditionsx <= 2:
                        correctresponse2.append('0')
                        print('response ===========  incorrect')
                    elif singleconditionsx >= 3:
                        correctresponse2.append('1')
                        print('response ===========  correct')
                elif colour_order1 == 2:
                    if singleconditionsx <= 2:
                        correctresponse2.append('1')
                        print('response ===========  correct')
                    elif singleconditionsx >= 3:
                        correctresponse2.append('0')
                        print('response ===========  incorrect')
                # Append which colour question was being asked:
                colourcolour2.append(colour_order1)
                
                # Keep track of keys pressed
                keyspressed2.append('right')
                
                # Update the counter
                counter01 = counter01+1
                
                # Keep track of trial number to be saved 
                trialNo2.append(counter01)
                
                
                # DRAW FIXATION CROSS AFTER EACH TRIAL
                win.flip() # Clears the window
                fcross.draw() # Draw the fixation cross
                win.flip() # Clears the window
                core.wait(1.5) # Keep the cross on screen for 2 seconds
                checkclock01.reset()
                
                # END THE EXPERIMENT HERE AND SAVE DATA
                if counter01 == singletrials:
                    win.flip() # Clears the window
                    endtext01.draw() # Draw ending message here
                    endtext010.draw()
                    win.flip() # Clears the window
                    keypressed = event.waitKeys(timeStamped=False)
                break # End the expriment
            
            
            
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
        
        # END THE EXPERIMENT HERE
        if counter01 == singletrials:
            win.flip() # Clears the window
            endtext01.draw() # Draw ending message here
            endtext010.draw()
            win.flip() # Clears the window
            keypressed = event.waitKeys(timeStamped=False)
            break
            
#-------Ending Routine "show_flash"-------
for thisComponent in show_flashComponents01:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
########################################################################################
########################################################################################



# Shuffle the single grid conditions again:
np.random.shuffle(single_proportions)



########################################################################################
########################################################################################
########################################################################################
# Single Grid Trials - JUDGING PROPORTIONS - BLOCK 2:
########################################################################################
########################################################################################
########################################################################################
# Initialize components for Routine "init_experiment"
init_experimentClock = core.Clock()
# set_colors()
# Colors used during the experiment.s
def set_colors():
    global sc_c # screen color
    global f_c # frame color
    global sq_c # square color
    # 1 = white
    # -0.06 = grey 80
    # -0.37 = grey 120
    # -1 = black
    sc_c = 1
    f_c = -0.06
    sq_c = -0.37
    t_c = -0.06

# set_sizes()
# Sizes used during the experiment
def set_sizes():
    global f_s # frame size (square) (frame surrounding the stimulus)
    global sq_s # square size (square where the stimulus is shown)
    global l_s # line size (the width of the line surrounding the stimulus)
    f_s = 540
    sq_s = 800
    l_s = 100
    
# Set the position of left stimulus
def set_positions01():
    global fl_p3 # Where should the flash be drawn
    fl_p3 = [0, 0]

########################################################################################
# Set main conditions and loop
########################################################################################

# Counter to keep track of things
counters2 = 0
thecounts2 = 0
counter01s2 = 0
thecount01s2 = 0
pcounters2 = practicetrials+1
pcounter2s2 = 1


for j in range(singletrials):
    # Select what condition is to be performed on experimental trials:
    if colour_order1 == 1:
        singleconditionsx = single_proportions[counter01s2]
    elif colour_order1 == 2:
        singleconditionsx = single_proportions[counter01s2]
        
    
    if pcounter > practicetrials:
        # Append the condition we're on:
        if singleconditionsx == 1:
            conused3.append('b,o')
            difflevel3.append('Exp - Hard 1')
        elif singleconditionsx == 2:
            conused3.append('B,o')
            difflevel3.append('Con - Easy 1')
        elif singleconditionsx == 3:
            conused3.append('o,b')
            difflevel3.append('Exp - Hard 1')
        elif singleconditionsx == 4:
            conused3.append('O,b') 
            difflevel3.append('Con - Easy 1')
    
    # Set the conditions here:
    if singleconditionsx == 1:
        p01 = .52#(52/48) more blue
    elif singleconditionsx == 2:
        p01 = .70#(70/30) a lot more blue
    elif singleconditionsx == 3:
        p01 = .52#(52/48) more blue orange
    elif singleconditionsx == 4:
        p01 = .70#(70/30) a lot more orange
        
    
    # flash stimulus functions
    # flash initialization
    def flash_init(win, position01=[0,0], square_size=10, columns=20, rows=20, percent_color01=p01): # Colour2 being manipulated whic is BLUE
        global flash01s2 # The flash stimulus (an array of flashing squares)
        
        if singleconditionsx <= 2:
            color_set01 = [color2, color1] # color2 being manipulated which is the BLUE
        elif singleconditionsx >= 3:
            color_set01 = [color1, color2] # colour1 is being manipulated which is the ORANGE
        cell_number = columns * rows
    
        num_color4 = int(np.floor(float(cell_number)*percent_color01)) # First colour
        num_color5 = int(np.floor(float(cell_number)*(1-percent_color01))) # Second colour
        
        # fill an array with colors. Each color should appear approximatively the same number of times.
        f_colors3s2 = []
        for i in range(num_color4):
            f_colors3s2.append(color_set01[0])
        for i in range(num_color5):
            f_colors3s2.append(color_set01[1])
        numpy.random.shuffle(color_set01)
        i = cell_number - len(f_colors3s2)
        while i > 0:
            f_colors3s2.append(color_set01[i])
            i -= 1
        
        # randomize color order.
        shuffle(f_colors3s2)
        
        # fill an array with coordinate for each color square. First square should be at the upper left
        # and next should follow from left to right and up to down.
        xys = []
        x_left = (1 - columns) * square_size / 2
        y_top = (1 - rows) * square_size / 2
        for l in range(rows):
            for c in range(columns):
                xys.append((x_left + c * square_size, y_top + l * square_size))
        
        
        # fill an array with coordinate for each color square. First square should be at the upper left
        # and next should follow from left to right and up to down.
        xys2 = []
        x_left = (1 - columns) * square_size / 2
        y_top = (1 - rows) * square_size / 2
        for l in range(rows):
            for c in range(columns):
                xys2.append((x_left + c * square_size, y_top + l * square_size))
        
        # MAIN FUNCTION TO CREATE FIRST GRID
        flash01s2 = visual.ElementArrayStim(win=win,
                            fieldPos=position01,
                            fieldShape='sqr',
                            nElements=cell_number,
                            sizes=square_size,
                            xys=xys,
                            colors=f_colors3s2,
                            elementTex=None,
                            elementMask=None,
                            name='flash',
                            autoLog=False)
                            
                            
                            
    
    # flash stimulus change
    def flash_changes2():
        global flash01s2
        shuffle(flash01s2.colors)
        flash01s2.setColors(flash01s2.colors)
    
    # Time variables used during the experiment
    def set_timings2():
        global f_t 
        f_t = 5 # The duration (in frame) of a flash image presentation
    
    # data_init
    set_colors()
    set_sizes()
    set_positions01()
    set_timing()
    
    #############################
    # MAIN FUNCTION HERE
    flash_init(win, fl_p3, square_size=0.3, columns=20, rows=20) # set the parameters here for the function!!
    #############################
    
    # Initialize components for Routine "show_flash"
    show_flashClock01s2 = core.Clock()
    frame_fl = visual.ImageStim(win=win, name='frame_fl',
        image=None, mask=None,
        ori=0, pos=fl_p3, size=f_s,
        color=f_c, colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=0.0)
    
    # Create some handy timers
    globalClock01s2 = core.Clock()  # to track the time since experiment started
    routineTimer01s2 = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 
    
    #------Prepare to start Routine "init_experiment"-------
    t = 0
    frameN = -1
    
    #------Prepare to start Routine "show_flash"-------
    t = 0
    show_flashClock01s2.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    # flash begin routine
    f_change = 0
    
    # keep track of which components have finished
    show_flashComponents01s2 = []
    show_flashComponents01s2.append(frame_fl)
    for thisComponent in show_flashComponents01:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    ########################################################################################
    ########################################################################################
    
    
    ########################################################################################
    # MAIN EXPERIMENT
    ########################################################################################
    
    #---Start Routine "show_flash"-------
    continueRoutine = True
    while continueRoutine:    
        # Hides mouse
        mouse = event.Mouse(visible=0)
        
        # get current time
        t = show_flashClock01s2.getTime()
        #print("t =", t)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        
        # update/draw components on each frame
        #print(frameN)
        
        # *frame_fl* updates
        if t >= 0.0 and frame_fl.status == NOT_STARTED:
            # keep track of start time/frame for later
            frame_fl.tStart = t  # underestimates by a little under one frame
            frame_fl.frameNStart = frameN  # exact frame index
            frame_fl.draw()
        # flash each frame
        if frameN >= f_change:
            flash_changes2()
            f_change+= f_t
#        if colour_order1 == 1:
#            strialtextb.draw()
#        elif colour_order1 == 2:
#            #strialtexto.draw()
        flash01s2.draw()  # First stimulus is drawn here
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer01s2.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in show_flashComponents01s2:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
                
        # RESPONSE 1: (Left Side - BLUE)
        if event.getKeys(keyList=["escape"]):
            win.flip()
            breaktext.draw()
            win.flip()
            keypressed = event.waitKeys(timeStamped=False)
            checkclock01s2.reset()
        if event.getKeys(keyList=["6"]):
            win.close()
            core.quit()
        if event.getKeys(keyList=["z"]): # MORE key
        
            # Update practice trial counter
            pcounters2 = pcounters2+1
            
            # print the condition we did
            print("actual single trial done =", singleconditionsx)
            
            # Track response times
            #rt = rtclock.getTime()
            time01s2 = checkclock01s2.getTime()
            RT3.append(time01s2)
            
            if colour_order1 == 1:
                if singleconditionsx <= 2:
                    correctresponse3.append('1')
                    print('response ===========  correct')
                elif singleconditionsx >= 3:
                    correctresponse3.append('0')
                    print('response ===========  incorrect')
            elif colour_order1 == 2:
                if singleconditionsx <= 2:
                    correctresponse3.append('0')
                    print('response ===========  incorrect')
                elif singleconditionsx >= 3:
                    correctresponse3.append('1')
                    print('response ===========  correct')
            # Append which colour question was being asked:
            colourcolour3.append(colour_order1)
            
            # Keep track of keys pressed
            keyspressed3.append('left')
            
            # Update the counter
            counter01s2 = counter01s2+1
            
            # Keep track of trial number to be saved 
            trialNo3.append(counter01s2)
            
            
            # DRAW FIXATION CROSS AFTER EACH TRIAL
            win.flip() # Clears the window
            fcross.draw() # Draw the fixation cross
            win.flip() # Clears the window
            core.wait(1.5) # Keep the cross on screen for 2 seconds
            checkclock01s2.reset()
            
            # END THE EXPERIMENT HERE AND SAVE DATA
            if counter01s2 == singletrials:
                win.flip() # Clears the window
                endtext0122.draw() # Draw ending message here
                endtext01229.draw()
                win.flip() # Clears the window
                keypressed = event.waitKeys(timeStamped=False)
            break # End the expriment
            
         # RESPONSE 2: (Right Side - ORANGE)
        if event.getKeys(keyList=["m"]): # LESS key
            
            
            # Update practice trial counter
            pcounters2 = pcounters2+1
            
            # print the condition we did
            print("actual single trial done =", singleconditionsx)
            
            time01s2 = checkclock01s2.getTime()
            RT3.append(time01s2)
            
            if colour_order1 == 1:
                if singleconditionsx <= 2:
                    correctresponse3.append('0')
                    print('response ===========  incorrect')
                elif singleconditionsx >= 3:
                    correctresponse3.append('1')
                    print('response ===========  correct')
            elif colour_order1 == 2:
                if singleconditionsx <= 2:
                    correctresponse3.append('1')
                    print('response ===========  correct')
                elif singleconditionsx >= 3:
                    correctresponse3.append('0')
                    print('response ===========  incorrect')
        # Append which colour question was being asked:
            colourcolour3.append(colour_order1)
            
            # Keep track of keys pressed
            keyspressed3.append('right')
            
            # Update the counter
            counter01s2 = counter01s2+1
            
            # Keep track of trial number to be saved 
            trialNo3.append(counter01s2)
            
            
            # DRAW FIXATION CROSS AFTER EACH TRIAL
            win.flip() # Clears the window
            fcross.draw() # Draw the fixation cross
            win.flip() # Clears the window
            core.wait(1.5) # Keep the cross on screen for 2 seconds
            checkclock01s2.reset()
            
            # END THE EXPERIMENT HERE AND SAVE DATA
            if counter01s2 == singletrials:
                win.flip() # Clears the window
                endtext0122.draw() # Draw ending message here
                endtext01229.draw()
                win.flip() # Clears the window
                keypressed = event.waitKeys(timeStamped=False)
                #nowbreak = nowbreak+1
            break # End the expriment
            
            
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
         
        # END THE EXPERIMENT HERE:
        if counter01s2 == singletrials:
            break
            
            
#-------Ending Routine "show_flash"-------
for thisComponent in show_flashComponents01s2:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
########################################################################################
########################################################################################


# Shuffle the single grid conditions again:
np.random.shuffle(single_proportions)


########################################################################################
########################################################################################
########################################################################################
# Single Grid Trials - JUDGING DIFFICULTY - BLOCK 2:
########################################################################################
########################################################################################
########################################################################################
# Initialize components for Routine "init_experiment"
init_experimentClock = core.Clock()
# set_colors()
# Colors used during the experiment.s
def set_colors():
    global sc_c # screen color
    global f_c # frame color
    global sq_c # square color
    # 1 = white
    # -0.06 = grey 80
    # -0.37 = grey 120
    # -1 = black
    sc_c = 1
    f_c = -0.06
    sq_c = -0.37
    t_c = -0.06

# set_sizes()
# Sizes used during the experiment
def set_sizes():
    global f_s # frame size (square) (frame surrounding the stimulus)
    global sq_s # square size (square where the stimulus is shown)
    global l_s # line size (the width of the line surrounding the stimulus)
    f_s = 540
    sq_s = 800
    l_s = 100
    
# Set the position of left stimulus
def set_positions01():
    global fl_p3 # Where should the flash be drawn
    fl_p3 = [0, 0]

########################################################################################
# Set main conditions and loop
########################################################################################

# Counter to keep track of things
counters2 = 0
thecounts2 = 0
counter01s2 = 0
thecount01s2 = 0
pcounters2 = practicetrials+1
pcounter2s2 = 1


for j in range(singletrials):
    # Select what condition is to be performed on experimental trials:
    if colour_order1 == 1:
        singleconditionsx = single_proportions[counter01s2]
    elif colour_order1 == 2:
        singleconditionsx = single_proportions[counter01s2]
        
    
    if pcounter > practicetrials:
        # Append the condition we're on:
        if singleconditionsx == 1:
            conused4.append('b,o')
            difflevel4.append('Exp - Hard 1')
        elif singleconditionsx == 2:
            conused4.append('B,o')
            difflevel4.append('Con - Easy 1')
        elif singleconditionsx == 3:
            conused4.append('o,b')
            difflevel4.append('Exp - Hard 1')
        elif singleconditionsx == 4:
            conused4.append('O,b') 
            difflevel4.append('Con - Easy 1')
    
    # Set the conditions here:
    if singleconditionsx == 1:
        p01 = .52#(52/48) more blue
    elif singleconditionsx == 2:
        p01 = .70#(70/30) a lot more blue
    elif singleconditionsx == 3:
        p01 = .52#(52/48) more blue orange
    elif singleconditionsx == 4:
        p01 = .70#(70/30) a lot more orange
    
    
    # flash stimulus functions
    # flash initialization
    def flash_init(win, position01=[0,0], square_size=10, columns=20, rows=20, percent_color01=p01): # Colour2 being manipulated whic is BLUE
        global flash01s2 # The flash stimulus (an array of flashing squares)
        
        if singleconditionsx <= 2:
            color_set01 = [color2, color1] # color2 being manipulated which is the BLUE
        elif singleconditionsx >= 3:
            color_set01 = [color1, color2] # colour1 is being manipulated which is the ORANGE
        cell_number = columns * rows
    
        num_color4 = int(np.floor(float(cell_number)*percent_color01)) # First colour
        num_color5 = int(np.floor(float(cell_number)*(1-percent_color01))) # Second colour
        
        # fill an array with colors. Each color should appear approximatively the same number of times.
        f_colors3s2 = []
        for i in range(num_color4):
            f_colors3s2.append(color_set01[0])
        for i in range(num_color5):
            f_colors3s2.append(color_set01[1])
        numpy.random.shuffle(color_set01)
        i = cell_number - len(f_colors3s2)
        while i > 0:
            f_colors3s2.append(color_set01[i])
            i -= 1
        
        # randomize color order.
        shuffle(f_colors3s2)
        
        # fill an array with coordinate for each color square. First square should be at the upper left
        # and next should follow from left to right and up to down.
        xys = []
        x_left = (1 - columns) * square_size / 2
        y_top = (1 - rows) * square_size / 2
        for l in range(rows):
            for c in range(columns):
                xys.append((x_left + c * square_size, y_top + l * square_size))
        
        
        # fill an array with coordinate for each color square. First square should be at the upper left
        # and next should follow from left to right and up to down.
        xys2 = []
        x_left = (1 - columns) * square_size / 2
        y_top = (1 - rows) * square_size / 2
        for l in range(rows):
            for c in range(columns):
                xys2.append((x_left + c * square_size, y_top + l * square_size))
        
        # MAIN FUNCTION TO CREATE FIRST GRID
        flash01s2 = visual.ElementArrayStim(win=win,
                            fieldPos=position01,
                            fieldShape='sqr',
                            nElements=cell_number,
                            sizes=square_size,
                            xys=xys,
                            colors=f_colors3s2,
                            elementTex=None,
                            elementMask=None,
                            name='flash',
                            autoLog=False)
                            
                            
                            
    
    # flash stimulus change
    def flash_changes2():
        global flash01s2
        shuffle(flash01s2.colors)
        flash01s2.setColors(flash01s2.colors)
    
    # Time variables used during the experiment
    def set_timings2():
        global f_t 
        f_t = 5 # The duration (in frame) of a flash image presentation
    
    # data_init
    set_colors()
    set_sizes()
    set_positions01()
    set_timing()
    
    #############################
    # MAIN FUNCTION HERE
    flash_init(win, fl_p3, square_size=0.3, columns=20, rows=20) # set the parameters here for the function!!
    #############################
    
    # Initialize components for Routine "show_flash"
    show_flashClock01s2 = core.Clock()
    frame_fl = visual.ImageStim(win=win, name='frame_fl',
        image=None, mask=None,
        ori=0, pos=fl_p3, size=f_s,
        color=f_c, colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=0.0)
    
    # Create some handy timers
    globalClock01s2 = core.Clock()  # to track the time since experiment started
    routineTimer01s2 = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 
    
    #------Prepare to start Routine "init_experiment"-------
    t = 0
    frameN = -1
    
    #------Prepare to start Routine "show_flash"-------
    t = 0
    show_flashClock01s2.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    # flash begin routine
    f_change = 0
    
    # keep track of which components have finished
    show_flashComponents01s2 = []
    show_flashComponents01s2.append(frame_fl)
    for thisComponent in show_flashComponents01:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    ########################################################################################
    ########################################################################################
    
    
    ########################################################################################
    # MAIN EXPERIMENT
    ########################################################################################
    
    #---Start Routine "show_flash"-------
    continueRoutine = True
    while continueRoutine:    
        # Hides mouse
        mouse = event.Mouse(visible=0)
        
        # get current time
        t = show_flashClock01s2.getTime()
        #print("t =", t)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        
        # update/draw components on each frame
        #print(frameN)
        
        # *frame_fl* updates
        if t >= 0.0 and frame_fl.status == NOT_STARTED:
            # keep track of start time/frame for later
            frame_fl.tStart = t  # underestimates by a little under one frame
            frame_fl.frameNStart = frameN  # exact frame index
            frame_fl.draw()
        # flash each frame
        if frameN >= f_change:
            flash_changes2()
            f_change+= f_t
#        if colour_order1 == 1:
#            strialtextb.draw()
#        elif colour_order1 == 2:
#            #strialtexto.draw()
        flash01s2.draw()  # First stimulus is drawn here
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer01s2.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in show_flashComponents01s2:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
                
        # RESPONSE 1: (Left Side - BLUE)
        if event.getKeys(keyList=["escape"]):
            win.flip()
            breaktext.draw()
            win.flip()
            keypressed = event.waitKeys(timeStamped=False)
            checkclock01s2.reset()
        if event.getKeys(keyList=["6"]):
            win.close()
            core.quit()
        if event.getKeys(keyList=["z"]): # MORE key
        
            # Update practice trial counter
            pcounters2 = pcounters2+1
            
            # print the condition we did
            print("actual single trial done =", singleconditionsx)
            
            # Track response times
            #rt = rtclock.getTime()
            time01s2 = checkclock01s2.getTime()
            RT4.append(time01s2)
            
            if colour_order1 == 1:
                if singleconditionsx <= 2:
                    correctresponse4.append('1')
                    print('response ===========  correct')
                elif singleconditionsx >= 3:
                    correctresponse4.append('0')
                    print('response ===========  incorrect')
            elif colour_order1 == 2:
                if singleconditionsx <= 2:
                    correctresponse4.append('0')
                    print('response ===========  incorrect')
                elif singleconditionsx >= 3:
                    correctresponse4.append('1')
                    print('response ===========  correct')
            # Append which colour question was being asked:
            colourcolour4.append(colour_order1)
            
            # Keep track of keys pressed
            keyspressed4.append('left')
            
            # Update the counter
            counter01s2 = counter01s2+1
            
            # Keep track of trial number to be saved 
            trialNo4.append(counter01s2)
            
            
            # DRAW FIXATION CROSS AFTER EACH TRIAL
            win.flip() # Clears the window
            fcross.draw() # Draw the fixation cross
            win.flip() # Clears the window
            core.wait(1.5) # Keep the cross on screen for 2 seconds
            checkclock01s2.reset()
            
            # END THE EXPERIMENT HERE AND SAVE DATA
            if counter01s2 == singletrials:
                win.flip() # Clears the window
                endtext1.draw() # Draw ending message here
                win.flip()
                core.wait(5.0)
                win.flip()
                #####################################################################
                #Write Data To File
                #####################################################################
                
                # Write RESULTS To A File 
                os.chdir("JD_task_results") # move to folder called RESULTS, need to CREATE this if it does not exist already.
                fout = open(filename, 'w')
                fout.write('Trial Number, Response, Correct/Incorrect(1/0), RT, Condition, Difficulty, Colour Order:\n')
                for i in range(singletrials):
                    fout.write('%d\t'% trialNo[i],)
                    fout.write('%s\t'% keyspressed[i],)
                    fout.write('%s\t'% correctresponse[i],)
                    fout.write('%.3f\t'% RT[i],)
                    fout.write('%s\t'% conused[i],)
                    fout.write('%s\t'% difflevel[i],)
                    fout.write('%s\t\n'% colourcolour1[i],)
                    
#               fout.write('\n')
                for i in range(singletrials):
                    fout.write('%d\t'% trialNo2[i],)
                    fout.write('%s\t'% keyspressed2[i],)
                    fout.write('%s\t'% correctresponse2[i],)
                    fout.write('%.3f\t'% RT2[i],)
                    fout.write('%s\t'% conused2[i],)
                    fout.write('%s\t'% difflevel2[i],)
                    fout.write('%s\t\n'% colourcolour2[i],)
                
#               fout.write('\n')
                for i in range(singletrials):
                    fout.write('%d\t'% trialNo3[i],)
                    fout.write('%s\t'% keyspressed3[i],)
                    fout.write('%s\t'% correctresponse3[i],)
                    fout.write('%.3f\t'% RT3[i],)
                    fout.write('%s\t'% conused3[i],)
                    fout.write('%s\t'% difflevel3[i],)
                    fout.write('%s\t\n'% colourcolour3[i],)
                    
#               fout.write('\n')
                for i in range(singletrials):
                    fout.write('%d\t'% trialNo4[i],)
                    fout.write('%s\t'% keyspressed4[i],)
                    fout.write('%s\t'% correctresponse4[i],)
                    fout.write('%.3f\t'% RT4[i],)
                    fout.write('%s\t'% conused4[i],)
                    fout.write('%s\t'% difflevel4[i],)
                    fout.write('%s\t\n'% colourcolour4[i],)
                
                # Close the results data file
                fout.close()
                
                #Say Where Results Are Written & If Experiment Successful
                print('Results Written To File Called ' + filename) 
                print('Program Completed Successfuly.')
                ####################################################################
                ####################################################################
                
                win.close()
                core.quit()
            break # End the expriment
            
         # RESPONSE 2: (Right Side - ORANGE)
        if event.getKeys(keyList=["m"]): # LESS key
            
            
            # Update practice trial counter
            pcounters2 = pcounters2+1
            
            # print the condition we did
            print("actual single trial done =", singleconditionsx)
            
            time01s2 = checkclock01s2.getTime()
            RT4.append(time01s2)
            
            if colour_order1 == 1:
                if singleconditionsx <= 2:
                    correctresponse4.append('0')
                    print('response ===========  incorrect')
                elif singleconditionsx >= 3:
                    correctresponse4.append('1')
                    print('response ===========  correct')
            elif colour_order1 == 2:
                if singleconditionsx <= 2:
                    correctresponse4.append('1')
                    print('response ===========  correct')
                elif singleconditionsx >= 3:
                    correctresponse4.append('0')
                    print('response ===========  incorrect')
            # Append which colour question was being asked:
            colourcolour4.append(colour_order1)
            
            # Keep track of keys pressed
            keyspressed4.append('right')
            
            # Update the counter
            counter01s2 = counter01s2+1
            
            # Keep track of trial number to be saved 
            trialNo4.append(counter01s2)
            
            
            # DRAW FIXATION CROSS AFTER EACH TRIAL
            win.flip() # Clears the window
            fcross.draw() # Draw the fixation cross
            win.flip() # Clears the window
            core.wait(1.5) # Keep the cross on screen for 2 seconds
            checkclock01s2.reset()
            
            # END THE EXPERIMENT HERE AND SAVE DATA
            if counter01s2 == singletrials:
                win.flip() # Clears the window
                endtext1.draw() # Draw ending message herehe window
                win.flip()
                core.wait(5.0)
                win.flip()
                #nowbreak = nowbreak+1
                #####################################################################
                #Write Data To File
                #####################################################################
                
                # Write RESULTS To A File 
                os.chdir("JD_task_results") # move to folder called RESULTS, need to CREATE this if it does not exist already.
                fout = open(filename, 'w')
                fout.write('Trial Number, Response, Correct/Incorrect(1/0), RT, Condition, Difficulty, Colour Order:\n')
                for i in range(singletrials):
                    fout.write('%d\t'% trialNo[i],)
                    fout.write('%s\t'% keyspressed[i],)
                    fout.write('%s\t'% correctresponse[i],)
                    fout.write('%.3f\t'% RT[i],)
                    fout.write('%s\t'% conused[i],)
                    fout.write('%s\t'% difflevel[i],)
                    fout.write('%s\t\n'% colourcolour1[i],)
                    
#               fout.write('\n')
                for i in range(singletrials):
                    fout.write('%d\t'% trialNo2[i],)
                    fout.write('%s\t'% keyspressed2[i],)
                    fout.write('%s\t'% correctresponse2[i],)
                    fout.write('%.3f\t'% RT2[i],)
                    fout.write('%s\t'% conused2[i],)
                    fout.write('%s\t'% difflevel2[i],)
                    fout.write('%s\t\n'% colourcolour2[i],)
                
#               fout.write('\n')
                for i in range(singletrials):
                    fout.write('%d\t'% trialNo3[i],)
                    fout.write('%s\t'% keyspressed3[i],)
                    fout.write('%s\t'% correctresponse3[i],)
                    fout.write('%.3f\t'% RT3[i],)
                    fout.write('%s\t'% conused3[i],)
                    fout.write('%s\t'% difflevel3[i],)
                    fout.write('%s\t\n'% colourcolour3[i],)
                    
#                fout.write('\n')
                for i in range(singletrials):
                    fout.write('%d\t'% trialNo4[i],)
                    fout.write('%s\t'% keyspressed4[i],)
                    fout.write('%s\t'% correctresponse4[i],)
                    fout.write('%.3f\t'% RT4[i],)
                    fout.write('%s\t'% conused4[i],)
                    fout.write('%s\t'% difflevel4[i],)
                    fout.write('%s\t\n'% colourcolour4[i],)
                
                # Close the results data file
                fout.close()
                
                #Say Where Results Are Written & If Experiment Successful
                print('Results Written To File Called ' + filename) 
                print('Program Completed Successfuly.')
                ####################################################################
                ####################################################################
                
                win.close()
                core.quit()
            break # End the expriment
            
            
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
         
        # END THE EXPERIMENT HERE:
        if counter01s2 == singletrials:
            break
            
            
#-------Ending Routine "show_flash"-------
for thisComponent in show_flashComponents01s2:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
########################################################################################
########################################################################################
