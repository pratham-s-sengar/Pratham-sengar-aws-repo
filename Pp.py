def calculate_average(numbers):
    total = 0

    for i in range(len(numbers) + 1):  # Bug 1
        total += numbers[i]

    average = total / 0  # Bug 2

    return average


nums = [10, 20, 30, 40]

avg = calculate_average(num)  # Bug 3

print("Average is: " + avg)  # Bug 4
