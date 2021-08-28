from statistics import mean as M
import statistics

admins = {'Python':'Pass123@'}

studentsDict = {'Jeff': [78, 88, 93], 
                'Alex': [92, 76, 88], 
                'Jack': [95, 85, 80]}

def enterGrades():
    nameToEnter = input('Student Name: ')
    gradeToEnter = input('Grade: ')
    
    if nameToEnter in studentsDict:
        print('Adding Grade...')
        studentsDict[nameToEnter].append(float(gradeToEnter))
    else:
        print('Student does not exist.' )
        
    print(studentsDict)
    
def removeStudent():
    nameToRemove = input('What student to remove?: ')
    if nameToRemove in studentsDict:
        print('Removing student...')
        del studentsDict[nameToRemove]
        
def averageGrades():
    for eachStudent in studentsDict:
        gradeList = studentsDict[eachStudent]
        avgGrade = M(gradeList)
        
        print(eachStudent, 'has an average grade of:', avgGrade)
    
def main():
    print('''
    Welcome to Grade Central
    
    [1] - Enter Grades
    [2] - Remove Student
    [3] - Student Average Grades
    [4] - Exit      
          
    ''')
    
    action = input('What you like to do today? (Enter a Number)')
    
    if action == '1':
        enterGrades()
    elif action == '2':
        removeStudent()
    elif action == '3':
        averageGrades()
    elif action == 4:
       exit() 
    else:
        print('No valid choice was given... Try again!')
        
login = input('Username: ')
passw = input('Password: ')

if login in admins:
    if admins[login] == passw:
        print('Welcome, ',login)
        while True:
            main()
    else:
        print('Invalid password!')
else:
    print('Invalid username!')