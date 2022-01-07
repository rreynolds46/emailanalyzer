import statistics


def calculate_formality(counts):
    context_independent = counts["nouns"] + counts["adjectives"] + counts["prepositions"] + counts["articles"]
    deictic = counts["pronouns"] + counts["verbs"] + counts["adverbs"] + counts["interjections"]
    formality_1 = (context_independent - deictic + 100) / 2
    formality_2 = 50*(((context_independent - deictic) / (context_independent + deictic)) + 1)
    return statistics.mean([formality_1, formality_2])