# Q30. Write a program to display the cube of the number up to an integer.

num = int(input ("enter a number to obtain a cube "))

if num < 0 :
    print("please enter a number greater than or equal to zero")

else:
    for i in range (1, num + 1):
        cube = i ** 3
        print(f"the cube upto {num} is {cube}")
    
       