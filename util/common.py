import re
from nltk.corpus import cmudict


class Color:
    RED = '\033[91m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    END = '\033[0m'

def normalize_quotes(inp: str) -> str:
    return inp.replace('’', "'").replace('“', '"').replace('”', '"')


def remove_phoneme_stress(phonemes: list[str]) -> list[str]:
    """ not neccesary for consideration, see http://www.speech.cs.cmu.edu/cgi-bin/cmudict for more information """
    return [re.sub(r'\d+', '', phoneme) for phoneme in phonemes]


def remove_word_version(word: str) -> str:
    """ remove the version number from the word """
    return re.sub(r'\(\d+\)', '', word)


def get_cmudict() -> tuple[dict[str, list[str]], dict[str, str]]:
    """ load in the CMU Dictionary """
    print(f'{Color.YELLOW}! Loading CMU Dictionary...{Color.END}')

    # get CMU dict from nltk corpus
    cmudict.ensure_loaded()
    raw = cmudict.dict()

    # lookup and reverse lookup dictionaries
    word_to_phoneme = {word: pronunciation[0] for word, pronunciation in raw.items()}  # NOTE: this will overwrite any words with multiple pronunciations
    phoneme_to_word = {str(b): a for a, b in word_to_phoneme.items()}  # reverse dictionary to get words from pronunciations; NOTE: this will overwrite any words with the same pronunciations

    print(f'{Color.YELLOW}! CMU Dictionary loaded!{Color.END}')
    return word_to_phoneme, phoneme_to_word
