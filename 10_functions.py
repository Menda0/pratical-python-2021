
# functions
def sayHelloWorld(name, age):
    print(f"hello world Name:{name} Age:{age}")

# TypeError: sayHelloWorld() takes 2 positional arguments but 3 were given
# sayHelloWorld("Marco", 31, 1.75)
sayHelloWorld("Sandra", 24)
sayHelloWorld("Diogo", 78)
#TypeError: sayHelloWorld() missing 2 required positional arguments: 'name' and 'age'
# sayHelloWorld()

def isPair(num):
    if num % 2 == 0:
        return True
    else:
        return False

def example1():
    print("Begin of function")
    return 
    # Never will be executed because is after the return statement
    print("After return function")

print("isPair(5) =", isPair(5))
print("isPair(20) =", isPair(20))

is8Pair = isPair(8)
print("is8Pair =", is8Pair)

def getPerimeterOfCircle(radius):
    # perimeter = 2*pi*radius
    # pi = 3.14
    pi = 3.14
    perimeter = 2*pi*radius
    return perimeter

print("getPerimeterOfCircle(4) =", getPerimeterOfCircle(4))

def getAreaOfCircle(radius):
    # pi*r^2
    pi = 3.14
    return pi * (radius*radius)

def getCircleAreaPerimeter(radius):
    perimeter = getPerimeterOfCircle(radius)
    area = getAreaOfCircle(radius)

    return (area, perimeter)

print("getCircleAreaPerimeter(10) =",getCircleAreaPerimeter(10))

perimeterAreaOf20 = getCircleAreaPerimeter(20)
print("perimeterAreaOf20", perimeterAreaOf20)
print("type(perimeterAreaOf20) =", type(perimeterAreaOf20))

people = [
    {
        "name": "marco",
        "age": 31
    },
    {
        "name": "jose",
        "age": 42
    },
    {
        "name":"ana",
        "age": 29
    }
]

# SUM(AGE) / Total
# Total = len(people)

def averageAge(listOfPersons):
    sum = 0
    for person in listOfPersons:
        age = person["age"]
        sum = sum + age

    total = len(listOfPersons)

    average = sum / total

    return average

print("averageAge(people) =",averageAge(people))

# Recursive functions

# 1! = 1
# 0! = 1
# 2! = 2*1 = 2
# 3! = 3*2*1 = 6
# 4! = 4*3*2*1 = 24

# 1! = 1
# 0! = 1
# 2! = 2 * 1!
# 3! = 3 * 2!
# 4! = 4 * 3!
# n! = n * (n-1)!

# Iterative function
def fact(number):
    if number == 0 or number == 1:
        return 1
    else:
        count = number
        result = 1
        while count > 1:
            result = count * result
            count = count - 1
        return result

# n! = n * (n-1)!
# Recursive function
def fact(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * fact(number-1)

print("fact(1) =", fact(1))
print("fact(2) =", fact(2))
print("fact(3) =", fact(3))
print("fact(4) =", fact(4))