def sum_odd_even(numbers):
    sum_odd = 0
    sum_even = 0
    for number in numbers:
        if number % 2 == 0:
            sum_even += number
        else:
            sum_odd += number
    print(f"Sum of odd numbers: {sum_odd}")
    print(f"Sum of even numbers: {sum_even}")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_odd_even(numbers)
