import re

class C:
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


def get_cmudict():
    """ load in the CMU Dictionary """
    print(f'{C.YELLOW}Loading CMU Dictionary...{C.END}')
    # ref: http://www.speech.cs.cmu.edu/cgi-bin/cmudict
    with open('cmudict-0.7b', 'r') as f:
        raw = f.read()
    uncomment = [definition.split('  ') for definition in raw.split('\n')[:-1] if not definition.startswith(';;;')]
    # NOTE: by some error, some words like "PATHOGENESIS" have 3 spaces instead of 2 between the word and pronunciation
    word_to_phoneme = {word: pronunciation.strip().split(' ') for word, pronunciation in uncomment}
    phoneme_to_word = {str(b): a for a, b in word_to_phoneme.items()}  # reverse dictionary to get words from pronunciations; NOTE: this will overwrite any words with the same pronunciations
    print(f'{C.YELLOW}CMU Dictionary loaded!{C.END}')
    return word_to_phoneme, phoneme_to_word
