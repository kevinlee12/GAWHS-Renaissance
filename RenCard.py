#-------------------------------------------------------------------------------
# Name:        RenCard
# Purpose:     Do all things RenCard related, mainly: sorting and counting and
#              cateogorzing.
# Author:      leekevin
# Created:     04/11/2013
# Copyright:   (c) leekevin 2013
# Licence:     Creative Commons: Attribution-NonCommercial-ShareAlike 3.0 Unported
# Notes:       Program is written backward, please start from the bottom to begin reading.
#
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
import datetime
#---------End Import------

def splitter():
    'Arrange Students by Pride Class'
    step1.destroy()
    try:
        new_sheet = open(outsheet_directory[0]+'/GPAOutput.csv','r')
    except:
        sys.exit()
    output = open(outsheet_directory[0]+'/Output.txt','w')
    teacher = ''
    sheet_reader = csv.reader(new_sheet, dialect="excel")
    new_sheet.seek(1)
    for line in sheet_reader:
        if teacher == line[3]:
            pass
        elif line[3] == 'Teacher':
            continue
        elif teacher != line[3]:
            output.write('\n')
            output.write('Teacher: ' + line[3] +'\n')
        new_line = line[1] + ':' + line[2] + ' = ' + line[4] + '.:' + line[5] + '\n'
        teacher= line[3]
        print(new_line)
        output.write(new_line)
    new_sheet.close()
    step1 = ttk.Frame(win)
    global step1
    step1.pack()
    done1_prompt = ttk.Label(step1, text= 'Done!',font = 'SegoeUI 13')
    done1_prompt.grid(row = 0, column = 0)
    step1_quit = ttk.Button(step1, text = 'Exit', command = sys.exit)
    step1_quit.grid(row = 1, column = 0)

def gpa():
    'GPA Ranker and Counter'
    #CSV File (out_file in Decider) will now be sheet
    try:
        step1.destroy()
    except:
        pass
    total = 0
    none = 0
    wildcat = 0
    bronze = 0
    silver = 0
    gold = 0
    platinum = 0
    try:
        sheet_filename = filedialog.askopenfilename(filetypes = (("CSV Files", ".csv"),("All files", "*.*")),initialfile = 'PRIDEOutput.csv')
    except IOError:
        sheet_filename = filedialog.askopenfilename(filetypes = (("CSV Files", ".csv"),("All files", "*.*")),initialfile = 'PRIDEOutput.csv')
    except:
        sys.exit()
    sheet = open(sheet_filename, 'r')
    outsheet_directory = os.path.split(sheet_filename)
    global outsheet_directory
    new_sheet = open(outsheet_directory[0]+'/GPAOutput.csv','w')
    writer =csv.writer(new_sheet, dialect='excel')
    sheet_reader = csv.reader(sheet, dialect="excel")
    writer.writerow(['Gender','Grade','Name','Teacher','GPA','Rank'])
    for row in sheet_reader:
        total = total + 1
        if row[4] == 'GPA':
            continue
        elif row[4] == '':
            row[5] = 'wildcat'
            row[4] = 'N/A'
            wildcat = wildcat + 1
            writer.writerow(row)
        try:
            row[4] = float(row[4])
            #if row[4] == 0:
                #row[5] = 'wildcat'
            if 0<= row[4] and row[4]<2:
                row[5] = 'none'
                none = none + 1
            elif 2<= row[4] and row[4]<2.5:
                row[5] = 'bronze'
                bronze = bronze + 1
            elif 2.5<=row[4] and row[4]<3:
                row[5] = 'silver'
                silver = silver + 1
            elif 3<=row[4] and row[4]<3.5:
                row[5] = 'gold'
                gold = gold + 1
            elif 3.5<=row[4] and row[4]<6:
                row[5] = 'platinum'
                platinum = platinum + 1
            print(row)
            writer.writerow(row)
        except ValueError:
            pass
        except:
            sheet.close()
            quit
        print(row)
    try:
        sheet.close()
        print('done')
    except ValueError:
        pass
        quit
    try:
        home.destroy()
    except:
        pass
    date_time = str(datetime.datetime.now())
    total = str(total-1)
    none = str(none)
    wildcat = str(wildcat)
    bronze = str(bronze)
    silver = str(silver)
    gold = str(gold)
    platinum = str(platinum)
    numbers_results = open(outsheet_directory[0]+'/Numbers.txt','w')
    numbers_results.write('Summary of the Total Counts generated:'+ date_time +'\n' + 'Totals:'+ total + '\nNo Card:'+ none +'\nWildcat:'+ wildcat + '\nBronze:'+ bronze + '\nSilver:'+ silver + '\nGold:'+ gold + '\nPlatinum:' + platinum)
    numbers_results.close()
    new_sheet.close()
    os.system(str("start excel.exe " + outsheet_directory[0] + '/GPAOutput.csv'))
    step1 = ttk.Frame(win)
    global step1
    step1.pack()
    done1_prompt = ttk.Label(step1, text= 'Sort the spreadsheet according to the following order:', font = 'SegoeUI 13')
    done1_prompt.grid(row = 0, column = 0)
    done1_prompt2 = ttk.Label(step1, text= '1. Teacher', font = 'SegoeUI 13')
    done1_prompt2.grid(row = 1, column = 0)
    done1_prompt3 = ttk.Label(step1, text= '2. Name', font = 'SegoeUI 13')
    done1_prompt3.grid(row = 2, column = 0)
    done_step1 = ttk.Button(step1, text = 'Done', command = splitter)
    done_step1.grid(row = 3, column = 0)
    step1_quit = ttk.Button(step1, text = 'Quit', command = sys.exit)
    step1_quit.grid(row = 3, column = 1)
    #OS file joiner and splitter


def decider():
    '''Pride document reader. Reads PRIDE file and outputs CSV File'''
    prev_teacher = []
    file = open(file_n,'r')
    #output_name = 'Output'
    output = filedialog.asksaveasfilename(filetypes = (("CSV Files", ".csv"),("All files", "*.*")), initialfile = 'PRIDEOutput.csv')
    out_file = open(output,'w')
    writer =csv.writer(out_file)
    count = 1
    writer.writerow(['Gender','Grade','Name','Birthday','Teacher','GPA','Rank'])
    teacher_pat = re.compile(r'(?P<pat>Teache)'r'(?P<teacher_last>[-a-zA-Z\' ]+, [-a-zA-Z\']+)')
    room_pat1 = re.compile(r'[A-Z]-[a-zA-Z0-9]+')
    room_pat2 = re.compile(r'[A-Z][a-zA-Z0-0]+') #Thompson Bugged
    student_pat = re.compile(r'(?P<gender>[FM] )'r'(?P<grade>\d\d)'r'(?P<name>[-a-zA-Z ]+, [-a-zA-Z ]+)'r'(?P<bday>\d\d/\d\d/\d\d)')
    for line in file.readlines():
        teacher = teacher_pat.findall(line)
        student = student_pat.findall(line)
        room1 = room_pat1.findall(line)
        room2 = room_pat2.findall(line)
        if teacher != []:
            #print(teacher[0][1])
            if prev_teacher == teacher[0][1]:
                pass
            else:
                #print(teacher[0][1])
                count = 1
                if room1 != []:
                    prev_teacher = teacher[0][1] + ' :: ' + str(room1[0])
                else:
                    prev_teacher = teacher[0][1] + ' :: ' + str(room2[0])
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
    print(output)
    os.system(str("start excel.exe " + output))
    home.destroy()
    step1 = ttk.Frame(win)
    global step1
    step1.pack()
    done1_prompt = ttk.Label(step1, text= 'Sort spreadsheet according to the following order:',font = 'SegoeUI 13')
    done1_prompt.grid(row = 0, column = 0)
    done1_prompt = ttk.Label(step1, text= '1. Grade',font = 'SegoeUI 13')
    done1_prompt.grid(row = 1, column = 0)
    done1_prompt = ttk.Label(step1, text= '2. Name',font = 'SegoeUI 13')
    done1_prompt.grid(row = 2, column = 0)
    done_step1 = ttk.Button(step1, text = 'Done', command = gpa)
    done_step1.grid(row = 3, column = 0)
    step1_quit = ttk.Button(step1, text = 'Quit', command = sys.exit)
    step1_quit.grid(row = 3, column = 1)
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
global win
top= ttk.Frame(win)
top.pack()
home = ttk.Frame(win)
home.pack()
style = ttk.Style()
style.configure("BW.TLabel" ) #Change font size
welcome = ttk.Label(top,text = 'Renaissance Card Sorter', font = 'SegoeUI 14')
welcome.grid(row = 0 , column = 0)
logo_image = PhotoImage(file = 'logowhite.gif')
logo = ttk.Label(top ,image = logo_image)
logo.grid(row=0, column =2)
prideButton = ttk.Button(home, text = 'Pride File', command = pride_extractor)
prideButton.grid(row = 1, column = 0)
gpaButton = ttk.Button(home, text = 'GPA Ranker & Counter', command = gpa)
gpaButton.grid(row = 2, column = 0)

mainloop()
