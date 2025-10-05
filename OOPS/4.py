# 2️⃣ POLYMORPHISM — Method Overriding + Duck Typing

# 🧩 Question:
# Create a Python program that demonstrates Polymorphism using:

# Method overriding (same method name, different implementation in child class).

# Duck typing (no inheritance, just same method name used in different unrelated classes).

# 💡 Hint:

# Create a Bird class with a speak() method → "Chirp!"

# Create a Dog class with a speak() method → "Woof!"

# Create a function make_it_speak(animal) that calls animal.speak()

# Create a Parrot class inheriting Bird and override speak() → "I can talk!"

# Call make_it_speak() for all three classes to show polymorphic behavior.


# 2️⃣ POLYMORPHISM — Method Overriding + Duck Typing

# 🦜 Base class
class Bird:
    def speak(self):
        print("Chirp! 🐦")  # Default bird sound


# 🐶 Unrelated class (no inheritance)
class Dog:
    def speak(self):
        print("Woof! 🐕")  # Dog sound


# 🦚 Child class overriding the parent method
class Parrot(Bird):
    def speak(self):
        print("I can talk! 🦜")  # Overridden method


# 🧩 Function demonstrating Duck Typing
def make_it_speak(animal):
    # We don’t care what class it is — as long as it has a 'speak' method
    animal.speak()


# 🧪 Creating objects
bird = Bird()
dog = Dog()
parrot = Parrot()

# 🎬 Demonstrating polymorphism
print("🔹 Method Overriding Example:")
parrot.speak()   # Parrot overrides Bird’s speak()

print("\n🔹 Duck Typing Example:")
make_it_speak(bird)    # Works because Bird has speak()
make_it_speak(dog)     # Works because Dog has speak()
make_it_speak(parrot)  # Works because Parrot has speak()
