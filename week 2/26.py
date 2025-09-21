# 26. Create a function to rotate a list left by k positions.
def rotate_lst (lst,k):
    k  = k% len(lst)
    return lst[k:]+lst[:k]

print(rotate_lst([1,5,6,3,2,4,5,8,9,6,2,],3))