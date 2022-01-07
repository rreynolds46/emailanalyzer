import numpy as np


def get_i_you_ratio(tokens):
    i_count = 0
    you_count = 0
    for token in tokens:
        if token["text"] in ["I", "i", "We", "we", "Our", "our", "my", "My", "myself", "Myself", "me", "Me"]:
            i_count += 1
        if token["text"] in ["you", "yourself", "You", "You"]:
            you_count += 1
    i_you_counts = dict()
    i_you_counts["i_count"] = i_count
    i_you_counts["you_count"] = you_count
    if you_count == 0:
        i_you_counts["ratio"] = 1
    else:
        i_you_counts["ratio"] = (100*float(np.round((i_count / (i_count + you_count)), 2)))
    return i_you_counts
