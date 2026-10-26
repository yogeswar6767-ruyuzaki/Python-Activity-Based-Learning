# program to find Text Compression Using Repeated Characters

word = input("Enter some letters: ")

compressed = ""
count = 1

for i in range(len(word)):
    if i < len(word) - 1 and word[i] == word[i + 1]:
        count = count + 1
    else:
        compressed = compressed + word[i] + str(count)
        count = 1

print("Compressed text:", compressed)