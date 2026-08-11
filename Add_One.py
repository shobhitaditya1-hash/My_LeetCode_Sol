list1 = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    element = int(input(f"Enter element {i + 1} for the list: "))
    list1.append(element)
print(list1)
new_num = list1[-1] + 1
list1.pop()
list1.append(new_num)
print(list1)