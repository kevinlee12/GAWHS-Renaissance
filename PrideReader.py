#-----------------------------------------------------
#PRIDE Reader
#-----------------------------------------------------
def teacher():
    import re
    teacher_pat = re.compile(r'(?P<pat>Teache)'r'(?P<teacher_last>[-a-zA-Z]+, [-a-zA-Z]+)')
    check = []
    for line in file.readlines():
        teacher = teacher_pat.findall(line)
        if teacher == []:
            pass
        else:
            print(teacher[0][1])

def student():
    import re
    student_pat = re.compile(r'(?P<gender>[FM] )'r'(?P<grade>\d\d  )'r'(?P<name>[-a-zA-Z]+, [-a-zA-Z]+)'r' (?P<middle_name>[-a-zA-Z]+)?')
    check_stu = []
    count = 0
    for line in file.readlines():
        student = student_pat.findall(line)
        #print(student)
        if student == []:
            pass
        else:
            print(student[0])
            count = count + 1
    print(count)


#file_name = input('File Name: ')
file_name = 'PRIDE'
try:
    file = open(file_name + '.txt', 'r')
except IOError:
    print('File not found')

student()
