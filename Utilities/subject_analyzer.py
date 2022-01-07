import re, string


def get_subject_length(text):
    word_count = 0
    for token in text:
        if token.pos_ not in ["PUNCT", "SPACE"]:
            word_count += 1
    return word_count


def get_if_title_case(text):
    return text.istitle()


def get_if_digit(text):
    return any(char.isdigit() for char in text)


def get_if_punctuation(text):
    regex = re.compile('[.,!?]')
    punctuation = regex.search(text)
    if punctuation:
        return True
    else:
        return False


def subject_analyzer(text, document):
    length_check = get_subject_length(document)
    title_case_check = get_if_title_case(text)
    digit_check = get_if_digit(text)
    punctuation_check = get_if_punctuation(text)
    subject_analysis = dict()
    subject_analysis["length_check"] = length_check
    subject_analysis["title_case_check"] = title_case_check
    subject_analysis["digit_check"] = digit_check
    subject_analysis["punctuation_check"] = punctuation_check
    return subject_analysis
