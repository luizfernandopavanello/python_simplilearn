gradeDict = {'Kelly': 89, 'David':65, 'Jack':95, 'Samantha': 78}

print('→',gradeDict)
print(gradeDict['Jack'])

gradeDict['David'] = 85
print('→',gradeDict)

gradeDict['Jessy'] = 80
print('→',gradeDict)

del gradeDict['Samantha']
print('→',gradeDict)

gradeDict = {'Kelly': [89, 88],
             'David': [65, 70],
             'Jack': [95, 85],
             'Samantha': [78, 85]}

print('→',gradeDict)
print('Jack →',gradeDict['Jack'])
print('Jack Test 2 →',gradeDict['Jack'][1])


