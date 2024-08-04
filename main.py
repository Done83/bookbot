    # Functions declarations
def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def letter_counter(text):
    lowered_string = text.lower()
    letters_count = {}
    for char in lowered_string:
        if char in letters_count:
            letters_count[char] += 1
        else:
            letters_count[char] = 1
    return letters_count
def print_report(text, num_words):
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{num_words} words found in the document')
    sorted_dict = dict(sorted(text.items()))
    for char in sorted_dict:
        if char.isalpha():
            print(f"The '{char}' character was found {sorted_dict[char]} times")
    print('--- End report ---')

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    count = letter_counter(text)
    print_report(count, num_words)


main()
