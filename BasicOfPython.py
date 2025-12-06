# 1. Say "Hello, World!" With Python
if __name__ == '__main__':
    print("Hello, World!")

# 2. Python If-Else
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input().strip())
print("Weird" if n % 2 == 1 or 6 <= n <= 20 else "Not Weird")

# 3. Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
print (a+b)
print (a-b)
print (a*b)

# 4. Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
print(a // b)
print(a / b)

# 5. Loops
if __name__ == '__main__':
    n = int(input())
for i in range(n): print(i**2)

# 6. Write a function
def is_leap(year):
    leap = False

    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True

    return lea
year = int(input())

# 7. Print Function
def newFunction(n: int) -> None:
    i: int = 1
    while i <= n:
        print(i, end = "")
        i += 1

if __name__ == '__main__':
    n = int(input())
    newFunction(n)
