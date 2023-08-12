list1 = []
list2 = []

l1 = int(input("Enter number of element needed in list1 :"))
l2 = int(input("Enter number of element needed in list1 :"))

print("Enter value for set 1:")
for i in range(l1):
    num = int(input(">"))
    list1.append(num)

print("Enter value for set 2:")

for i in range(l2):
    num = int(input(">"))
    list2.append(num)

set_E = set(list1)
set_N = set(list2)

# Perform set operations
union_result = set_E.union(set_N)
intersection_result = set_E.intersection(set_N)
difference_result = set_E.difference(set_N)
symmetric_difference_result = set_E.symmetric_difference(set_N)

# Print the results
print(f"Union of E and N is {union_result}")
print(f"Intersection of E and N is {intersection_result}")
print(f"Difference of E and N is {difference_result}")
print(f"Symmetric difference of E and N is {symmetric_difference_result}")
