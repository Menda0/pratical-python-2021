from module_example import fib
from module_example import Car

print("fib(10) =",fib(10))

diogo_car = Car("Tesla", "X", "batery")

print("diogo_car =", diogo_car)

import requests

response = requests.get("https://dog-api.kinduff.com/api/facts?number=10")
dogs = response.json()

print(dogs)

for f in dogs["facts"]:
    print(f)