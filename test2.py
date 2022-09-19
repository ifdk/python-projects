a = [(['a', 'b', 'c', 'd'], ['a', 'f', 'c', 'h']),
     (['o', 'p', 'q', 'r'], ['s', 't', 'q', 'v'])]

eq = [[], []] # to make it clearer

for i in range(0, len(a)):
    first, second = a[i]
    for j in range(0, len(first)):
        fir = first[j]
        sec = second[j]
        equal = fir == sec # wrong operator: = instead of ==
        eq[i].append(equal) # wrong index, should be outer loop counter

print(eq)