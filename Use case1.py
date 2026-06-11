def find_largest(numbers):
    largest = numbers[0]

    for i in range(len(numbers)):
        if numbers[i] > largest:
            largest == numbers[i]  # Bug 1

    return largest


nums = []
print(find_largest(nums))  # Bug 2
