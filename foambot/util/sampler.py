import os
import random

SAMPLES_DIR = os.path.abspath("./../samples")


def get_random_sample(cog, category):
    files = list(filter(lambda x: 'mp3 in x', os.listdir(SAMPLES_DIR + "/%s/%s" % (cog, category))))
    return SAMPLES_DIR + "/%s/%s/" % (cog, category) + random.choice(files)
