number1 = 2
number2 = 3

number3 = number1 + number2

print("number3 =", number3)
print("type(number3) =", type(number3))

number4 = number1 * number2

print("number4 =", number4)
print("type(number4) =", type(number4))

number5 = number1 - number2

print("number5 =", number5)
print("type(number5) =", type(number5))

number6 = number2 / number1
print("number6 =", number6)
print("type(number6) =", type(number6))

number7 = 8 % 2
number8 = 8 % 3
print("number7 =", number7)
print("number8 =", number8)

string1 = "Hello world"
string2 = "Marco Mendao"

string3 = string1 + " " + string2

print("string3 =", string3)

# TypeError: unsupported operand type(s) for -: 'str' and 'str'
# string4 = string1 - string2


# Logica booleana
verdadeiro = True
falso = False

boolean1 = verdadeiro & falso
print("boolean1 =", boolean1)

boolean2 = verdadeiro | falso
print("boolean2 =", boolean2)

number1 = 2
number2 = 3

result1 = number1 > number2
print("result1 =", result1)

result2 = number1 <= number1
print("result2 =", result2)

# TypeError: can only concatenate str (not "int") to str
# result3 = "Hello world " + 10

string1 = "Hello world "
number1 = 10

result3 = string1 + str(number1)

print("result3 =", result3)

string1 = "10000"
string2 = "20000"

result4 = int(string1) + int(string2)

print("result4 =", result4)
print("type(result4) =", type(result4))