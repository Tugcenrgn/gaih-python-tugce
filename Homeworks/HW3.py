#Tuğçe Nur Ergen
#Course Grade Application

student1= str(input("Name Surname: "))
midterm1 = float(input("Midterm Grade: "))
project1= float(input("Project Grade: "))
final1 = float(input("Final Grade: "))

student2= str(input("NameSurname: "))
midterm2 = float(input("Midterm Grade: "))
project2= float(input("Project Grade: "))
final2= float(input("Final Grade: "))

student3= str(input("Name Surname: "))
midterm3 = float(input("Midterm Grade: "))
project3= float(input("Project Grade: "))
final3= float(input("Final Grade: "))

student4= str(input("Name Surname: "))
midterm4 = float(input("Midterm Grade: "))
project4= float(input("Project Grade: "))
final4= float(input("Final Grade: "))

student5= str(input("Name Surname: "))
midterm5 = float(input("Midterm Grade: "))
project5= float(input("Project Grade: "))
final5= float(input("Final Grade: "))

passingGrade1= midterm1 * (0.3) + project1 * (0.3) + final1 * (0.4)
passingGrade2= midterm2 * (0.3) + project2 * (0.3) + final2 * (0.4)
passingGrade3= midterm3 * (0.3) + project3 * (0.3) + final3 * (0.4)
passingGrade4= midterm4 * (0.3) + project4 * (0.3) + final4 * (0.4)
passingGrade5= midterm5 * (0.3) + project5 * (0.3) + final5 * (0.4)

students={
'student1':{
    'midterm':midterm1,
    'project':project1,
    'final':final1,
    'passingGrade': passingGrade1
},
'student2':{
    'midterm':midterm2,
    'project': project2,
    'final': final2,
    'passingGrade': passingGrade2
},
'student3':{
    'midterm': midterm3,
    'project': project3,
    'final': final3,
    'passingGrade': passingGrade3
},
'student4':{
    'midterm': midterm4,
    'project': project4,
    'final': final4,
    'passingGrade': passingGrade4
},
'student5':{
    'midterm': midterm5,
    'project': project5,
    'final': final5,
    'passingGrade': passingGrade4
}
}

list = [passingGrade1, passingGrade2, passingGrade3,passingGrade4,passingGrade5]
list.sort()
list.reverse()

print("-DEGREE-")
print(str(student1)+ " " +str(list[0]))
print(str(student2)+ " " +str(list[1]))
print(str(student3)+ " " +str(list[2]))
print(str(student4)+ " " +str(list[3]))
print(str(student5)+ " " +str(list[4]))

