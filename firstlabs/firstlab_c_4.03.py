def find_longest_word(text):
    words = text.split()
    longest_word = max(words, key=len)
    return longest_word, len(longest_word)


text_length = int(input())
text = input()

longest_word, length = find_longest_word(text)

print(longest_word)
print(length)
