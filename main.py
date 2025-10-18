
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
    try:
        text = get_book_text(dir)
    except FileNotFoundError:
        print("Error: File not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(2)
    
    n = num_words(text)
    c_dict, nc = count_characters(text)

    count = sort_char(c_dict)
    
    #print(count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {dir}...")
    print("----------- Word Count ----------")
    print(f"Found {n} total words")
    print("--------- Character Count -------")
    for i in count:
        p = (i["num"]/nc)*100
        print(f"{i["character"]}: {i["num"]}: {round(p,2)}%" )
    print(f"*: {nc}: 100%")
    print("============= END ===============")

main()

