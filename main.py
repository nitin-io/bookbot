from curses.ascii import isalpha
from stats import get_num_words, get_character_counts, get_sorted_list_of_char

def main():
	path_to_file = 'books/frankenstein.txt'
	num_words = get_num_words(path_to_file)
	char_dict = get_character_counts(path_to_file)
	sorted_list = get_sorted_list_of_char(char_dict)
	print("============ BOOKBOT ============")
	print("Analyzing book found at books/frankenstein.txt...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for char in sorted_list:
		if char["char"].isalpha():
			print(f"{char['char']}: {char['num']}")
	print("============= END ===============")
main()
