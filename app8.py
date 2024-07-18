def element_wise_addition(lst1, lst2):
    sum_list = [a + b for a, b in zip(lst1, lst2)]
    print(sum_list)

lst1 = [1, 2, 3, 4, 5, 6]
lst2 = [1, 2, 3, 4, 5, 6]
element_wise_addition(lst1, lst2)
