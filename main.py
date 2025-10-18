
#print("greetings boots")
import sys

from stats import num_words, count_characters, sort_char

#dir = "books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents

def get_path():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    return path

def main():

    dir = get_path()
    text = get_book_text(dir)

    n = num_words(text)
    
    count = sort_char(count_characters(text))
    
    #print(count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {dir}...")
    print("----------- Word Count ----------")
    print(f"Found {n} total words")
    print("--------- Character Count -------")
    for i in count:
        print(f"{i["character"]}: {i["num"]}")
    print("============= END ===============")

main()

