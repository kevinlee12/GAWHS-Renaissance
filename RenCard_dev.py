#-------------------------------------------------------------------------------
# Name:        RenCard
# Purpose:     Renaissance Card Sorter and Counter#
# Author:      leekevin#
# Created:     04/11/2013
# Copyright:   (c) leekevin 2013
# Licence:     Creative Commons: Attribution-NonCommercial-ShareAlike 3.0 Unported
#-------------------------------------------------------------------------------
from tkinter import *
import sys

def gpa():
    home.destroy()
    gpa_win = Frame(win,bg='white')
    gpa_win.pack()
    welcome = Label(gpa_win, text ='GPA Mode',font = 'Arial 16')
    welcome.grid(row = 0, column =0)

def pride():
    print('Pride Mode')

def result():
    print('Result Mode')

win= Tk()
home= Frame(win,bg ='white')
home.pack()
win.wm_title('Renaissance Card Sorter')
welcome = Label(home, text = 'Renaissance Card Sorter', foreground ='dark red', font = 'Arial 16')
welcome.grid(row = 0 , column = 0)
gpaButton = Button(home, text = 'GPA Mode', font ='Arial 12', command = gpa)
gpaButton.grid(row = 1, column = 0)
prideButton = Button(home, text ='Pride Mode', font = 'Arial 12', command = pride)
prideButton.grid(row = 2, column = 0)
resultButton = Button(home, text= 'Sort & Count', font = 'Arial 12', command = result)
resultButton.grid(row = 3, column = 0)
logo_image = PhotoImage(file = 'logowhite.gif')
logo = Label(home, image = logo_image)
logo.grid(row=0, column =1)

mainloop()
