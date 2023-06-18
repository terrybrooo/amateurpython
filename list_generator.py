#list generator (整合for+if+list)
maxx = int(input("please_enter_a_number:"))
x = [[a,b,c] for a in range(1,maxx) for b in range(1,maxx) for c in range(1,maxx)
     if a**2 + b**2 == c**2 and a<b]        # 需要加入and 條件來排除重複出現的組合
print(f"all posssible of Pythagorean triple combination which lenght under {maxx}")
print(x)
