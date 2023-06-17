# Unary_Quadratic_Simultaneous_Equations
print("一元二次方程式計算機")
print("ax^2+bx+c=0")
a,b,c=eval(input("請輸入a,b,c三個變數:"))
result1=(-b+(b**2-4*a*c)**0.5)/(2*a)
result2=(-b-(b**2-4*a*c)**0.5)/(2*a)
print(f"{result1:5.2f}與{result2:5.2f}為一元二次方程式解")