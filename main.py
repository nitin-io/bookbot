def get_book_text(path_to_file):
    with open(path_to_file) as f:
       file_content = f.read()
       return file_content

def main():
	path_to_file = 'books/frankenstein.txt'
	file_content = get_book_text(path_to_file)
	print(file_content)

main()
