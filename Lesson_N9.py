"""
x = int(input())
y = int(input())
res = x / y
print(res)

a = int(input())
b = int(input())
try:
    res = a / b
except ZeroDivisionError:
    print("Դուք գրել էք 0")
    res = 0
print(res)
"""

try:
    a = int(input())
except ValueError:
    print("Սխալ արժեք")
else:
    print("Ճիշտ է")
    a = 0
try:
    y = int(input())
except ValueError:
    print("Սխալ արժեք")
finally:
    print("Կատարված")
    y = 0
try:
    res = a / y
except ZeroDivisionError:
    print("Զրոյական արժեք")
    res = 0
    res = 0
print  (res)