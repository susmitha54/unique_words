words=[]
unique_word = []
for i in range(3):
    word = input("Enter a words:")
    words.append(word)
for word in words :
    if word not in unique_word:
        unique_word.append(word)
print(unique_word)