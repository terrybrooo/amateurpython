#for continue
score =[12,34,26,37,34,52,24,36]
game  =0
for s in score:
    if s>30:
        game += 1
print(f"{game} games get more than 30 points")

for s in score:
    if s<30:           #如果s小於30"暫時停止執行" game+1 的動作，然後 "繼續"回到for函數測試下一個score
        continue
    game += 1
print(f"{game} games get more than 30 points")

#for else 
#質數數列
end = 10
lst=[]
for num in range(2,end):
    if num ==2:
        print("2",end=",")
    else:
        for n in range(2,num-1):
            if num % n == 0:
                break
        else:
            print(f"{num}",end=",")
print()

# while  相較於for自動重複性執行 while 需要輸入特定條件才會停止 while 裡面的程式內容
#guess lucky number
'''
answer = 754
guess = 0
while guess != answer:
        guess = int(input("Please guess a number between 1~1000, \nif you want to quit the game please enter 'quit'):"))
if guess > answer:
        print(f"please guess a number below {guess}")
elif guess < answer:
        print(f"please guess a number larger than {guess}")
else:
    print(f"Congradulation!!! the lucky number is {answer}")
'''


#小於1000的連續加法計算機
m = int(input("please enter a number:"))
sum = 0 # initial vale
while m < 1000: #當m 小於 1000 時 執行while的內容，直到大於1000停止 (sentivel value)
    sum += m
    m = int(input("add with:"))
print(f"Sum is {sum}")


#利用for 跟 while 寫出相同結果
tuition = 50000
year = 0
while tuition < 60000: # 用while寫較簡潔 當tuition<60000時，持續跑內容直到大於或等於60000
    tuition = tuition * 1.05
    year += 1
print(f"after {year} years, the tuition fee is more than 60000")

tuition1 = 50000
for x in range(10): #用for寫太複雜 變成是用嘗試的還須設範圍跟停止條件 while自帶停止條件較方便
    total = tuition1*((1.05)**x)
    if total > 60000:
        print(f"after {x} years, the tuition fee is more than 60000")
        break

