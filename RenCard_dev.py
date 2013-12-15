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
#Import for all functions needed
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import filedialog
import sys
import re
import csv
import os
#---------End Import------

def gpa():
    'GPA Ranker and Counter'
    #CSV File (out_file in Decider) will now be sheet
    sheet_filename = filedialog.askopenfilename(filetypes = (("CSV Files", ".csv"),("All files", "*.*")))
    sheet = open(sheet_filename, 'r')
    new_sheet = open('GPAOutput.csv','w')
    writer =csv.writer(new_sheet, dialect='excel')
    sheet_reader = csv.reader(sheet, dialect="excel")
    sheet.seek(1)
    for row in sheet_reader:
        print(row)
        print(type(row[4]))
        something = input(':')
        if row[4] == 'GPA':

        try:
            row[4] = float(row[4])
            print(type(row[4]))
            if row[4] == 0:
                row[5] = 'wildcat'
            elif 0<= row[4] and row[4]<2:
                row[5] = 'none'
            elif 2<= row[4] and row[4]<2.5:
                row[5] = 'bronze'
            elif 2.5<=row[4] and row[4]<3:
                row[5] = 'silver'
            elif 3<=row[4] and row[4]<3.5:
                row[5] = 'gold'
            elif 3.5<=row[4] and row[4]<6:
                row[5] = 'platinum'
            print(row)
            writer.writerow(row) #needs fixing
        except ValueError:
            pass
        except:
            sheet.close()
            quit
    try:
        sheet.close()
        print('done')
        exit
    except ValueError:
        pass
        quit
    #step1.destroy()

def decider():
    '''Pride document reader. Reads PRIDE file and outputs CSV File'''
    prev_teacher = []
    file = open(file_n,'r')
    #output_name = 'Output'
    output = filedialog.asksaveasfilename(filetypes = (("CSV Files", ".csv"),("All files", "*.*")), initialfile = 'PRIDEOutput.csv')
    out_file = open(output,'w')
    writer =csv.writer(out_file)
    count = 1
    writer.writerow(['Gender','Grade','Name','Teacher','GPA','Rank'])
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
    os.system(str("start excel.exe " + output))
    home.destroy()
    step1 = ttk.Frame(win)
    step1.pack()
    done_step1 = ttk.Button(step1, text = 'Done', command = gpa)
    done_step1.grid(row = 0, column = 0)

def pride_extractor():
    file_n = filedialog.askopenfilename(filetypes = (("Text Files", ".txt"),("All files", "*.*")))
    global file_n
    file_name = ttk.Label(home,text = file_n)
    file_name.grid(row=1,column = 1)
    if file_n != '':
        process = ttk.Button(home, text = 'Extract!',command = decider)
        process.grid(row = 1, column = 2)

win= Tk()
win.title('Renaissance Card Sorter')
top= ttk.Frame(win)
top.pack()
home = ttk.Frame(win)
home.pack()
style = ttk.Style()
style.configure("BW.TLabel" ) #Change font size
welcome = ttk.Label(top,text = 'Renaissance Card Sorter', style = "BW.TLabel")
welcome.grid(row = 0 , column = 0)
logo_image = PhotoImage(file = 'logowhite.gif')
logo = ttk.Label(top ,image = logo_image)
logo.grid(row=0, column =2)
prideButton = ttk.Button(home, text = 'Pride File', command = pride_extractor)
prideButton.grid(row = 1, column = 0)
gpaButton = ttk.Button(home, text = 'GPA Ranker & Counter', command = gpa)
gpaButton.grid(row = 2, column = 0)

mainloop()
