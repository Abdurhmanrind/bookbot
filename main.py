import sys
from stats import get_book_word_num
from stats import get_chara_num
from stats import sorting_list
def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
        return file_contents


def main():
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        book = get_book_text(file_path)
        num_words = get_book_word_num(book)
        all_charac = get_chara_num(book)
        sorted_list , list_num = sorting_list(all_charac)
        sorted_list.sort(key=lambda item: item["num"], reverse=True)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for item in sorted_list:
            print(f"{item['char']}: {item['num']}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()