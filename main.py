def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    word_count = get_word_count(text)
    chars_dict = get_char_count(text)
    # print(sort_on(chars_dict))
    # letters_dict = get_letters_sorted(chars_dict)
    # get_report(book_path, word_count, letters_dict)
    dict_list = make_dictionary(chars_dict)
    get_report(book_path, word_count, dict_list)
   
    
        




def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    # print out words to check if it works:
    # print(words)
    # word_count = 0
    # for word in words:
    #     word_count += 1
    # print(f"word_count: {word_count}")
    return len(words)

def get_char_count(text):
    # char_count = 0
    # char_list = []
    chars = {}

    for c in text:
        # char_count += 1
        # char_list.append(char)
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else: 
            chars[lowered] = 1

    return chars

# def sort_on(chars_dict):
#     # list_of_chars = chars_dict["num"]
#     # print(f"sorting try: {list_of_chars}")
#     return chars_dict["num"]


# def get_letters_sorted(chars_dict):

   
        
  

    # print(nums)
    # print(characters)
        

    
    # chars_dict_list = only_letters["num"]
    # return characters, nums

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]

def make_dictionary(chars_dict):
    only_letters = {}
    # letters    = {}
    # nums       = {}
    characters   = []
    nums         = []
    dict_list       = []


    for key in chars_dict:
        # print(f"The {key} character was fount {chars_dict[key]} times")
        if key.isalpha() == True:
            only_letters[key] = chars_dict[key]

    for key in only_letters:
        characters.append(key)
        nums.append(only_letters[key])

        # letters[key] = key
        # nums[num] = only_letters[key]
    

   
    for i in range(len(characters)):
        dict = {}
        dict["character"] = characters[i]
        dict["num"] = nums[i]
        dict_list.append(dict)
        
        
    dict_list.sort(reverse=True, key=sort_on)

    # print(dict_list)
    return dict_list


def get_report(book_path, word_count, dict_list):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    # for key in letters_dict:
    # print(dict_list)
    for dict in dict_list:
        print(f"The character '{dict["character"]}' was found {dict["num"]} times")



    # for i in range(len(char_list)):
    #     letter = char_list[i].lower() 
    #     if letter not in char_dict:
    #         char_dict[letter] = 1
    #     else:
    #         char_dict[letter] += 1
    # print(f"char_count: {char_count}")


    # for key in char_dict:
    #     print(f"{key}: {char_dict[key]}\n")

        
     

    # print(f"char_count: {char_count}\n char_dict: {char_dict}")



main()