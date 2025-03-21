import sys
from stats import get_num_words, count_characters, sort_character_dict

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    print("----------- Word Count ----------")
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_counts = count_characters(text)
    sorted_chars = sort_character_dict(char_counts)

    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['count']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
