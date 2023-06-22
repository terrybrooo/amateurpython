def sub(a,b):
    return a-b

def add(a,b):
    return a+b

def times(a,b):
    return a*b

def devide(a,b):
    return a/b

print("welcome to use basic calculator")
a = int(input("please enter a +-*/ b consequencely:"))
op =str(input())
b =int(input())

if op == '+':
    print(f"{a} {op} {b} = ",add(a,b))
elif op == '-':
    print(f"{a} {op} {b} = ",sub(a,b))
elif op == '*':
    print(f"{a} {op} {b} =",times(a,b))
elif op =='/':
    print(f"{a} {op} {b} =",devide(a,b))
else:
    print("error")

