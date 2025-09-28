# Question:
# Create a Student class with:
# A class attribute school_name.
# An instance attribute name.
# An instance mehod show().
# A class method update_school().
# A static method is_adult(age).

class student:
    school_name= "bharat english high school"

    def __init__(self,name,age):
        self.name= name
        self.age =age
    
    def show(self):
        print(f"student details are: {self.name}, {self.age}, {student.school_name}")

    @classmethod
    def update_school(cls, new_school):
        cls.school_name = new_school
        print(f"school name is updated to {new_school} ")

    # @staticmethod
    # def is_adult(age):
    #     return age >=18 
    # here we have to provide age to check 

    def is_adult(self):
        return self.age>=18


    

stu1 = student("aqsa shah", 21)
stu2 = student("tabish shaikh", 22)
stu3 = student("afreen shaikh", 18)
stu4 = student("sumaiiyaaa", 15)
stu5 = student("faiza", 17)

stu1.show()
stu2.show()
stu3.show()
stu3.show()
stu4.show()
stu5.show()

student.update_school("mosco international school")

stu1.show()
stu2.show()
stu3.show()
stu3.show()
stu4.show()
stu5.show()

print(stu1.is_adult())
print(stu2.is_adult())
print(stu3.is_adult())
print(stu4.is_adult())
print(stu5.is_adult())