from stats import get_book_word_num
def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
        return file_contents


def main():
    book = get_book_text("books/frankenstein.txt")
    num_words = get_book_word_num(book)
    print(f"{num_words} words found in the document")

main()