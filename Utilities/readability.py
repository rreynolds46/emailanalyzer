import textdescriptives as td


def get_readability_statistics(document):
    readability_statistics = dict()
    readability_statistics["readability"] = document._.readability
    readability_statistics["word_length"] = document._.token_length
    readability_statistics["sentence_length"] = document._.sentence_length
    readability_statistics["syllables"] = document._.syllables

    return readability_statistics