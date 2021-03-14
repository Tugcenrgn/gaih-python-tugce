#Tuğçe Nur Ergen
#Course Grade Application

listOfMidterms= [0,0,0,0,0]
listOfProjects=[0,0,0,0,0]
listOfFinals=[0,0,0,0,0]
listOfStudents=[0,0,0,0,0]
for i in range(0,5):
    listOfStudents[i]= str(input("Name Surname: "))
    listOfMidterms[i]=float(input("Midterm Grade: "))
    listOfProjects[i]=float(input("Project Grade: "))
    listOfFinals[i]= float(input("Final Grade: "))

def passingCalculate(midterm,project,final):
      passingGrade = midterm*(0.3) + project*(0.3) + final*(0.4)
      return passingGrade
    

passingGrade1= passingCalculate(listOfMidterms[0],listOfProjects[0],listOfFinals[0])
passingGrade2= passingCalculate(listOfMidterms[1],listOfProjects[1],listOfFinals[1])
passingGrade3= passingCalculate(listOfMidterms[2],listOfProjects[2],listOfFinals[2])
passingGrade4= passingCalculate(listOfMidterms[3],listOfProjects[3],listOfFinals[3])
passingGrade5= passingCalculate(listOfMidterms[4],listOfProjects[4],listOfFinals[4])
students={
'student1':{
    'name-Surname': listOfStudents[0],
    'midterm':listOfMidterms[0],
    'project':listOfProjects[0],
    'final':listOfFinals[0],
    'passingGrade': passingGrade1
},
'student2':{
    'name-Surname': listOfStudents[1],
    'midterm':listOfMidterms[1],
    'project':listOfProjects[1],
    'final':listOfFinals[1],
    'passingGrade': passingGrade2
},
'student3':{
    'name-Surname': listOfStudents[2],
    'midterm':listOfMidterms[2],
    'project':listOfProjects[2],
    'final':listOfFinals[2],
    'passingGrade': passingGrade3
},
'student4':{
    'name-Surname': listOfStudents[3],
    'midterm':listOfMidterms[3],
    'project':listOfProjects[3],
    'final':listOfFinals[3],
    'passingGrade': passingGrade4
},
'student5':{
    'name-Surname': listOfStudents[4],
    'midterm':listOfMidterms[4],
    'project':listOfProjects[4],
    'final':listOfFinals[4],
    'passingGrade': passingGrade4
}
}
list = [passingGrade1, passingGrade2, passingGrade3,passingGrade4,passingGrade5]
list.sort()
list.reverse()

print("-DEGREE-")
print(str(students['student1']['name-Surname'])+ " " +str(list[0]))
print(str(students['student2']['name-Surname'])+ " " +str(list[1]))
print(str(students['student3']['name-Surname'])+ " " +str(list[2]))
print(str(students['student4']['name-Surname'])+ " " +str(list[3]))
print(str(students['student5']['name-Surname'])+ " " +str(list[4]))
