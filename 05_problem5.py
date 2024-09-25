from functools import reduce
list1 = [4,5,6,7,8,76,5,3214,98]

def maxNum(a,b):
    if a>b:
        return a
    return b

print(reduce(maxNum,list1))