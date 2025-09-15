# 10. Create a dictionary of squares of numbers from 1 to 10.


squares={}

for i in range(1,11):
    squares[i] = i**2 # key = i, value = i squared

print(squares)
