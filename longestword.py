#Write a Python program to find the longest word in a sentence.
sentence = input("enter a sentence: ")
words = sentence.split()
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print(f"The longest word in the sentence is: {longest_word}")
