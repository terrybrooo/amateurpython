# Prime_number_sequence
end = int(input("enter_the_maximum:"))
lst = []
for num in range(2, end):  # first layer for
    if num == 2:
        lst.append(2)
    else:
        for n in range(2, num-1):  # second layer for
            if num % n == 0:
                break  # if reminder = 0, stop second for and back to first for layer
        else:
            lst.append(num)
print(lst)
