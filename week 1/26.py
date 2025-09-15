# Q26. Convert a decimal number to binary using loops.



num = int(input("enter a decimal number:"))
original = num

if num == 0:
    print("Binary is: 0")
else:
    binary = ""

    while num >0 :
        remainder = num%2
        binary = str(remainder) + binary # adds bigits to the left side 

        num = num//2

print (f"the binary value for {original}is {binary}")