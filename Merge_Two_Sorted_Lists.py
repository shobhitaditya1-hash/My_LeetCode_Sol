n = int(input("Enter the number of elements in the first sorted list: "))
list1 = []
for i in range(n):
    element = int(input(f"Enter element {i + 1} for the first sorted list: "))
    list1.append(element)

m = int(input("Enter the number of elements in the second sorted list: "))
list2 = []
for i in range(m):
    element = int(input(f"Enter element {i + 1} for the second sorted list: "))
    list2.append(element)
list3 = list1 + list2
list3.sort()
print("The merged sorted list is:", list3)
