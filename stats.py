def sort_on(char):
	return char["num"]

def get_book_text(path_to_file):
    with open(path_to_file) as f:
       file_content = f.read()
       return file_content

def get_num_words(path_to_file):
	text = get_book_text(path_to_file)
	words = text.split()
	return len(words)

def get_character_counts(path_to_file):
	text = get_book_text(path_to_file)
	characters = text.lower()
	counts = {}
	for char in characters:
		if char not in counts:
			counts[char] = 0
		counts[char] += 1
	return counts

def get_sorted_list_of_char(characters):
	new_list = []
	for char in characters:
		new_list.append({"char": char, "num": characters[char]})
	new_list.sort(reverse=True, key=sort_on)
	return new_list
