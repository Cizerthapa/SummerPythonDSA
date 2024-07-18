def divisible_by_2_and_3(lst):
    result = [x for x in lst if x % 2 == 0 and x % 3 == 0]
    print(result)

a = [2, 3, 6, 8, 9, 12, 15, 18, 24, 22, 33, 112]
divisible_by_2_and_3(a)
    