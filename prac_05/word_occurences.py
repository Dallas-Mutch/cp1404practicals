"""
Word Occurrences
Estimate: 15 minutes
Actual:   28 minutes
"""

word_to_count = {}
text = input("Text: ")
# text = "Text: this is a collection of words of nice words this is a fun thing it is"
words = text.split()
for word in words:
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1
    # print(frequency)

# sorts the words by alphabetical
words = list(word_to_count.keys())
words.sort()

# counts and displays the reoccurring words
max_length = max((len(word) for word in words))
for word in words:
    print(f"{word:{max_length}} : {word_to_count[word]}")