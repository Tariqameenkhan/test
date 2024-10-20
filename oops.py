# class car ():
#     def __init__(self,model) -> None:
#         print("blue")
#         self.model=model

# car1=car("honda")
# car2=car("todo")
# print(car2.model)
# print(car1.model)

# class student:
#     name = "ali"

# s1=student()
# print(s1.name)

# class student():
#    def __init__(self) -> None:
#       print("ali")

# s1=student()

# class Student:
#    school ="abc"
#    def __init__(self,name:str,marks:int) -> None:
#       self.name=name
#       self.marks=marks
      

# s1=Student(name="ali",marks=1234)
# s2=Student("khan",3456)
# print(s1.name,s1.marks)
# print(s1.school)
# print(s2.name,s2.marks)
# print(s2.school)


# class student:
#    def __init__(self) -> None:
#       print("ali")
      
#    def hi (self):
#       print("hello")
         

# s1=student()
# s1.hi()


# class Student:
#    school ="abc"
#    def __init__(self,name:str,marks:int) -> None:
#       self.name=name
#       self.marks=marks
#    def mar (self) :
#       return self.marks 
#    def hi (self):
#       print("hello",self.name)

# s1=Student(name="ali",marks=1234)
# s2=Student("khan",3456)
# print(s1.name,s1.marks)
# print(s1.school)
# print(s2.name,s2.marks)
# print(s2.school)
# print(s1.mar())
# s1.hi()

# class student:
#     def __init__(self,name,marks) -> None:
#         self.name=name
#         self.marks=marks
    
#     def aver (self):
#         sum= 0
#         for val in self.marks:
#           sum += val
#         print("average",sum/3*100)
        

# s1=student("ali",[123,456,789])       

# s1.aver()
# class student:
#     def __init__(self, name: str, marks) -> None:
#         self.name = name
#         self.marks = marks
    
#     def aver(self):
#         sum = 0
#         for val in self.marks:
#             sum += int(val)  # Convert each mark to an integer, just in case
#         print("average", sum / len(self.marks))  # Divide by the number of marks, not a hardcoded 3

# s1 = student("ali", [123, 333, "444"])  # "444" will be converted to an integer
# s1.aver()

