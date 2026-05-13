def word_count(text):
        words = text.split()
        total_words = len(words)
        return total_words

def letters_in_book(text):
    lower_string = text.lower()
    letter_counts = {}
    for char in lower_string:
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1
    return letter_counts

def sort_on(letter_counts):
	return letter_counts["num"]

def sorted_letters(letter_counts):
	result = []
	for letter in letter_counts:
		result.append({"char": letter, "num": letter_counts[letter]})
	result.sort(reverse=True, key=sort_on)
	return result
