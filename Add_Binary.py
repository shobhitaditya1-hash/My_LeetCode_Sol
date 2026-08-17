def binary_to_decimal(num):
    b=0
    numlist = []
    for digit in str(num):
        numlist.append(int(digit))
    for i in range(len(numlist)):
        a = numlist[-i - 1] *(2**i)
        b +=a
    return b

num1 = int(input("Enter a binary number: "))
decimal_value = binary_to_decimal(num1)
print(f"The decimal value of binary {num1} is: {decimal_value}")