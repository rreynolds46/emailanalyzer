import math
import numpy as np


def get_reading_time(word_count):
    calculation = word_count / 200
    seconds, minutes = math.modf(calculation)
    reading_time = dict()
    reading_time["minutes"] = minutes
    reading_time["seconds"] = int(100*float(np.round((seconds * .60), 2)))
    return reading_time
