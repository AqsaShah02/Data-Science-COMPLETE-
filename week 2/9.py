# 9. Write a function to count the frequency of elements in a list.

def count (lst):
    freq={}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] =1
    return freq

num =[1,5,8,3,6,2,5,2,6,2,22,488]        

print ("frequencies: ",count(num))
