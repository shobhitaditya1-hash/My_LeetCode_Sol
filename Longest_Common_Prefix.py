def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    
    for string in strs[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix
list1 =[]
n = int(input("Enter the number of strings: "))
for i in range(n):
    string = input(f"Enter string {i + 1}: ")
    list1.append(string)
result = longestCommonPrefix(list1)
print(f"The longest common prefix is: '{result}'")