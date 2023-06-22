# Unary_Quadratic_Simultaneous_Equations
def UQSE(a,b,c):
    print("一元二次方程式計算機")
    print(f"{a}x^2+{b}x+{c}=0")
    result1=(-b+(b**2-4*a*c)**0.5)/(2*a)
    result2=(-b-(b**2-4*a*c)**0.5)/(2*a)
    print(f"{result1:5.2f}與{result2:5.2f}為一元二次方程式解")