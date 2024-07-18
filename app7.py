def combine_alternating(lst1, lst2):
    combined_list = [item for pair in zip(lst1, lst2) for item in pair]
    print(combined_list)

lst1 = ['a', 'b', 'c']
lst2 = [1, 2, 3]
combine_alternating(lst1, lst2)
