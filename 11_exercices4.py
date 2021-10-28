'''
    1. Create a function to calculate the area and perimeter of a square
    1.1 P = 4 * L | A = L * L
    2. Create a function to calculate the area of a triangle
    2.1 A = B * H / 2
'''

def perimetroQuadrado(lado):
    return lado*4

def areaPerimetroQuadrado(lado):
    perimetro = perimetroQuadrado(lado)
    area = lado**2
    return (area, perimetro)


def areaPerimetroTrianguloEquilatero(lado):
    perimetro = lado*3
    area = (3 ** 0.5) * lado / 4
    return (area, perimetro)


def areaTriangulo(base, altura):
    return base * altura / 2


lado = (1, 2, 4, 20)

triangulos = ((1, 2), (4, 20))

for l in lado:
    print(f'areaPerimetroQuadrado({l}): {areaPerimetroQuadrado(l)}')
    print(f'areaPerimetroTrianguloEquilatero({l}): {areaPerimetroTrianguloEquilatero(l)}')

for t in triangulos:
    print(f'areaTriangulo({t[0], t[1]}): {areaTriangulo(t[0], t[1])}')

'''
    1. Define a list of values
    1.1 l = [1,2,3,4,5,6,7,8,9,10]
    2. Iterate list l and create a new list with the multiple of 2
    2.1 Multiple of two -> num % 2 == 0
'''

l=[1,2,3,4,5,6,7,8,9,10]

def getMultipleOfTwo(list):
    a =[]
    for number in list:
        if number % 2 == 0:
            a.append(number)
    return a

print(getMultipleOfTwo(l))
print(getMultipleOfTwo(l))