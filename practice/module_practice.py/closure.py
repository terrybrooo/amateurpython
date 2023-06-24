def outer():
    b = 10
    def inner(x):
        return 5 * x + b
    return inner

b = 2
f = outer()   
print(f(b))