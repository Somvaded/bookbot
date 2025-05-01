import os
from stats import total_words,sort_map
import sys

def main():
	cmd = sys.argv
	if(len(cmd) != 2):
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	
	file= cmd[1]
	filepath = os.path.join(file)
	with open(file) as f:
		contents = f.read()
		num_of_words = total_words(contents)
		sorted_char_count = sort_map(contents)
		print("============ BOOKBOT ============")
		print(f"Analyzing book found at {filepath}...")
		print("----------- Word Count ----------")
		print(f"Found {num_of_words} total words")
		print("--------- Character Count -------")

		for x in sorted_char_count:
			print(f"{x['char']}: {x['num']}")

		print("============= END ===============")

if __name__ == "__main__":
	main()