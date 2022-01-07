def get_pos(document):
    tokens = []
    counts = dict()
    counts["nouns"] = 0
    counts["adjectives"] = 0
    counts["prepositions"] = 0
    counts["articles"] = 0
    counts["pronouns"] = 0
    counts["verbs"] = 0
    counts["adverbs"] = 0
    counts["interjections"] = 0
    counts["words"] = 0
    adverbs = []
    for token in document:
        token_data = dict()
        token_data["text"] = token.text
        token_data["index"] = token.idx
        token_data["type"] = token.pos_
        token_data["length"] = len(token.text)
        tokens.append(token_data)
        if token_data["type"] == "NOUN":
            counts["nouns"] += 1
        elif token_data["type"] == "ADJ":
            counts["adjectives"] += 1
        elif token_data["type"] == "ADP":
            counts["prepositions"] += 1
        elif token_data["text"] in ["a", "an", "the"]:
            counts["articles"] += 1
        elif token_data["type"] == "PRON":
            counts["pronouns"] += 1
        elif token_data["type"] == "VERB":
            counts["verbs"] += 1
        elif token_data["type"] == "ADV":
            adverbs.append({
                "text": token.text,
                "idx": token.idx,
                "length": len(token.text)
            })
            counts["adverbs"] += 1
        elif token_data["type"] == "INTJ":
            counts["interjections"] += 1

        if token_data["type"] not in ["PUNCT", "SPACE"]:
            counts["words"] += 1
    parts_of_speech = dict()
    parts_of_speech["counts"] = counts
    parts_of_speech["tokens"] = tokens
    parts_of_speech["adverbs"] = adverbs
    return parts_of_speech
