def count_words(text):
        word_count = 0
        book_split = text.split()
        for w in book_split:
            word_count += 1
        return word_count


def character_count(text):
    letters = {}
    text = text.lower()
    for l in text:
        if l in letters:
            letters[l] += 1
        else:
            letters[l] = 1
    return letters

def list_counts(counts_dict):
    count_list = []
    for item in counts_dict:
        temp_dict = {"char": item, "num":counts_dict[item]}
        count_list.append(temp_dict)

    def sort_dicts(item):
        return item["num"]

    count_list.sort(reverse=True, key=sort_dicts)
    return count_list

