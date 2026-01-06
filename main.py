from stats import word_count, count_chars, char_sorter
import sys

#function to read files
def get_book_text(path):
    with open(path) as f:
        return f.read()


#takes every function and calls them to get final data back
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

        
    book_path = sys.argv[1]
    text = get_book_text(book_path)


    num_words = word_count(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f'Found {num_words} total words')
    print("--------- Character Count -------")
    char_counter = count_chars(text)
    #print(char_counter)
    sort_dict = char_sorter(char_counter)
    for items in sort_dict:
        first_key = items['char']
        second_value = items['num']
        print(first_key + ": " + str(second_value))
    #print(sort_dict)
    #print(f'{first_key},{second_value}')
    print("============= END ===============")
    
    

main()