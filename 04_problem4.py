def divisibleBY5(n):
    if n%5 == 0:
        return True
    return False

list1 = [11,15,25,56,76,78,90]
print(list(filter(divisibleBY5,list1)))