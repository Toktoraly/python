students =[]

s_file = open("student.txt","r")

for line in s_file:
    students = line.strip("\n")
    studnets.append(student)
print (students)

while True:
    st_name = input("write student name: ")

    if st_name = "done":
        break
    students.append(st_name)

s_file = open('student.txt','w') 

for student in students:
    s_file.write(student+"\n")

s_file.close

print (students)
