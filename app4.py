def unique_elements(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    print(unique_lst)

lst = [1, 1, 2, 3, 3, 4, 4, 5, 6, 5, 6]
unique_elements(lst)
