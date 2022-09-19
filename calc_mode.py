def calc_mode(num_list):
    count_num = {}
    # for every number in num_list
    for num in num_list:
        if num not in count_num:
            count_num[num] = 1
        else:
            count_num[num] = count_num[num] + 1

    max_value = 0
    max_key = 0
    for key, value in count_num.items():
        if value > max_value:
            max_value = value
            max_key = key

    return max_key


print(calc_mode([1, 1, 1, 1, 2, 2, 2, 12, 12]))
