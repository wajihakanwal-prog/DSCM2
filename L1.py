class_mates=["ali","ahmad","mohammad","reza","saad"]
print(class_mates)

print("Total class mates",len(class_mates))
print("First student",class_mates[0])
print("Last student",class_mates[-1])
print("First threee ",class_mates[0:3])


class_mates.append("sara")
print(class_mates)
class_mates.insert(0,"sara")
print(class_mates)
class_mates.remove("sara")
print(class_mates)
class_mates.pop(0)
print(class_mates)
class_mates.sort()
print(class_mates)
class_mates.reverse()
print(class_mates)
print(class_mates.index("ali")) 

teacher={"name":"Mr. Ali","subject":"Math","experience":10}
print(teacher)
print("name: ",teacher["name"])
print("subject: ",teacher["subject"])
print("experience: ",teacher["experience"])
teacher["email"]="ali@gmail.com"
print(teacher)

roll_numbers=[1,2,3,4,5]
names=["ali","ahmad","mohammad","reza","saad"]
student_directory=dict(zip(roll_numbers,names))
print(student_directory)
print("Total students",len(student_directory))
print("First student",student_directory[1])
