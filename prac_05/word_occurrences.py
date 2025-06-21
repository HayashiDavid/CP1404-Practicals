"""Word Occurrences
Estimate: 1 hour
Actual: 35 minutes
"""
def main():
    text = input("Text>>> ")
    words_to_count = count_words(text)
    sorted_words = sort_words(words_to_count)
    print_results(words_to_count, sorted_words)

def count_words(text):
    """ Count words and return to dictionary """
    words_to_count = {}
    phrases = text.split()

    for text in phrases:
        if text in words_to_count.keys():
            words_to_count[text] += 1
        else:
            words_to_count[text] = 1

    return words_to_count

def sort_words(words_to_count):
    """ Sort words alphabetically """
    return  sorted(words_to_count.keys())

def find_max_width(sorted_words):
    """ Find the longest word for formatting """
    return max(len(phrases) for phrases in sorted_words)

def print_results(words_to_count, sorted_words):
    """ Print results with aligned formatting """
    max_width = find_max_width(sorted_words)
    for text in sorted_words:
        print(f"{text:{max_width}} : {words_to_count[text]}")

main()