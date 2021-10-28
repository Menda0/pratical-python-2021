'''
    1. Create a list of people with 6 people
    2. Iterate over the list of people create a new list with the people over 18 years old
    3. Iterate over the list of people create a 3 list with the short people, average people and tall people
    4. Print all the list
'''

people =[
    {
        "name": "Henrique",
        "size": 1.72,
        "age": 33
    },
    {
        "name": "Joao",
        "size": 1.2,
        "age": 15
    },
    {
        "name": "Marco",
        "size": 1.75,
        "age": 31
    },
    {
        "name": "Pedro",
        "size": 2.20,
        "age": 36
    },
    {
        "name": "Anibla",
        "size": 2.10,
        "age": 35
    },
    {
        "name": "Zulmiro",
        "size": 1.10,
        "age": 10
    }
]

adults = []
tall_people = []
average_people = []
short_people = []

#vamos iterar sobre a lista de people
for person in people:

    #Validação dos maiores de idade
    if person["age"] >= 18:
        adults.append(person)

    #validação das pessoas muito altas
    if person["size"] >= 2.0:
        tall_people.append(person)
    #validação das pessoas de estatura média
    elif person["size"] >= 1.60 and person["size"] < 2.0:
        average_people.append(person)
    #validação de "escape" todas as abaixo de 1.60, pessoas mais baixas
    else:
        short_people.append(person)

print("###### List of Adults (size > 18) ######")
#print(adults)
for adult in adults:
    print (f"Name: {adult['name']}")
    print (f"Age: {adult['age']}")
    print (f"Size: {adult['size']}")
    print ("")

print("")
print("###### List of Tall People (size > 2.0) ######")
#print(tall_people)
for tall_person in tall_people:
    print (f"Name: {tall_person['name']}")
    print (f"Age: {tall_person['age']}")
    print (f"Size: {tall_person['size']}")
    print ("")

print("")
print("###### List of Average People (1.6 <= size < 2.0) ######")
#print(average_people)
for average_person in average_people:
    print (f"Name: {average_person['name']}")
    print (f"Age: {average_person['age']}")
    print (f"Size: {average_person['size']}")
    print ("")
print("")
print("###### List of Short People < 1.6 ######")
#print(short_people)
for short_person in short_people:
    print (f"Name: {short_person['name']}")
    print (f"Age: {short_person['age']}")
    print (f"Size: {short_person['size']}")
    print ("")
