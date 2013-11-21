#-----------------------------------------------------
#PRIDE Reader
#-----------------------------------------------------
def decider():
    import re
    prev_teacher = []
    teacher_pat = re.compile(r'(?P<pat>Teache)'r'(?P<teacher_last>[-a-zA-Z]+, [-a-zA-Z]+)')
    student_pat = re.compile(r'(?P<gender>[FM] )'r'(?P<grade>\d\d)'r'(?P<name>[-a-zA-Z ]+, [-a-zA-Z ]+)')
    for line in file.readlines():
        teacher = teacher_pat.findall(line)
        student = student_pat.findall(line)
        if teacher != []:
            #print(teacher[0][1])
            if prev_teacher == teacher[0][1]:
                pass
            else:
                print(teacher[0][1])
                prev_teacher = teacher[0][1]
        elif student != []:
            #print(student[0][0:3])
            student = list(student[0][0:])\
            #student[0][1]= float(student[0][1]) #Needs fixing, cannot convert string to float
            student.append(prev_teacher)
            print(student[0][1])



def teacher_find():
    'Teacher extractor'
    import re
    prev_teacher = []
    #teacher_pat = re.compile(r'(?P<pat>Teache)'r'(?P<teacher_last>[-a-zA-Z]+, [-a-zA-Z]+)')
    for line in file.readlines():
        teacher = teacher_pat.findall(line)
        if teacher == []:
            pass
        else:
            #print(teacher[0][1])
            if prev_teacher == teacher[0][1]:
                pass
            else:
                print(teacher[0][1])
                prev_teacher = teacher[0][1]


#'r' (?P<middle_name>[-a-zA-Z]+)?'
def student_find():
    'Student extractor'
    import re
    record = open('Record.txt','w')
    count = 0
    #student_pat = re.compile(r'(?P<gender>[FM] )'r'(?P<grade>\d\d  )'r'(?P<name>[-a-zA-Z ]+, [-a-zA-Z ]+)')
    check_stu = []
    for line in file.readlines():
        student = student_pat.findall(line)
        #print(student)
        if student == []:
            pass
        else:
            print(list(student[0][0:3]))
            student = str(student[0][0:2])
            record.write(student + '\n')
            count = count + 1
    print(count)
    print('1616 students')

#file_name = input('File Name: ')
file_name = 'PRIDE'
try:
    file = open(file_name + '.txt', 'r')
except IOError:
    print('File not found')

decider()
