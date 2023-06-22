def interest(interest_type='traveling', subject='Protugal'): #設定預設值 traveling and Protugal
    "showing interest and theme"
    print(f"my interest is {interest_type}")
    print(f"about {interest_type}, {subject} is my favorite!")

interest('playing instrument','guitar') #直接輸入變數值
interest(interest_type='playing instrument',subject='guitar') #呼叫出參數後給予變數
interest(subject='guitar',interest_type='playing instrument') #參數前後對調不影響
interest() #若沒提供新的參數值，則會顯示預設值

#return 就是直接在呼叫出函數的位置出現結果(result)

def substract(x,y):
    result = x-y
    return result   #表示在跑完substract後,會得到result回傳到原本呼叫函數的位置

substract(15,3)