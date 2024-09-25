def info():
    name = input("Enter your name : ")
    marks = int(input("Enter your marks : "))
    phone = input("Enter your phone number : ")

    a = "The name of the student is {}, his marks are {} and his phone number is {}".format(name,marks,phone)
    return a
print(info())