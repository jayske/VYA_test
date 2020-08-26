def sum_luhn(total):
    if (total % 10 == 0) and (total > -1):
        return "the number is valid"
    else:
        return "the number is invalid"
    # 371612019985236

def do_luhn(lst):
    sum = 0
    for index in range(len(lst)):
        if (index%2 != 0) and (int(lst[index]) >= 0):
            x2value = int(lst[index]) * 2
            if x2value > 9:
                sum = sum + (x2value%10 + 1)
            else:
                sum = sum + x2value
        elif (int(lst[index]) < 0):
            return -1
        else:
            sum = sum + int(lst[index])
    return sum

def start(input_number):

    input_list = list(input_number)
    input_list.reverse()
    sum = do_luhn(input_list)
    print(sum_luhn(sum))



if __name__ == "__main__":
        input_= str(input('enter your credit card number '))
        start(input_)





    


