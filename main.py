import string

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_count = get_char_count(text)
    print(f"Word count: {word_count}")
    print("Character counts:")
    for char in sorted(character_count.keys()):
        count = character_count[char]
        print(f"{char}: {count}")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_count = {}
    for char in text.lower():
        if char.isalnum() or char in string.punctuation:
            char_count[char] = char_count.get(char, 0) + 1
    return char_count

main()
