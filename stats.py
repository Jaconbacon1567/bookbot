def get_words(text):
    return len(text.split())

def count_characters(text):
    chars = {}
    new_text = text.lower()
    for char in new_text:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars

def sort_on(d):
    return d["num"]

def order_characters(char_dict):
    sorted_list = []
    for ch in char_dict:
        sorted_list.append({"char": ch, "num": char_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list    