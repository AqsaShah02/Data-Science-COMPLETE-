
# Q10. Check if a number is a palindrome

num = input("enter a number")
r_num = num[::-1]

if num == r_num:
    print(f"{num} is a palindrome ")
else:
    print(f"{num} is a not palindrome ")