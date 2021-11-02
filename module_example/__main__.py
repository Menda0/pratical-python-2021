import sys

from . import fib

num = int(sys.argv[1])

print("type(num) =", type(num))
print("fib() = ",fib(num))

# Execute module
# python3 -m module_example 10