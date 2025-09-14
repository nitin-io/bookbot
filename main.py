from stats import get_num_words, get_character_counts, get_sorted_list_of_char
import sys
def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	path_to_file = sys.argv[1]

	num_words = get_num_words(path_to_file)
	char_dict = get_character_counts(path_to_file)
	sorted_list = get_sorted_list_of_char(char_dict)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path_to_file}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for char in sorted_list:
		if char["char"].isalpha():
			print(f"{char['char']}: {char['num']}")
	print("============= END ===============")
main()
