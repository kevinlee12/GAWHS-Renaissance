#-------------------------------------------------------------------------------
# Name:        RenCard
# Purpose:     Do all things RenCard related, mainly: sorting and counting and
#              categorzing.
# Author:      leekevin
# Created:     04/11/2013
# Copyright:   (c) leekevin 2013
# Licence:     GPL v3
# Notes:       Program is written backward, please start from the bottom to begin reading.
# Prerequites: Windows, MS Excel, Notepad
#-------------------------------------------------------------------------------

#Import for all functions needed
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import filedialog
import tkinter
import sys
import re
import csv
import os
import datetime
#---------End Import------

def splitter():
    '''Arrange Students by Pride Class and outputs text files.'''
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
        if teacher == line[4]:
            pass
        elif line[3] == 'Teacher':
            pass
        elif teacher != line[4]:
            output.write('\n')
            output.write('Teacher: ' + line[4] +'\n')
        new_line = line[1] + ':' + line[2] + ' = ' + line[5] + '.:' + line[6] + '\n'
        teacher= line[4]
        print(new_line)
        output.write(new_line)
    new_sheet.close()
    os.system(str("start notepad " + outsheet_directory[0]+'/Numbers.txt'))
    os.system(str("start notepad " + outsheet_directory[0]+'/Output.txt'))
    step1 = ttk.Frame(win)
    global step1
    step1.pack()
    done1_prompt = ttk.Label(step1, text= 'Done!',font = 'Arial 13')
    done1_prompt.grid(row = 0, column = 0)
    step1_quit = ttk.Button(step1, text = 'Exit', command = sys.exit)
    step1_quit.grid(row = 1, column = 0)

def gpa():
    '''GPA Ranker and Counter, reads and outputs a new CSV File.'''
    #CSV File (out_file in Decider) will now be sheet
    try:
        step1.destroy()
        home.destroy()
    except:
        pass
    total = 0
    none = 0
    wildcat = 0
    bronze = 0
    silver = 0
    gold = 0
    platinum = 0
    errors = 0
    try:
        sheet_filename = filedialog.askopenfilename(filetypes = (("CSV Files", ".csv"),("All files", "*.*")),initialfile = 'PRIDEOutput.csv')
    except IOError:
        sheet_filename = filedialog.askopenfilename(filetypes = (("CSV Files", ".csv"),("All files", "*.*")),initialfile = 'PRIDEOutput.csv')
    except:
        sys.exit()
    sheet = open(sheet_filename, 'r')
    outsheet_directory = os.path.split(sheet_filename)
    sheet_reader = csv.reader(sheet, dialect="excel")
    global outsheet_directory
    new_sheet = open(outsheet_directory[0]+'/GPAOutput.csv','w')
    writer =csv.writer(new_sheet, dialect='excel')
    new_sheet_reader=csv.reader(new_sheet,dialect='excel')
    writer.writerow(['Gender','Grade','Name','Birthday','Teacher','GPA','Rank'])
    numbers_results = open(outsheet_directory[0]+'/Numbers.txt','w')
    date_time = str(datetime.datetime.now())
    numbers_results.write('Summary of the Total Counts generated: '+ date_time +'\n')
    numbers_results.write('\nErrors:')
    #step1 = ttk.Frame(win)
    #step1.pack()
    for row in sheet_reader:
        total = total + 1
        if row[5] == 'GPA':
            continue
        elif row[5] == '':
            row[6] = 'wildcat'
            row[5] = 'N/A'
            wildcat = wildcat + 1
            writer.writerow(row)
        try:
            row[5] = float(row[5])
            #if row[5] == 0:
                #row[6] = 'wildcat'
            if 0<= row[5] and row[5]<2:
                row[6] = 'encouragement'
                none = none + 1
            elif 2<= row[5] and row[5]<2.5:
                row[6] = 'bronze'
                bronze = bronze + 1
            elif 2.5<=row[5] and row[5]<3:
                row[6] = 'silver'
                silver = silver + 1
            elif 3<=row[5] and row[5]<3.5:
                row[6] = 'gold'
                gold = gold + 1
            elif 3.5<=row[5] and row[5]<=6:
                row[6] = 'platinum'
                platinum = platinum + 1
            elif row[5]>6:
                row[6] = 'INVALID GPA'
                numbers_results.write('\n' + str(row[1:3] + row[4:6]))
                errors = 1
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
    total = str(total-1)
    none = str(none)
    wildcat = str(wildcat)
    bronze = str(bronze)
    silver = str(silver)
    gold = str(gold)
    platinum = str(platinum)
    if errors == 1:
        numbers_results.write('\n\nIf there are errors listed above, please correct the errors'
                          '\nin the PRIDE input file and run GPA Ranker and Sorter again.\n\n')
    elif errors == 0:
        numbers_results.write('\n\nNO Errors Found!\n\n')
    numbers_results.write('Renaissance Card Counts\n' + 'Totals: '+ total + '\nEncouragement: '+ none +
                          '\nWildcat: '+ wildcat + '\nBronze: '+ bronze + '\nSilver: '+ silver + '\nGold: '+
                          gold + '\nPlatinum: ' + platinum)
    numbers_results.close()
    new_sheet.close()
    if errors == 1:
        os.system(str("start notepad " + outsheet_directory[0]+'/Numbers.txt'))
        home.destroy()
        step1 = ttk.Frame(win)
        global step15
        step1.pack()
        done1_prompt = ttk.Label(step1, text= 'Error:', font = 'Arial 13')
        done1_prompt.grid(row = 0, column = 0)
        done1_prompt2 = ttk.Label(step1, text= 'Errors were found, please correct them.', font = 'Arial 13')
        done1_prompt2.grid(row = 1, column = 0)
        done_step1 = ttk.Button(step1, text = 'Done', command = gpa)
        done_step1.grid(row = 3, column = 0)
        step1_quit = ttk.Button(step1, text = 'Quit', command = sys.exit)
        step1_quit.grid(row = 3, column = 1)
        os.system(str("start excel.exe " + outsheet_directory[0] + '/' + outsheet_directory[1]))
        sys.exit()
        os.system('pause')
    
    os.system(str("start excel.exe " + outsheet_directory[0] + '/GPAOutput.csv'))
    step1 = ttk.Frame(win)
    global step1
    step1.pack()
    done1_prompt = ttk.Label(step1, text= 'Sort the spreadsheet according to the following order:', font = 'Arial 13')
    done1_prompt.grid(row = 0, column = 0)
    done1_prompt2 = ttk.Label(step1, text= '1. Teacher', font = 'Arial 13')
    done1_prompt2.grid(row = 1, column = 0)
    done1_prompt3 = ttk.Label(step1, text= '2. Name', font = 'Arial 13')
    done1_prompt3.grid(row = 2, column = 0)
    done_step1 = ttk.Button(step1, text = 'Done', command = splitter)
    done_step1.grid(row = 3, column = 0)
    step1_quit = ttk.Button(step1, text = 'Quit', command = sys.exit)
    step1_quit.grid(row = 3, column = 1)
    #OS file joiner and splitter


def decider():
    '''Pride document reader. Reads PRIDE file and outputs CSV File WITHOUT GPA.'''
    prev_teacher = []
    file = open(file_n,'r')
    #output_name = 'Output'
    output = filedialog.asksaveasfilename(filetypes = (("CSV Files", ".csv"),("All files", "*.*")), initialfile = 'PRIDEOutput.csv')
    out_file = open(output,'w')
    writer =csv.writer(out_file)
    count = 1
    writer.writerow(['Gender','Grade','Name','Birthday','Teacher','GPA','Rank'])
    teacher_pat = re.compile(r'(?P<pat>Teache)'r'(?P<teacher_last>[-a-zA-Z\' ]+, [-a-zA-Z\']+)')
    room_pat = re.compile(r'(?P<pat>Room )'r'(?P<room>[A-Z][-a-zA-Z0-9]+)')
    student_pat = re.compile(r'(?P<gender>[FM] )'r'(?P<grade>\d\d)'r'(?P<name>[-a-zA-Z ]+, [-a-zA-Z ]+)'r'(?P<bday>\d\d/\d\d/\d+)')
    for line in file.readlines():
        teacher = teacher_pat.findall(line)
        student = student_pat.findall(line)
        room = room_pat.findall(line)
        if teacher != []:
            #print(teacher[0][1])
            if prev_teacher == teacher[0][1]:
                pass
            else:
                #print(teacher[0][1])
                count = 1
                if room != []:
                    prev_teacher = teacher[0][1] + ' :: ' + str(room[0][1])
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
    done1_prompt = ttk.Label(step1, text= '1. Grade',font = 'Arial 13')
    done1_prompt.grid(row = 1, column = 0)
    done1_prompt = ttk.Label(step1, text= '2. Name',font = 'Arial 13')
    done1_prompt.grid(row = 2, column = 0)
    done1_prompt4 = ttk.Label(step1, text = 'After sorting, input each student\'s GPA,', font = 'Arial 13')
    done1_prompt4.grid(row = 3, column = 0)
    done1_prompt5 = ttk.Label(step1, text = 'if the student does not have a GPA or is new,', font = 'Arial 13')
    done1_prompt5.grid(row = 4, column = 0)
    done1_prompt6 = ttk.Label(step1, text = 'leave it blank.', font = 'Arial 13')
    done1_prompt6.grid(row = 5, column = 0)
    done_step1 = ttk.Button(step1, text = 'Done', command = gpa)
    done_step1.grid(row = 6, column = 0)
    step1_quit = ttk.Button(step1, text = 'Quit', command = sys.exit)
    step1_quit.grid(row = 7, column = 0)
    
def pride_extractor():
    '''Asks user for file and sends user to decider function.'''
    file_n = filedialog.askopenfilename(filetypes = (("Text Files", ".txt"),("All files", "*.*")))
    global file_n
    file_name = ttk.Label(home,text = file_n)
    file_name.grid(row=1,column = 1)
    if file_n != '':
        process = ttk.Button(home, text = 'Extract!',command = decider)
        process.grid(row = 1, column = 2)

def start():
    assistwin.destroy()
    home = ttk.Frame(win)
    global home
    home.pack()
    prideButton = ttk.Button(home, text = 'Pride File', command = pride_extractor)
    prideButton.grid(row = 1, column = 0)
    gpaButton = ttk.Button(home, text = 'GPA Ranker & Counter', command = gpa)
    gpaButton.grid(row = 2, column = 0)
    assistButton = ttk.Button(home, text = 'Help & License', command = assist)
    assistButton.grid(row = 3, column = 0)


def assist():
    '''Assist module'''
    try:
        home.destroy()
    except:
        pass
    assistwin= ttk.Frame(win)
    assistwin.pack()
    global assistwin
    top = ttk.Label(assistwin, text = 'Help and License Module', font = 'Arial 14')
    top.grid(row = 0, column = 0)
    assist_license_title = ttk.Label(assistwin, text = 'License', font = 'Arial 13')
    assist_license_title.grid(row = 1, column = 0)
    lic = ttk.Label(assistwin, text = 'This file is part of Renaissance Card Sorter. Renaissance Card Sorter is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.', font = 'Arial 7', wraplength = 450, pad = 5)
    lic1 = ttk.Label(assistwin, text = 'Renaissance Card sorter is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.', font = 'Arial 7', wraplength = 450, pad = 5)
    lic2 = ttk.Label(assistwin, text = 'See the GNU General Public License for more details. You should have received a copy of the GNU General Public Licensealong with Renaissance Card Sorter.  If not, see <http://www.gnu.org/licenses/>.', font = 'Arial 7', wraplength = 450, pad = 5)
    lic.grid(row = 2, column = 0)
    lic1.grid(row = 3, column = 0)
    lic2.grid(row = 4, column = 0)
    assist_title= ttk.Label(assistwin,text = '\nAssist',font = 'Arial 13')
    assist_title.grid(row = 5, column = 0)
    assist1 = ttk.Label(assistwin, text = 'GPA Guidelines',font = 'Arial 11',wraplength = 400)
    assist1.grid(row = 6, column = 0)
    assist2 = ttk.Label(assistwin, text = 'GPA Range: [0,6] and none\n\nNew Students: Leave corresponding cell blank\nStudents with GPA: Enter corresponding GPA in cell\nNon-Frosh w/o GPA: Compile a list and ask the advisor to look up those students\' GPA, if the student is new, leave the cell blank, otherwise, input 0.', font = 'Arial 9', wraplength = 450, pad = 2)
    assist2.grid(row= 7, column =0)
    assist3 = ttk.Label(assistwin, text = 'GPA Levels', font = 'Arial 11')
    assist3.grid(row = 8, column = 0)
    assist4 = ttk.Label(assistwin, text = 'Encouragement: Incomplete and GPA below 2.0\nBronze: 2.0 to 2.49\nSilver: 2.5 to 2.99\nGold: 3.0 to 3.49\nPlatinum: 3.5 to 6', font = 'Arial 9', wraplength = 450, pad = 5)              
    assist4.grid(row = 9, column = 0)
    assist5 = ttk.Label(assistwin, text = 'Reminders', font = 'Arial 11')
    assist5.grid(row = 10, column = 0)
    assist6 = ttk.Label(assistwin, text = '1. Don\'t forget to check "My data has headers".\n2. Check to make sure that no windows overlap! (Notepad windows tend to overlap)', font = 'Arial 9',wraplength = 450)
    assist6.grid(row = 11, column = 0)
    assist5 = ttk.Label(assistwin, text= 'Errors', font = 'Arial 11')
    assist5.grid(row= 12, column = 0)
    assist6 = ttk.Label(assistwin, text = 'For GPAs that are over 6, the program will trigger an error response. After the program is executed, it will launch a text document (with the list of the students with incorrect GPA and preliminary count) and an excel file that was used to enter the GPA. After the two file launch, locate the people who had issues on the spreadsheet file and correct the errors, close the program and click \"Done\". The program will re-run and resume as normal. ', font = 'Arial 9', wraplength = 450, pad = 5)
    assist6.grid(row = 13, column = 0)
    back = ttk.Button(assistwin, text = 'Return to Main Menu', command = start)
    back.grid(row = 14,column =0)

#The following is for the main window, program begins here.
win= Tk()
win.title('Renaissance Card Sorter')
global win
top= ttk.Frame(win)
top.pack()
home = ttk.Frame(win)
home.pack()
style = ttk.Style()
style.configure("BW.TLabel")
welcome = ttk.Label(top,text = 'Renaissance Card Sorter', font = 'Arial 14')
welcome.grid(row = 0 , column = 0)
logo_image = PhotoImage(file = 'logowhite.gif')
logo = ttk.Label(top ,image = logo_image)
logo.grid(row=0, column =2)
prideButton = ttk.Button(home, text = 'Pride File', command = pride_extractor)
prideButton.grid(row = 1, column = 0)
gpaButton = ttk.Button(home, text = 'GPA Ranker & Counter', command = gpa)
gpaButton.grid(row = 2, column = 0)
assistButton = ttk.Button(home, text = 'Help & License', command = assist)
assistButton.grid(row = 3, column = 0)
