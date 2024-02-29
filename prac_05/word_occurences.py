def word_occurrences(text):

    words = text.split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    max_length = max(len(word) for word in word_counts)
    for word, count in sorted(word_counts.items()):
        print(f"{word:{max_length}} : {count}")


"""

Estimate: 30 minutes

"""

text = input("Enter a string: ")
word_occurrences(text)
