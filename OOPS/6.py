# 4️⃣ ABSTRACTION — Using abc Module (Abstract Class + Abstract Method)

# 🧩 Question:
# Create an abstract class using Python’s abc module to demonstrate Abstraction.

# 💡 Hint:

# Import ABC and abstractmethod from abc.

# Create an abstract class Shape with:

# An abstract method area()

# A concrete method description() that prints "This is a shape."

# Create subclasses Circle and Rectangle that implement the area() method.

# Show that you cannot instantiate the Shape class directly, but you can instantiate its subclasses.

# Display the area() for both Circle and Rectangle.


# 4️⃣ ABSTRACTION — Using abc Module (Abstract Class + Abstract Method)

from abc import ABC, abstractmethod   # ✅ Importing required classes


# 🧩 Abstract Base Class
class Shape(ABC):
    # Concrete method — common to all shapes
    def description(self):
        print("📐 This is a shape.")

    # Abstract method — must be implemented by subclasses
    @abstractmethod
    def area(self):
        pass


# ⚪ Subclass 1 — Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Implementation of abstract method
    def area(self):
        return 3.14 * self.radius * self.radius


# ⬛ Subclass 2 — Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Implementation of abstract method
    def area(self):
        return self.length * self.width


# 🧪 Testing the concept
# shape = Shape()   # ❌ ERROR: Can't instantiate abstract class

circle = Circle(7)
rectangle = Rectangle(10, 5)

print("🔹 Circle Details:")
circle.description()                # inherited concrete method
print(f"Area of Circle: {circle.area()}")

print("\n🔹 Rectangle Details:")
rectangle.description()             # inherited concrete method
print(f"Area of Rectangle: {rectangle.area()}")
