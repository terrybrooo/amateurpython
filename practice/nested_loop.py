#乘法表
x,y = eval(input("please_enter_a_range:"))
for i in range(x,y,1):
    for j in range(x,y,1):
        result=i*j
        print(f"{j}x{i}={result:<3d}",end=" ")
    print()