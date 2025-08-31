a = [1,10,25,32,75,85,100]

if len(a) < 2:
    print("Not Found")
else:
    max_num, second_largest = float("-inf"), float("-inf")
    for num in a:
        if num > max_num:
            second_largest = max_num
            max_num = num
        elif num < max_num and num > second_largest:
            second_largest = num

    if second_largest == float("-inf"):
        print("Not Found")
    else:
        print(second_largest)