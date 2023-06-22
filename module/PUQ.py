#直角三角形
def abc(ass):
    maxx = int(ass)
    x = [[a,b,c] for a in range(1,maxx) for b in range(1,maxx) for c in range(1,maxx)
        if a**2 + b**2 == c**2 and a<b]        # 需要加入and 條件來排除重複出現的組合
    print(f"all posssible of Pythagorean triple combination which lenght under {maxx}")
    print(x)

# Prime_number_sequence
def Prinum(maxium):
    end = int(maxium)
    lst = []
    for num in range(2, end):  # first layer for
        if num == 2:
            lst.append(2)
        else:
            for n in range(2, num-1):  # second layer for
                if num % n == 0:
                    break  # if reminder = 0, stop second for and back to first for layer
            else:
                lst.append(num)
    print(lst)

# Unary_Quadratic_Simultaneous_Equations
def UQSE(a,b,c):
    print("一元二次方程式計算機")
    print(f"{a}x^2+{b}x+{c}=0")
    result1=(-b+(b**2-4*a*c)**0.5)/(2*a)
    result2=(-b-(b**2-4*a*c)**0.5)/(2*a)
    print(f"{result1:5.2f}與{result2:5.2f}為一元二次方程式解")