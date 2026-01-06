#gets the full word count for the file provided
def word_count(full_text):
    word_split = full_text.split()
    num_words = len(word_split)
    return num_words

#gets the character count for each letter,number or misc character
def count_chars(text):
    counter = 0    
    char_list = {}
    for char in text.lower():
        if char in char_list:
            char_list[char] = char_list[char] + 1
        else:
            char_list[char] = 1
    return char_list

#gets the items out of the dicionary and turns that into a list that is sorted
#based on the helper function
def char_sorter(dictionary):
    dict_items = dictionary.items()
    result = []
    for char, count in dict_items:
        new_dict = {
            "char": char,
            "num": count
        } 
        result.append(new_dict)
    result.sort(reverse=True, key=sort_on)
    return (result)

## helper function to sort on num
def sort_on(item):
    return item["num"]

