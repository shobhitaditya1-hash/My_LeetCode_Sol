list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
        for k in range(j + 1, len(list1)):
            if list1[i] + list1[j] == 7:
                print(f"Triplet found: ({list1[i]}, {list1[j]})")