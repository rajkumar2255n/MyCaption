num = int(input("Enter the number of number needed in the list:"))
print("Enter the input for the list:")
number = []
result = []
for i in range(num):
    n = int(input(">"))
    number.append(n)
for i in number:
    if i > 0:
        result.append(i)
print(result)
