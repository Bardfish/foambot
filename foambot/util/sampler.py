import os
import random

SAMPLES_DIR = os.path.abspath("./../samples")


def get_random_sample(cog, category):
    return SAMPLES_DIR + "/%s/%s/" % (cog, category) + random.choice(os.listdir(SAMPLES_DIR + "/%s/%s" % (cog, category)))
