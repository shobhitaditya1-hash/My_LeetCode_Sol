def Valid_Paranthesis(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack
text = input("Enter a string of parentheses: ")
if Valid_Paranthesis(text):
    print(f"The string '{text}' is valid.")
else:
    print(f"The string '{text}' is not valid.")
    