def my_sort(list_to_sort):
    # should return the sorted list

    if len(list_to_sort) > 0:
        list_to_sort.sort()
    else:
        return None
    return list_to_sort


print(my_sort(['mother', 'father', 'brother']))
