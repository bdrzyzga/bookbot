# stats.py

def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    char_dict = {}

    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

# Helper for sorting
def sort_on(dict):
    return dict["count"]

def sort_character_dict(char_dict):
    sorted_list = []

    for char, count in char_dict.items():
        if char.isalpha():  # Skip non-alphabetical
            sorted_list.append({"char": char, "count": count})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
