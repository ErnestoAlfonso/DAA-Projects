from source import *
a=Student("P", 1)
b=Student("P", 1)
c=Student("P", 2)
d=Student("P", 3)
e=Student("P", 3)
f=Student("R", 5)
g=Student("R", 2)
h=Student("R", 4)
i=Student("R", 4)
j=Student("R", 5)

list_stud = [a,b,c,d,e,f,g,h,i,j]

result=Solve(list_stud,3)
print(result)
