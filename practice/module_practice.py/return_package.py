def multifunvtion(a,b):
    addresult = a+b
    subresult = a-b
    timesresult = a*b
    devideresult = a/b
    return addresult, timesresult, subresult, devideresult #可回傳不只一個值 且回傳值可重複出現已宣告的變數 回傳值順序可任意放
print(multifunvtion(12,3))

result = multifunvtion(12,3)  #return 值會被打包成 tuple，因此可直接定義新的tuple,再用[]呼叫的方式叫出要得值
print(result[1:4])
