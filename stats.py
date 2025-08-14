def get_num_words(content):
    words_array = content.split()
    return len(words_array)


def get_num_chars(content):
    times = {}
    for c in content:
        if c.lower() in times:
            times[c.lower()] += 1
        else:
            times[c.lower()] = 1
    return times


def sort_on(d):
    return d["num"]


def sorted_dict(times):
    sorted_list = []
    for t in times:
        sorted_list.append({"char": t, "num": times[t]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
