#可簡單理解為不可改變的串列(list)
#如果要改動tuple則須直接重新定義
trutle =(12,24)
for a in trutle:
    print(a)

trutle = (21,42)   #直接重新定義
for a in trutle:
    print(a)

#用list()或tuple()改變數值型態
key =[12,45,4,6]
newkey = tuple(key)
print(type(newkey))
newwkey = list(newkey)
print(type(newwkey))

#enumarate物件解析後list 內的索引與物件即是 "tuple"

keye = enumerate(key,1)
lss = list(keye)
print(lss)
print(type(lss[2]))