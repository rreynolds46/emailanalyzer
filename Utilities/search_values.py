from Values import hedges, weasels, spam
import regex


def get_other_values(type, text):
    search_list = [hedges, weasels, spam][type]
    match_list = []
    for item in regex.finditer(r"\L<words>", text, words=search_list):
        match = dict()
        match["text"] = item.group(0)
        match["index"] = item.start(0)
        match["length"] = len(item.group(0))
        match_list.append(match)
    return match_list

