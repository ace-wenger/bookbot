def count_words(text):
    list_words = text.split()
    return(len(list_words))

def count_characters(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict["count"]

def sort_dict(char_dict):
    char_dict_list = []
    for char in char_dict:
        char_dict_list.append({"char": char, "count": char_dict[char]})

    char_dict_list.sort(reverse = True, key = sort_on)
    return char_dict_list