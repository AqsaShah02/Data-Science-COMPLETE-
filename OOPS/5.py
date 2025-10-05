# 3️⃣ ENCAPSULATION — Public, Protected, Private

# 🧩 Question:
# Write a Python program to demonstrate Encapsulation using:

# Public, protected (_var), and private (__var) attributes.

# Public, protected, and private methods.

# Accessing and modifying them from outside and inside the class.

# 💡 Hint:

# Create a class BankAccount with:

# Public attribute → account_holder

# Protected attribute → _balance

# Private attribute → __pin

# Add methods:

# deposit(amount) → public

# _calculate_interest() → protected

# __show_pin() → private

# Try accessing each from outside the class and inside another derived class SavingsAccount to show which ones are accessible.


# 3️⃣ ENCAPSULATION — Public, Protected, Private

class BankAccount:
    def __init__(self, holder, balance, pin):
        # Public attribute
        self.account_holder = holder
        
        # Protected attribute (single underscore)
        self._balance = balance
        
        # Private attribute (double underscore)
        self.__pin = pin

    # Public method
    def deposit(self, amount):
        self._balance += amount
        print(f"✅ Deposited ₹{amount}. New balance: ₹{self._balance}")

    # Protected method
    def _calculate_interest(self):
        interest = self._balance * 0.05
        print(f"💰 Interest (5%) on balance: ₹{interest}")
        return interest

    # Private method
    def __show_pin(self):
        print(f"🔒 Your account PIN is: {self.__pin}")

    # Public method to access private data safely
    def access_private(self):
        print("Accessing private details safely:")
        self.__show_pin()


# 🏦 Derived class
class SavingsAccount(BankAccount):
    def __init__(self, holder, balance, pin):
        super().__init__(holder, balance, pin)

    def show_details(self):
        print(f"👤 Account Holder: {self.account_holder}")   # public
        print(f"💵 Balance (protected): ₹{self._balance}")    # protected access allowed
        # print(self.__pin)  ❌ Not accessible — private

        # Access private using a public wrapper
        self.access_private()

        # Access protected method
        self._calculate_interest()

        print("📘 All accessible from derived class.")


# 🧪 Creating objects
acc1 = BankAccount("Aqsa Shah", 5000, 1234)
savings = SavingsAccount("Aqsa Shah", 10000, 5678)

# 🎬 Access from outside class
print("🔹 Public Access from Outside:")
print(acc1.account_holder)      # ✅ Works (public)

print("\n🔹 Protected Access from Outside:")
print(acc1._balance)            # ⚠️ Works but not recommended (protected)

print("\n🔹 Private Access from Outside:")
# print(acc1.__pin)             # ❌ AttributeError
print(acc1._BankAccount__pin)   # ✅ Name mangling trick (not recommended)

print("\n🔹 Accessing Methods:")
acc1.deposit(2000)              # ✅ Public
# acc1._calculate_interest()    # ⚠️ Works but not recommended
acc1.access_private()            # ✅ Safely calls private method

print("\n🔹 Accessing from Derived Class:")
savings.show_details()
