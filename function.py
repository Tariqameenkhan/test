# password = "123"
# def pas (password):
#     password = ""  
#     while password != "123":
#        password = int(input("enter password :"))
#     print( "correct")
        
# pas(password)   


# def greet(name="ali", message="hello"):
#     print(f"Hello  {message} , {name}")

# greet() 

# def sum (**kar):
#     print(**kar)
    
# print(a="ali",b ="khan")


# def function_name(**kwargs):
#     # kwargs is a dictionary containing all keyword arguments
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# function_name(a="ali" , b = "khan")       


# sum = lambda x,y:x+y
# print(sum(2,6))


def get_marks(subject_name):
    while True:
        try:
            marks = int(input(f"Enter {subject_name} marks obtained (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Error: Marks must be between 0 and 100. Please enter a valid mark.")
        except ValueError:
            print("Error: Please enter a valid integer.")
def get_subject(subject_number):
    return input(f"Enter subject {subject_number} name: ")

# Collect subject names and marks
subject1 = get_subject(1)
subject1_marks = get_marks(subject1)

subject2 = get_subject(2)
subject2_marks = get_marks(subject2)

subject3 = get_subject(3)
subject3_marks = get_marks(subject3)

subject4 = get_subject(4)
subject4_marks = get_marks(subject4)

# Calculate total marks and percentage
total_marks = subject1_marks + subject2_marks + subject3_marks + subject4_marks
percentage = (total_marks / 400) * 100             