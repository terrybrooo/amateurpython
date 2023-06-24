# module 內的變數可以list的格式輸入，再以for依序拆解輸入
def product_msg(customers):
    str1 = 'Dear'
    str2 = 'we will hold a products exhibition on October 21 2021'
    str3 = 'Sincerely,'  #先宣告字串
    for customer in customers:  #customer 從 module 的 customers 取出變數，此處得變數位置是members list，可以套入for
        msg = str1 + customer + '\n' + str2 + '\n' + str3
        print(msg, '\n')

members = ['Terry', 'Lulu', 'Debra']
product_msg(members)
