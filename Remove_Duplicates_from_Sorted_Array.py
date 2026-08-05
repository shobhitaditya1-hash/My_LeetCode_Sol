list1 = []
n = int(input("Enter the number of elements in the sorted list: "))
for i in range(n):
    element = int(input(f"Enter element {i + 1} for the sorted list: "))
    list1.append(element)
for i in range(1, len(list1)):
    if list1[i] == list1[i - 1]:
        list1[i] = None
print("The sorted list with duplicates removed is:", [x for x in list1 if x is not None])