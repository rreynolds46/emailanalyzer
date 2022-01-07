import spacy

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("textdescriptives")
nlp.add_pipe("sentencizer")


def prepare_text(text):
    doc = nlp(text)
    return doc