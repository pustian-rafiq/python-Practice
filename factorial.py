

def factorial(number):

    if number == 1:
        return 1
    else:
        return (number * factorial(number - 1) )


print("the factorial of the number is ", factorial(6) )


