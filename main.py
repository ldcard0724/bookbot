from stats import count_words
from stats import count_characters
from stats import sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents

working_book = ""

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        working_book = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {working_book}...")
        print("----------- Word Count ----------")
        print(f"Found {count_words(get_book_text(working_book))} total words")
        print("--------- Character Count -------")
        for item in sort_dict(count_characters(get_book_text(working_book))):
            print(f"{item["char"]}: {item["num"]}")


main()