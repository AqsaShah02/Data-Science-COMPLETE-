# 1️⃣ INHERITANCE — All Types (Single, Multiple, Multilevel) + super() + Constructor

# 🧩 Question:
# Write a Python program to demonstrate Single, Multiple, and Multilevel inheritance.
# Your code must:

# Include constructors in all parent classes.

# Use super() to call the parent constructor inside the child class.

# Demonstrate how Method Resolution Order (MRO) works when multiple parents are inherited.

# Show how attributes and methods are accessed from each level of inheritance.

# 💡 Hint:
# Include:

# A Grandparent class with family_name

# A Parent class inheriting Grandparent, adding parent_name

# A Mother class as a second parent

# A Child class inheriting both Parent and Mother

# Demonstrate constructor execution order and method inheritance.

class grandparent:
    person = "Mr. Shah"

    def __init__(self, surname):
        self.surname = surname

    def show(self):
        print(f"The person of this family will be called as {self.person}")


class parent(grandparent):
    def __init__(self, surname, middlename):
        grandparent.__init__(self, surname)
        self.middlename = middlename


class father(parent):
    def __init__(self, surname, middlename, name):
        parent.__init__(self, surname, middlename)
        self.name = name

    def show(self):
        print(f"The father name is: {self.name} {self.middlename} {self.surname}")


class mother(parent):
    def __init__(self, surname, middlename, name):
        parent.__init__(self, surname, middlename)
        self.name = name

    def show(self):
        print(f"The mother name is: {self.name} {self.middlename} {self.surname}")


class child(mother, father):
    def __init__(self, surname, middlename, name):
        # Call both parent constructors explicitly (no super!)
        father.__init__(self, surname, middlename, "Abdul Rehman")
        mother.__init__(self, surname, middlename, "Juveria")
        self.child_name = name
        print("Child constructor called")

    def show_child(self):
        print(f"The child name is: {self.child_name} {self.middlename} {self.surname}")


# Creating objects
dad = father("Shah", "Abdul", "Rehman")
mom = mother("Shah", "Juveria", "Fatima")
kid = child("Shah", "Aqsa", "Abdul Rehman")

# Display
dad.show()
mom.show()
kid.show_child()
