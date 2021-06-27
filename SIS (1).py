
def addingStudent():
    studentData = {}
    data = {}
    Name = input('Enter Fullname: ')
    idNumber = input('Enter ID Number: ')
    yearLevel = input('Enter Year Level: ')
    Gender = input('Enter Gender: ')
    Course = input('Enter Course: ')
    print('Student added successfully')
    print('\n')

    studentData['Name'] = Name
    studentData['idNumber'] = idNumber
    studentData['yearLevel'] = yearLevel
    studentData['Gender'] = Gender
    studentData['Course'] = Course

    data[idNumber] = studentData
    return data

def updateStudent(listOfStudents):
    idNumber = input('Enter ID number to update data: ')
    listOfId = []
    for mail in listOfStudents:
        listOfId.append(list(mail.keys())[0])
    check = listOfId.index(idNumber)
    if check >= 0:
        print('To update Name: Enter Name')
        print('To update Id Number: Enter Id Number')
        print('To update Year Level: Enter Year Level')
        print('To update Gender: Enter Gender')
        print('To update Course: Enter Course')
    userOpt = input('Enter user option: ')

    length = len(listOfStudents)
    for i in range(length):
        if idNumber == list(listOfStudents[i].keys())[0]:
            if userOpt == 'Name':
                listOfStudents[i][idNumber]['Name'] = input('Enter the name: ')
            elif userOpt == 'Id Number':
                listOfStudents[i][idNumber]['idNumber'] = input('Enter Id Number: ')
            elif userOpt == 'Year Level':
                listOfStudents[i][idNumber]['yearLevel'] = input('Enter Year Level: ')
            elif userOpt == 'Gender':
                listOfStudents[i][idNumber]['Gender'] = input('Enter Gender: ')
            elif userOpt == 'Course':
                listOfStudents[i][idNumber]['Course'] = input('Enter Course: ')


    print('Student details updated successfully')

def deleteStudent(listOfStudents):
    idNumber = input('Enter ID number: ')
    listOfId = []
    try:
        for mail in listOfStudents:
            listOfId.append(list(mail.keys())[0])
        check = listOfId.index(idNumber)
        length = len(listOfStudents)
        if check >= 0:
            for i in range(length):
                if idNumber == list(listOfStudents[i].keys())[0]:
                    del listOfStudents[i]
                    break
        else:
            print('Entered ID number is wrong')
        print('Student deleted successfully')
    except ValueError:
        print("Student not in the list.")


def readData(listOfStudents):
    idNumber = input('Enter ID number: ')
    listOfId = []
    try:
        for mail in listOfStudents:
            listOfId.append(list(mail.keys())[0])
        check = listOfId.index(idNumber)
        length = len(listOfStudents)
        if check >= 0:
            for i in range(length):
                if idNumber == list(listOfStudents[i].keys())[0]:
                    print(listOfStudents[i])
                    break
        else:
            print('No student found')
    except ValueError:
        print("Student data doesn't exist")


print('List of options')
studentDetails = {}
listOfData = []
while True:
    print('To add new student details, press (1)')
    print('To update students details, press (2)')
    print('To delete student details, press (3)')
    print('To view student details, press (4)')
    print('\n')
    print()
    UserOption = input('Select an option above: ')
    if UserOption == '1':
        returnedData = addingStudent()
        listOfData.append(returnedData)
    elif UserOption == '2':
        updateStudent(listOfData)
    elif UserOption == '3':
        deleteStudent(listOfData)
    elif UserOption == '4':
        readData(listOfData)




