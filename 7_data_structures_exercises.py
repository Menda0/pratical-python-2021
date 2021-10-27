# 1. Create a list with 5 people names
# 2. Create a tuple with 5 people names

'''
    1. Create 6 variables containing animals
       (Example: Salmon, Eagle, Bear, Fox, Turtle)
    2. Every animal must have the following information
    2.1 Name, Color, Sound
    3. Create 3 variables for animal families
       (Example: Bird, Mamals, Reptiles, Fish)
    4. Print on the screen the 3 family animals
    5. Print on the screen all the animals
    6. Print on the screen 3 equal animals
       (Example: 3 Eagles, 3 Bears, 3 Foxes)
'''

# Diogo
salmon = {
    "name":"Salmon",
    "color":"salmon",
    "sound":"gurrp"
}

eagle = {
    "name":"eagle",
    "color":"brown",
    "sound":"pii"
}

bear = {
    "name":"bear",
    "color":"brown",
    "sound":"uaaah"
}

fox = {
    "name":"fox",
    "color":"orange",
    "sound":"lol"
}

whale = {
    "name":"Whale",
    "color":"Blue",
    "sound":"mmmmmmmm"
}

tiger ={
    "name":"Tiger",
    "color":"Orange",
    "sound":"sneaky"
}


mammals = [tiger,bear,whale,fox]
bird = [eagle]
fish = [salmon]

#animals=[salmon,eagle,bear,fox,whale,tiger]
animals=mammals+bird+fish
print("Animals: ", animals)


bears=[bear]*3
print(bears)

list_bear=[bear,bear,bear]
print(list_bear)