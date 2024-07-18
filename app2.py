def find_max_min(numbers):
    max_number = numbers[0]
    min_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
        if number < min_number:
            min_number = number
    print(f"Maximum number: {max_number}")
    print(f"Minimum number: {min_number}")

numbers = [10, 20, 4, 45, 99]
find_max_min(numbers)
