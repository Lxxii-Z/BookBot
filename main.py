#Answer
"""def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split
    return len(words)
main()"""
import sys
from stats import count_words
from stats import count_characters
from stats import sorted_data

#Write a new function called get_book_text. 
#It takes a filepath as input and returns the contents of the file as a string.
def get_book_text(path):
    with open(path) as f:
        return f.read()
        
#Write a main function that uses get_book_text with the relative path 
# to your frankenstein.txt file to print the entire contents of the book to the console
def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = count_words(text)
    char = count_characters(text)
    sorted_letters = sorted_data(char)

        # Print the report header
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print each character and its count
    for items in sorted_letters:
        char = items["char"]
        count = items["num"]
        # Only print alphabetical characters
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()

