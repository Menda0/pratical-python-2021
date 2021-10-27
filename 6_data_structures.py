number1 = 10
number2 = 20
number3 = 30
number4 = 40

# List start at position 0
# Last element is size of list - 1
list1 = [number1, number2, number3, number4]

print("list1 =", list1)
print("type(list1) =", type(list1))

print("list1[0] =", list1[0])
print("list1[1] =", list1[1])
print("list1[2] =", list1[2])
# IndexError: list index out of range
# print("list1[4] =", list1[4])
print("type(list1[0]) =", type(list1[0]))

list2 = ["marco", "luis", "jose", "rui"]

print("type(list2)", type(list2))
print("type(list[2])", type(list2[2]))

list3 = ["marco", 31, 1.74]
print("type(list3[0])", type(list3[0]))
print("type(list3[1])", type(list3[1]))

list3[0] = "francisco"
print("list3[0]", list3[0])
print("list3 =", list3)

list3[1] = "marco"
print("list3 =", list3)

list1 = [1,2,3,4,5,6,7]
list2 = [8,9,10,11]

list3 = list1 + list2
print("list3 =", list3)

list4 = list2 + list1
print("list4 =", list4)

# TypeError: unsupported operand type(s) for -: 'list' and 'list'
# list5 = list1 - list2

list1 = ["marco"]

list2 = list1 * 3
print("list3 =", list2)

list1 = [1,2,3,4,5,6,7,8]

is_6_in_list = 6 in list1
print("is_6_in_list =", is_6_in_list)

is_12_in_list = 12 in list1
print("is_12_in_list =", is_12_in_list)

list1.append(12)
print("list1 =", list1)

list1.insert(2, 10)
print("list1 =", list1)
# 1, 2, 10, 3, 4, 5, 6, 7, 8, 12

list1.pop()
print("list1 =", list1)

list1.remove(10)
print("list1 =", list1)
# 1,2,3,4,5,6,7,8

list2 = [1,2,2,2,3]
list2.remove(2)

print("list2 =", list2)

list1.reverse()
print("list1 =", list1)

list2 = list1[0:3]
print("list2 =", list2)

list3 = list1[:3]
print("list3 =", list3)

# i >=3 i < 6
list4 = list1[3:6]
print("list4 =",list4)

# list5 = list1[0:2] + list1[3:size-1]
list5 = list1[:2] + list1[3:]
print("list5 = ", list5)

size = len(list1)
print("size list1 =", size)

print("list1[-2] =",list1[-2])

tup1 = ("marco", "sandra", "francisco")
print("tup1 =", tup1)
print("type(tup1) =", type(tup1))

print("tup1[1] =", tup1[1])

# TypeError: 'tuple' object does not support item assignment
# tup1[1] = "Pedro"

tup2 = "marco",
print("type(tup2) =", type(tup2))

# Dict key -> value
dict1 = {"name":"Marco", "age": 31}

print("dict1[name] =", dict1["name"])
print("dict1[age] =", dict1["age"])
print("type(dict1) =", type(dict1))
print("type(dict1[age]) =", type(dict1["age"]))

dict1["name"] = "Henrique"

print("dict1 =", dict1)

del dict1["age"]

print("dict1 =", dict1)

dict1 = {
    "name": "Marco",
    "age": 31,
    "gender": "male"
}

values = list(dict1.values())
print("values =",values)
print("type(values) =", type(values))

keys = list(dict1.keys())
print("keys =", keys)

dict1 = {
    "name": "Pratical Python",
    "formandos":[
        "Marco",
        "Manuel",
        "Luis",
        "Sandra"
    ]
}

print("type(dict1) =", type(dict1))
print("type(dict1[formandos]) =", type(dict1["formandos"]))

formandos1 = dict1["formandos"]
print("formandos1[0] =", formandos1[0])

print("dict1[formandos][0] =", dict1["formandos"][0])

# Pedro, Manuel, Luis, Sandra
formandos1[0] = "Pedro"

print("formandos1 =", formandos1)
print("dict1[formandos] =", dict1["formandos"])

list1 = [
    {
        "name":"Marco",
        "age": 31
    },
    {
        "name": "Pedro",
        "age": 15
    },
    {
        "name": "Filomena",
        "age": 25
    }
]

print("list1[2][age] =",list1[2]["age"])

filomena = list1[2]
print("filomena[name] =", filomena["name"])

filomena["age"] = 26

print("filomena =", filomena)
print("list1 =", list1)

list_of_list = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

# Get value 7
print("list_of_list =", list_of_list[1][2])

dict1 = {
    "name":"Marco",
    "details":{
        "address": "Avenida Sao Francisco Xavier",
        "number": 5
    }
}

print("dict1[details][number] =",dict1["details"]["number"])