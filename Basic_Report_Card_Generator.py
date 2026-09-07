print("=========================================  *******  =============================================")
#up to 7th line inputs are taken from the users for the information of the students
A=input("Enter The Name of the Student:")
print("============================  REPORT CARD OF "+A+"  ====================================")
a=int(input ("Enter no of Subjects:"))
B=int(input("Enter The Roll Number of The Student:"))
C=int(input("Enter the total marks by adding every subject total marks:"))
#this list is used to store the names of the subjects
c=[]
#this list is used to store the marks of the respective subjects of the subjects which were entered
d=[]
for i in range (1,a+1):
   b=input("Enter the names of the Subjects:")
   c.append(b)
for j in range (1,a+1):
   e=int(input("Enter the marks of the respective Subjects : "))
   d.append(e)
s=0
for k in (d):
   s=s+k
print(s)
#this loop is used to print the subjects and the respective marks 
for c,d in zip(c,d):
   print(f"{c}:{d}")
print("=======================  Total marks obtained by "+A+" : "+str(s)+"  ===========================")
formula=(s/C)*100
print("=====================  The percentage Obtained by "+A+":"+str(formula)+"%  ==========================")
#the below conditions are to print the grades and the perforamane of the students
if formula >=90:
   print("Very good, maintain the score")
elif formula>=75 :
   print("Good, try to score more")
elif formula>=50:
   print("Try to get more, practice more")
elif formula>=35:
   print("you were just passed,")
else:
   print("you failed in the exam!!!")




