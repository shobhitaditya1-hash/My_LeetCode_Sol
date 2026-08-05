list1 = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    element = int(input(f"Enter element {i + 1} for the list: "))
    list1.append(element)
count =0
element_to_remove = int(input("Enter the element to remove from the list: "))
if element_to_remove not in list1:
    print("The element is not present in the list.")
else:
    continue_removal = input("The element is present in the list. Do you want to remove it? (yes/no): ")
    if continue_removal.lower() == "no":
        print("The element will not be removed from the list.")
    else:
        for k in range(len(list1)):
            if list1[k] == element_to_remove:
                count = count + 1
                list1[k] = "_"
    list1 = [x for x in list1 if x != "_"]
    for j in range(count):
        list1.append("_")
print("The list after removing the element is:", list1)
print(count, "occurrences of the element", element_to_remove, "were removed from the list.")