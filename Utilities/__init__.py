from .part_of_speech import *
from .formality import *
from .search_values import *
from .readability import *
from .toneanalyzer import *
from .reading_time import *
from .i_vs_you_ratio import *
from .long_text_finder import get_long_texts
from .html_parser import *
from .tokenize_text import *
from .subject_analyzer import subject_analyzer


def get_subject_statistics(html):
    text = get_text_from_html(html)
    document = prepare_text(text)
    subject_statistics = subject_analyzer(text, document)
    return subject_statistics


def get_body_statistics(html):
    text = get_text_from_html(html)
    document = prepare_text(text)
    parts_of_speech = get_pos(document)
    formality_data = calculate_formality(parts_of_speech["counts"])
    hedge_list = get_other_values(0, text)
    weasel_list = get_other_values(1, text)
    spam_list = get_other_values(2, text)
    readability_statistics = get_readability_statistics(document)
    #tone_analysis = get_tone_analysis(text)
    reading_time_data = get_reading_time(parts_of_speech["counts"]["words"])
    i_you_ratio = get_i_you_ratio(parts_of_speech["tokens"])
    long_text = get_long_texts(document)
    email_body_statistics = {
        "parts_of_speech": parts_of_speech,
        "formality": formality_data,
        "hedges": hedge_list,
        "weasels": weasel_list,
        "spam": spam_list,
        "readability_statistics": readability_statistics,
        #"tone_analysis": tone_analysis,
        "reading_time": reading_time_data,
        "i_you_ratio": i_you_ratio,
        "long_text": long_text
    }
    return email_body_statistics
