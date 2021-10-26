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