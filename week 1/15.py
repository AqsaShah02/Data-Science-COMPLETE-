# Q15. Create a program to print the Fibonacci series up to N terms.

n = int (input("enter a number (n)"))
a,b = 0,1
print ("fibonacci series are:", end =" ")
for _ in range (n):
    
    print (a, end =" ")
    a,b = b, a+b