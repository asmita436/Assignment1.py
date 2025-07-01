def find_max(numbers):
    if not numbers:
        return "The list is empty."
    
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

num_list = [12, 45, 7, 89, 23]
print("Maximum value:", find_max(num_list))
