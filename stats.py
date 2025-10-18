def num_words(text):
    list_words = text.split()
    nw = len(list_words)
    return nw

def count_characters(text):
    result = {}
    lower_text = text.lower()
    for c in lower_text:
        if not c.isalpha():
            continue
        if (not c in result):
            result[c] = 0
        result[c] += 1
    return result

def sort_on(items):
    return items["num"]

def sort_char(dict):
    ld = []
    for c in dict:
        d = {}
        d["character"] = c 
        d["num"] = dict[c]
        ld.append(d)
    ld.sort(reverse=True, key=sort_on)
    return ld
