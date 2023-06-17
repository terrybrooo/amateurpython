# for "可被重複代入的元素" in "可迭代物件(iterable object)"
number  =   [1,2,3,4,5,6,7,8,9]
for num in number:
    print(num)
#可把程式併成一行(不推薦)

for num in number[:4]:print(num) 

#for + if 的應用
random =[29,55,73,24,15,58,49]
for nm in random:
    if int(nm)>50:
        print(nm)
    elif int(nm)>30:
        print(">30")
    else:
        print("<30")

'''
#range()製造等差級數列 range(start, stop[唯一一個對要存在的變數], step)
n = int(input("please_enter_a_number:"))
for n1 in range(n):
    print("*"*n1)
    print("@"*n1,end="")              #print 默認值是換行 因此輸入end=""則表示不換行連續印出 若""內加入元素則是以元素作為空格
'''

'''
#練習印出每年複利
money = 10000
rate =0.018
n = int(input("please_enter_your_deposit_year:"))
for i in range(n):
    mon= money*((1+rate)**i)  #可以直接在這行宣告一個新變數
    print(f"{i+1} year, money becomes {mon:5.2f}")       
'''

#range()
for i in range(-10,10,4):
    print(i)

for i in range(-10,10,2):
    print(i,end=" @ ")
print("")

#range 
n = int(input("enter a number:"))
total = sum(range(n+1))         #在n-1位時停止
print(f"the sum from 1 to {n} is {total}")

#range + list
mylist = []
start,stop,step = eval(input("please_enter_three_number:"))
for li in range(start,1+stop,step):
    mylist.append(li)
print(mylist)

# 新串列 =[運算式 for 項目 in 可迭代物件]
xlist =[n**2 for n in range(4)]
print(xlist)

