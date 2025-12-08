def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_chars(text):
    num_chars = {}
    for letter in text:
        letter = letter.lower()
        if letter not in num_chars:
            num_chars[letter] = 0
        if letter in num_chars:
            num_chars[letter] += 1
    return num_chars


def sort_on(items):
    return items["num"]


def get_sort_dict(items):
    sorted_list = []
    for char in items:
        sorted_list.append({"char": char, "num": items[char]})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
