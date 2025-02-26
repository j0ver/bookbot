from stats import word_count, sorted_count
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
       
def main():
    book_location = sys.argv[1]
    book_content = get_book_text(book_location)
    num_words = word_count(book_content)
    character_list = sorted_count(book_content)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_location}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for character_dict in character_list:
        for key, value in character_dict.items():
            if key.isalpha():
                print(f"{key}: {value}")      
    

main()

