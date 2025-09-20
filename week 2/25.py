# 25. Write a program to find the second highest number in a list.
lst = input("enter numbers seprated by spaces")
text = list(map(int,filter(None, lst.split(" "))))

def second_highest(lst):
    if len(text)<2:
        print("there should be more than two numbers available in the list")
    else:
        first = second = float('-inf')
        for num in text:
            if num>first:
                second = first
                first = num
            elif num>second and num!=first:
                second = num

    return second

print (second_highest(text))

