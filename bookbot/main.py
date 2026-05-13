import sys
from stats import word_count, letters_in_book, sorted_letters


def get_book_text(path):
	with open(path) as f:
		content = f.read()
		return content

def main():
	if len(sys.argv) < 2:
        	print("Usage: python3 main.py <path_to_book>")
        	sys.exit(1)
	path = sys.argv[1]
	text = get_book_text(path)
	words_counted = word_count(text)
	counts = letters_in_book(text)
	sorted_items = sorted_letters(counts)
	print ("============ BOOKBOT ============")
	print (f"Analyzing book found at {path}")
	print ("----------- Word Count ----------")
	print (f"Found {words_counted} total words")
	print ("--------- Character Count -------")
	for item in sorted_items:
		if item['char'].isalpha():
			print (f"{item['char']}: {item['num']}")
	print ("============= END ===============")
main()
