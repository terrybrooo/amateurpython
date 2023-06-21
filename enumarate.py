# enumarate
lst = [12, 'apple', 'james']
enm = enumerate(lst)
print(enm)  # 以enumarate物件輸出
print(list(enm))  # 以串列方式輸出 並加上數字索引
for count, place in enumerate(lst):
    print(place)
