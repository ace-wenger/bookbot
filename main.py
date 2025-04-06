from stats import count_words, count_characters, sort_dict
import sys

if len(sys.argv) <= 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(path):
    with open(path) as f:
        return(f.read())

def main(path = sys.argv[1]):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    book_text = get_book_text(path)
    num_words = count_words(book_text)
    dict_characters = count_characters(book_text)
    sorted_dict = sort_dict(dict_characters)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for i in range(len(sorted_dict)):
        if sorted_dict[i]["char"].isalpha():
            character = sorted_dict[i]["char"]
            char_count = sorted_dict[i]["count"]
            print(f"{character}: {char_count}")
    
    print("============= END ===============")

    

main()
