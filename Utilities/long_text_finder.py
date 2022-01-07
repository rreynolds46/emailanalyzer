import syllables


def find_long_sentences(document):
    long_sentences = []
    for item in list(document.sents):
        word_count = len(item)
        for i in item:
            if i.is_punct:
                word_count -= 1
        if word_count >= 17:
            sentence = dict()
            sentence["text"] = item.text
            sentence["index"] = item.start_char
            sentence["length"] = item.end_char - item.start_char
            long_sentences.append(sentence)
    return long_sentences


def find_long_words(document):
    long_words = []
    for token in document:
        if syllables.estimate(token.text) >= 4:
            long_word = dict()
            long_word["text"] = token.text
            long_word["index"] = token.idx
            long_word["length"] = len(token.text)
            long_words.append(long_word)
    return long_words


def get_long_texts(document):
    long_sentences = find_long_sentences(document)
    long_words = find_long_words(document)
    long_texts = dict()
    long_texts["long_sentences"] = long_sentences
    long_texts["long_words"] = long_words
    return long_texts