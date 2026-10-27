#Activity01
class Student:
    grade=10
    print("hi there i am in grade",grade)

ob=Student()

#Activity02
class Student:
    grade=10
    name="ali"

    def introduction(self):
        print("hi there i am in grade",self.grade,"my name is",self.name)
    def details(self):
        print("hi there i am in grade",self.grade,"my name is",self.name,"and i am a student")

ob=Student()
ob.introduction()
ob.details()

#Activity03
class Parrot:
    species="bird"

    def __init__(self,name,age):
        self.name=name
        self.age=age
blu=Parrot("Blu",10)
woo=Parrot("Woo",15)

print("blu is a",blu.species)   
print("Woo is a",woo.species)

print("{} is {} years old".format(blu.name,blu.age))
print("{} is {} years old".format(woo.name,woo.age))


#Activity04
class Parrot:
    def __init__(self,name,age):
        self.name=name
        self.age=age    
    def sing(self,song):
        return "{} sings {}".format(self.name,song) 
    def dance(self,dance):
        return "{} dances {}".format(self.name,dance)
    
blu=Parrot("Blu",10)
woo=Parrot("Woo",15)

print("blu sings",blu.sing("Happy"))
print("Woo sings",woo.sing("Happy"))
print("blu dances",blu.dance("Happy"))
print("Woo dances",woo.dance("Happy"))

      
