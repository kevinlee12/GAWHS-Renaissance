#-------------------------------------------------------------------------------
# Name:        RenCard
# Purpose:
#
# Author:      leekevin
#
# Created:     04/11/2013
# Copyright:   (c) leekevin 2013
# Licence:     Creative Commons: Attribution-NonCommercial-ShareAlike 3.0 Unported
#-------------------------------------------------------------------------------
from tkinter import *
from tkinter import filedialog
import sys
import re
import csv

def decider():
    'Pride document reader'
    prev_teacher = []
    file = open(file_n,'r')
    output_name = 'Output'
    out_file = open(output_name+'.csv','w')
    writer =csv.writer(out_file)
    count = 1
    teacher_pat = re.compile(r'(?P<pat>Teache)'r'(?P<teacher_last>[-a-zA-Z\' ]+, [-a-zA-Z\']+)')
    student_pat = re.compile(r'(?P<gender>[FM] )'r'(?P<grade>\d\d)'r'(?P<name>[-a-zA-Z ]+, [-a-zA-Z ]+)')
    for line in file.readlines():
        teacher = teacher_pat.findall(line)
        student = student_pat.findall(line)
        if teacher != []:
            #print(teacher[0][1])
            if prev_teacher == teacher[0][1]:
                pass
            else:
                #print(teacher[0][1])
                count = 1
                prev_teacher = teacher[0][1]
        elif student != []:
            #print(count)
            count = count + 1
            student = list(student[0][0:])
            student[1]= int(student[1])
            student.append(prev_teacher)
            print(student)
            writer.writerow(student)
    file.close()
    out_file.close()


def pride_extractor():
    file_n = filedialog.askopenfilename(filetypes = (("Text Files", ".txt"),("All files", "*.*")))
    global file_n
    file_name = Label(home,text = file_n ,background = 'white', font = 'Arial 10')
    file_name.grid(row=1,column = 1)
    if file_n != '':
        process = Button(home, text = 'Extract!', background = 'green', font = 'Arial 11',command = decider)
        process.grid(row = 1, column = 2)

def gpa():
    print('Pride Mode')

def result():
    print('Result Mode')

win= Tk()
home= Frame(win,bg ='white', bd = 0)
home.pack()
win.wm_title('Renaissance Card Sorter')
welcome = Label(home, text = 'Renaissance Card Sorter', foreground ='dark red',background ='white', font = 'Arial 14')
welcome.grid(row = 0 , column = 0)
gpaButton = Button(home, text = 'Pride File', font ='Arial 11', command = pride_extractor)
gpaButton.grid(row = 1, column = 0)
#prideButton = Button(home, text ='GPA', font = 'Arial 11', command = gpa)
#prideButton.grid(row = 2, column = 0)
#resultButton = Button(home, text= 'Sort & Count', font = 'Arial 11', command = result)
#resultButton.grid(row = 3, column = 0)
logo_image = PhotoImage(file = 'logowhite.gif')
logo = Label(home, image = logo_image)
logo.grid(row=0, column =2)

mainloop()
