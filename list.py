mylist  = [12,15,17,18,19]
number1 = mylist[0]
number2 = mylist[2]
number3 = mylist[4]
print("three number = ",number1, number2, number3)

#如果要直接對應到串列裡的位置，需給予相同的變數
num1,num2,num3,num4,num5 = mylist
print("five numbers = ",num1, num3, num5, num2, num4)

#串列切片 [:]冒號後面數字只印到數字前一位
print(mylist[:5])
print(mylist[0:])
#-n 表示倒數第n比資料
print(mylist[-1])
print(mylist[-3])
print(mylist)

#max()最大值, min()最小值, sum()總和, len()串列元素個數
print("maxium = ",max(mylist))
print("minium = ",min(mylist))
print("average = ",sum(mylist)/len(mylist))

#更改串列內容 list[要更改的位置]= 更改成多少
mylist[2]=50
print(mylist[2])

#串列相加
mylist1 = [23,31,52]
print(mylist+mylist1)

#串列乘上數字
newlist = mylist * 3
print(newlist)

#串列加法
print(mylist1[0]+mylist1[2])

#刪除串列元素 (無法保留原本刪除的資料)
lst =[12,56,37,'apple','banana']
del lst[3]
print(lst)

#建立空串列
listt=[]
if len(listt)==0:
    print('已刪除空串列')

#刪除串列
info = [12,'weight',34,'age']
del info

#更改字串元素更改字串元素代碼 (加在字串後面)
sentance = 'i need to cheer up'
print(sentance)
print((sentance.upper()))      #此處也可先定義sen1=sentance.upper()

print("/%s/" % sentance)       #較老舊的輸出手法類似 format()   
print("/{}/".format(sentance))
print(f"/{sentance}/")

# dir() 可用來查詢所有適用於串列,字串的方法
print(dir(sentance))

##串列部分6-4後還未閱讀練習 (p6-20~6-48)

