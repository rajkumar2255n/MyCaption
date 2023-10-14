def print_positive_numbers(input_list):
    positive_numbers = [num for num in input_list if num > 0]
    return positive_numbers

# Example usage
list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]

output1 = print_positive_numbers(list1)
output2 = print_positive_numbers(list2)

print(f"Input: list1 = {list1}  Output: {output1}")
print(f"Input: list2 = {list2}  Output: {output2}")
