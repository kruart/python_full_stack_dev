import itertools
from nltk import pos_tag


def flatten_list(_list):
    """ [(1,2), (3,4)] -> [1, 2, 3, 4]"""
    return list(itertools.chain.from_iterable(_list))


def is_verb(word):
    """Checks if the word is verb"""
    if not word:
        return False
    pos_info = pos_tag([word])
    return pos_info[0][1] == 'VB'