#Tuğçe Nur Ergen
#List application: hw1

list1 = []  #odd numbers
list2 = []  #even numbers

for i in range(1,10):
    num = int(input("Please enter a number: "))

    if (num%2==0): #this list will keep even numbers
        list2.append(num)
        
    elif (num%2!= 0): #this list will keep odd numbers
        list1.append(num)

print("1. Odd numbers:"+ str(list1))
print("2. Even numbers:" +str(list2))

list1.extend(list2)
print("Extended list:" + str(list1)
      )  #main list is list1

for i in range(0,9):
    list1[i]=list1[i]*2
list1.sort()
print("Multiplied each value in our list by 2 and sorted \n"+ str(list1))

print("\n data types of the elements in the list:\n")
for i in range(0,9):
    print(type(list1[i]))
    

 
