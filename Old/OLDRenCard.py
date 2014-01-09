#---------------------------------
#
#Old Version of RenCard Program
#
#---------------------------------
def gpa():
    "Name Database"
    import os
    print("GPA Mode")

    #file_name = input('File location:')
    #print(file_name)
    #file destination
#    if file_name == '':
#        file_name = input('Name of the file:')
#        file_name = file_name + '.txt'
#        file = open(file_name,'w')
#    else:
    try:
        file = open('gpa.txt','a')
    except IOError:
        #print('File not found.')
        #file_name = input('File Location')
        file = open('gpa.txt','a')
    grade =''

    while 1:
        student_info = ()
        complete_info = {}
        if grade == '':
            grade = input('Grade:')
        last_name = input('Last Name:')
        first_name = input('First (and Middle) Name:')
        try:
            gpa = float(input('GPA:'))
        except ValueError:
            print("re-enter GPA")
            gpa = float(input('GPA:'))
        if gpa == '':
            level = 'wildcat'
        elif 0<= gpa and gpa<2:
            level = 'none'
        elif 2<= gpa and gpa<2.5:
            level = 'bronze'
        elif 2.5<=gpa and gpa<3:
            level = 'silver'
        elif 3<=gpa and gpa<3.5:
            level = 'gold'
        elif 3.5<=gpa and gpa<6:
            level = 'platinum'
        else:
            print("Error:GPA is out of bounds, please re-enter GPA.")
            gpa = float(input('GPA:'))
            if 0<= gpa and gpa<2:
                level = 'none'
            elif 2<= gpa and gpa<2.5:
                level = 'bronze'
            elif 2.5<=gpa and gpa<3:
                level = 'silver'
            elif 3<=gpa and gpa<3.5:
                level = 'gold'
            elif 3.5<=gpa and gpa<6:
                level = 'platinum'
        gpa = str(gpa)
        student_info = grade + '::' + last_name + '::' + first_name + '::' + gpa + '::' + level
        print(student_info)
        cmd = input("Command:")
        #Press Enter to continue
        if cmd == '':
            pass
        elif cmd =="exit":
            file.write(student_info + ' \n')
            file.close()
            break
        elif cmd =="ngrade":
            grade = input('Grade:')
        elif cmd =='change':
            grade = input('Grade:')
            last_name = input('Last Name:')
            first_name = input('First (and Middle) Name:')
            gpa = float(input('GPA:'))
            if gpa == '':
                level = 'wildcat'
            elif 0<= gpa and gpa<2:
                level = 'none'
            elif 2<= gpa and gpa<2.5:
                level = 'bronze'
            elif 2.5<=gpa and gpa<3:
                level = 'silver'
            elif 3<=gpa and gpa<3.5:
                level = 'gold'
            elif 3.5<=gpa and gpa<6:
                level = 'platinum'
            gpa = str(gpa)
            student_info = grade + '::' + last_name + '::' + first_name + '::' + gpa + '::' + level
            print(student_info)
            nxt = input('Are there more students? (Y/n):')
            if nxt == 'y' or nxt =='Y':
                pass
            elif nxt == 'n' or nxt == 'N':
                file.write(student_info + ' \n')
                file.close()
                break
            gra_lev = input('Is the next student the same grade? (Y/n):')
            if gra_lev == 'Y' or gra_lev =='y':
                pass
            elif gra_lev == 'n' or gra_lev == 'N':
                grade = input('Grade:')
        file.write(student_info + ' \n')
    print("Program exit")
    quit

def pride():
    "Pride Class information"
    print("Pride Class Mode")

    #file_name = input('File location:')

    #file destination
    #if file_name == '':
        #file_name = input('Name of the file:')
        #file_name = file_name + '.txt'
        #file = open(file_name,'w')
    #else:
    try:
        file = open('pride.txt','a')
    except IOError:
        #print('File not found.')
        #file_name = input('File Location')
        file = open('pride.txt','a')

    teacher = ''

    while 1:
        if teacher == '':
            teacher = input("Teacher Name:")
            grade = input("Grade:")
        student_lastname = input("Student Last Name:")
        student_firstname = input("Student First Name:")
        pride = grade + '::' + student_lastname + '::' + student_firstname + '::' + teacher

        print(pride)
        cmd = input("Command:")
        if cmd == '':
            pass
        elif cmd == 'nteacher':
            teacher = input('Teacher Name:')
            grade = input('Grade:')
        elif cmd == 'ngrade':
            grade = input("Grade:")
        elif cmd =="exit":
            file.write(pride + '\n')
            file.close()
            break
        elif cmd =='change':
            grade = input("Grade:")
            student_lastname = input("Student Last Name:")
            student_firstname = input("Student First Name:")
            pride = grade + '::' + student_lastname + '::' + student_firstname + '::' + teacher
            nxt = input('Are there more students? (Y/n):')
            if nxt == 'y' or nxt =='Y':
                pass
            elif nxt == 'n' or nxt == 'N':
                file.write(pride + ' \n')
                file.close()
                break
            gra_lev = input('Is the next student the same grade? (Y/n):')
            if gra_lev == 'Y' or gra_lev =='y':
                pass
            elif gra_lev == 'n' or gra_lev == 'N':
                grade = input('Grade:')
            teach = input('Is the next student the same teacher? (Y/n):')
            if teach == 'Y' or teach == 'y':
                pass
            elif teach == 'n' or teach == 'N':
                teacher = input("Teacher:")
        file.write(pride + '\n')
    print("Program exit")
    quit


def readable():
    import re

    try:
        file = open('Result.txt','r')
        nfile = open('Readable Results.txt','w')
    except IOError:
        print('Error opening')
        exit

    remove =re.compile(r'\\n')

    pteacher = ''

    nfile.write('Renaissance Card Results\n\n')

    wildcat = 1
    bronze = 1
    silver = 1
    gold = 1
    platinum = 1

    for line in file.readlines():
        line1=line.split('::')
        #print(line1)
        if pteacher == line1[3]:
            if line1[4] == 'wildcat\n':
                wildcat =+ 1
            elif line1[4] == 'bronze \n':
                bronze =+ 1
            elif line1[4] == 'silver \n':
                silver =+ 1
            elif line1[4] == 'gold \n':
                gold =+ 1
            elif line1[4] == 'platinum \n':
                platinum =+ 1
        elif pteacher == '':
            wildcat = 1
            bronze = 1
            silver = 1
            gold = 1
            platinum = 1
            nfile.write('Teacher:' + line1[3] +'\n')
        elif pteacher != line1[3]:
            wildcat = str(wildcat)
            bronze = str(bronze)
            silver = str(silver)
            gold = str(gold)
            platinum = str(platinum)
            #print('Total Cards: Wilcat: ' + wildcat + ' Bronze:'+ bronze + ' Silver:'+ silver + ' Gold:'+ gold + ' Platinum:' + platinum +'\n')
            #nfile.write('Total Cards: Wildcat: ' + wildcat + ' Bronze:'+ bronze + ' Silver:'+ silver + ' Gold:'+ gold + ' Platinum:' + platinum +'\n')
            nfile.write('\n')
            nfile.write('Teacher:' + line1[3] +'\n')
            wildcat = 1
            bronze = 1
            silver = 1
            gold = 1
            platinum = 1
        re.sub(remove,'',line[4])
        new_line = line1[0] + ':' + line1[1] + ', ' + line1[2] + ' = ' + line1[4]
        pteacher= line1[3]
        #print(pteacher)
        print(new_line)
        nfile.write(new_line)

    wildcat = str(wildcat)
    bronze = str(bronze)
    silver = str(silver)
    gold = str(gold)
    platinum = str(platinum)
    nfile.write('Total Cards: Wildcat: ' + wildcat + ' Bronze:'+ bronze + ' Silver:'+ silver + ' Gold:'+ gold + ' Platinum:' + platinum +'\n')

    file.close()
    nfile.close()


def counting():
    "Ren Card Count"
    print("Counting Mode")
    import re
    import os
    import datetime

    name_file = input('File location for Student Database:')
    #name_file = 'C:\\Users\\leekevin\\Desktop\\gpa.txt'
    #name_file = 'gpa.txt'
    #pride_file = 'C:\\Users\\leekevin\\Desktop\\Pride.txt'
    #pride_file = 'Pride.txt'
    pride_file = input('File location for Pride classes:')

    try:
        number_file = open('Number.txt','w')
        compiled_file = open("Result.txt",'a')
    except IOError:
        compiled_file = open("Result.txt",'w')

    namef = 'not found'
    pridef = 'not found'

    try:
        names = open(name_file,'r')
        namef = 'found'
        pride = open(pride_file,'r')
        pridef = 'found'
    except IOError:
        print('Files not found')
        print('Names file =', namef)
        print('Pride file =', pridef)

    remove_pat = re.compile = (r'\n')

    #Sorting
    for pline in pride.readlines():
        pline1 = re.sub(remove_pat,'',pline)
        pline2 = pline1.split("::")
        compiled_line = pline1 + '::' + 'wildcat' + '\n'
        names.seek(0)
        for nline in names.readlines():
            nline = re.sub(remove_pat,'',nline)
            nline = nline.split("::")
            level = nline[4]
            if pline2[0:3] == nline[0:3]:
                compiled_line = pline1+ '::' + level + '\n'
        compiled_file.write(compiled_line)
        print(compiled_line)

    compiled_file.close()

    #Counting
    compiled = open("Result.txt",'r')
    total = 0
    no = 0
    wildcat = 0
    bronze = 0
    silver = 0
    gold = 0
    platinum = 0

    for line in compiled.readlines():
         line = re.sub(remove_pat,'',line)
         line = line.split("::")
         total = total + 1
         print(line)
         if line[4] == 'none ':
             no = no + 1
         elif line[4] == 'wildcat':
             wildcat = wildcat + 1
         elif line[4] == 'bronze ':
             bronze = bronze + 1
         elif line[4] == 'silver ':
             silver = silver + 1
         elif line[4] == 'gold ':
             gold = gold + 1
         elif line[4] == 'platinum ':
             platinum = platinum + 1
         #else:
            #print(line)

    date_time = str(datetime.datetime.now())
    total = str(total)
    no = str(no)
    wildcat = str(wildcat)
    bronze = str(bronze)
    silver = str(silver)
    gold = str(gold)
    platinum = str(platinum)

    stuff = 'Summary of the Total Counts generated:'+ date_time +'\n' + 'Totals:'+ total + ' No Card:'+ no +' Wildcat:'+ wildcat + ' Bronze:'+ bronze + ' Silver:'+ silver + ' Gold:'+ gold + ' Platinum:' + platinum
    number_file.write(stuff)

    #compiled_file.close()
    compiled.close()
    readable()
    print("Done")


def help():
    "Guide"
    print("Commands employed:\n",'nteacher = New teacher\n','ngrade = New Grade\n','change = change the previous entry\n','exit = Exit Program')
    cmd = input('Mode:')
    if cmd == 'gpa':
        gpa()
    elif cmd == 'pride':
        pride()
    elif cmd == 'count':
        counting()
    elif cmd == 'exit':
        print('Program out')
        quit

print("Renaissance Card Database\n",'Version 2013 beta\n','Granted use under the Creative Commons License: Attribution-NonCommercial-ShareAlike 3.0 Unported\n')
print('For more information about the Creative Commons License, please visit their site at: www.creativecommons.org\n')
print("Welcome! Please type in the mode that you want to enter:\n",'gpa\n','pride\n','count\n','help\n')
cmd = input("Mode:")
if cmd == 'gpa':
    gpa()
elif cmd == 'pride':
    pride()
elif cmd == 'count':
    counting()
elif cmd == 'help':
    help()
elif cmd == 'exit':
    quit
else:
    print('Command not found, please try again.')
    cmd = input("Mode:")
    if cmd == 'gpa':
        gpa()
    elif cmd == 'pride':
        pride()
    elif cmd == 'count':
        counting()
    elif cmd == 'help':
        help()
    elif cmd == 'exit':
        quit
