sentence = input("Enter a sentence: ")
words = sentence.split()
if words:
    last_word = words[-1]
    print("The length of the last word is:", len(last_word))
else:
    print("The sentence is empty.")