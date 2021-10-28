# IF Statement

# if condition
# then logic
# else logic

marco = {
    "name": "Marco",
    "age": 31 ,
    "size": 1.75
}

rui = {
    "name": "Rui",
    "age": 15,
    "size": 1.20
}

person = rui

if person["age"] >= 18:
    print(f"{person['name']} is an Adult")
    # print(marco["name"], " is an Adult")
else:
    print(f"{person['name']} is a child")

# se person >= 2 alta
# se person >= 1.6 e person < 2 normal
# se person < 1.6 baixa

if person["size"] >= 2.0:
    print(f"{person['name']} is a tall person")
elif person["size"] >= 1.6 and person["size"] <2.0:
    print(f"{person['name']} is average")
else:
    print(f"{person['name']} is short")


# Make a program that counts to 1-
print("1")
print("2")
print("3")
print("4")
# ...

# do then
# while condition

count = 1

while count <= 10:
    print(count)
    count = count + 1

people = [marco, rui]

# print(marco["name"])
# print(rui["name"])

i = 0
while i < len(people):
    person = people[i]
    print(f"Person is: {person['name']}")
    i = i + 1

# For statement

for person in people:
    print(f"Person age is: {person['age']}")