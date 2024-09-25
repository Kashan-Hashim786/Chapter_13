from functools import reduce
# map example
list1 = [2,3,4,5,6]

square = lambda x: x*x
print(list(map(square,list1)))


# filter
def odd(n):
    if(n % 2 == 1):
        return True
    return False
onlyOdd= filter(odd,list1)
print(list(onlyOdd))

# REDUCE
def multiply(a,b):
    return a * b

print(reduce(multiply,list1))