# # Q6. Convert temperature from Celsius to Fahrenheit.

# input = float(input("enter temperature in celcsius:"))

# temp = (input*9/5)+32

# print(f"temperaure for {input}c in ferenheit is",temp)

a = int(input("Enter 1 for Celsius to Fahrenheit And Enter 2 for Fahrenheit to Celsius :"))

if a == 1:
    c=float(input("Enter the Temperature in Celsius: "))
    fahrenheit= (c * 9/5)+32
    print("Temperature in Fahrenheit is:", fahrenheit)

elif a == 2:
    f=float(input("Enter the Temperature in Fahrenheit: "))
    celsius= (5/9)*(f-32)
    print("Temperature in Celsius is:", celsius)

else:
    print("Entered number is not in a range between 1 and 2")