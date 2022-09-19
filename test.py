def numbers_divisible(range_start, range_end, divisible_by):
    result = []
    for num in range(range_start, range_end):
        if num % divisible_by[0] == 0 and num % divisible_by[1] == 0:
            result.append(str(num)
                          )

    return ", ".join(result)


x = numbers_divisible(1, 5000, (6, 7))
print(x)
