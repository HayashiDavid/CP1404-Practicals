"""Word Occurrences
Estimate: 1 hour
Actual: 35 minutes
"""
def main():
    words_to_count = {}
    lengths = []

    text = input("Text>>> ")
    words_to_count = count_words(text)

def count_words(text):
    words_to_count = {}
    phrases = text.split()

    for text in phrases:
        if text in words_to_count.keys():
            words_to_count[text] += 1
        else:
            words_to_count[text] = 1

    return words_to_count
