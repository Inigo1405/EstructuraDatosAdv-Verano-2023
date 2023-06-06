def factorial(x):
    if x == 0:
        return 1
    
    else: 
        return x * factorial(x-1) 

print(factorial(100))


def factorial_cool(x):
    return 1 if x == 0 else x * factorial(x-1)

print(factorial_cool(100))