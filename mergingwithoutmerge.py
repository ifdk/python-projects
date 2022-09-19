def my_merge(list1, list2):
    for x in list1:
        list2.append(x)
    list2.sort()
    return list2


print(my_merge(list1=["mango", "bureau", "apple", "mandate"],
               list2=["physics", "physical", "application"]))
