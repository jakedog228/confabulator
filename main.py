from util.ipa import arpabet_to_ipa
from g2p_en import G2p
import re

# nltk.download('averaged_perceptron_tagger_eng')
g2p = G2p()  # g2p directly intelligently words to ARPABET phonemes (not a lookup table)


class C:
    RED = '\033[91m'
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    END = '\033[0m'


def get_cmudict():
    # ref: http://www.speech.cs.cmu.edu/cgi-bin/cmudict
    with open('cmudict-0.7b', 'r') as f:
        raw = f.read()
    uncomment = [definition.split('  ') for definition in raw.split('\n')[:-1] if not definition.startswith(';;;')]
    word_to_phoneme = {word: pronunciation.split(' ') for word, pronunciation in uncomment}
    phoneme_to_word = {str(b): a for a, b in word_to_phoneme.items()}  # reverse dictionary to get words from pronunciations; NOTE: this will overwrite any words with the same pronunciations
    return word_to_phoneme, phoneme_to_word


def get_partner(word, pronunciation, d, d_rev):
    partner = d_rev.get(str(['DH' if syl == 'TH' else syl for syl in pronunciation]), None)
    if partner and partner != word:
        return partner
    return None


# # RUNS TOO SLOW
# def group_partitions(lst):
#     """ RUNS IN O(2^n) TIME
#     list(group_partitions(['a', 'b', 'c', 'd']))
#     [
#         [['a'], ['b'], ['c'], ['d']],
#         [['a'], ['b'], ['c', 'd']],
#         [['a'], ['b', 'c'], ['d']],
#         [['a'], ['b', 'c', 'd']],
#         [['a', 'b'], ['c'], ['d']],
#         [['a', 'b'], ['c', 'd']],
#         [['a', 'b', 'c'], ['d']],
#         [['a', 'b', 'c', 'd']]
#     ]
#     """
#     if not lst:
#         yield []
#         return
#     for i in range(1, len(lst) + 1):
#         for rest in group_partitions(lst[i:]):
#             yield [lst[:i]] + rest
#
#
# def confabulate(phrase: list[str], word_to_phoneme, phoneme_to_word):
#     """ given a phrase, return a confabulated list of words that possess the same phonemes """
#     all_phonemes = [phoneme for word in phrase for phoneme in word_to_phoneme[word]]  # flatten phrase to arbitrary phonemes
#
#     constructed_words = []
#     working_phoneme_index = 0  # index of the start phoneme we are currently working with
#     for phoneme_set in group_partitions(all_phonemes):
#         this_wordset = []
#         for phonetic_word in phoneme_set:
#             if word := phoneme_to_word.get(str(phonetic_word), None):
#                 this_wordset.append(word)
#             else:
#                 break
#         else:
#             # if it got through the loop without breaking, then it's a success
#             constructed_words.append(' '.join(this_wordset))
#             print(f'Success: {phoneme_set} -> {this_wordset}')
#             continue
#
#         print(f'Failed: {phoneme_set} -> {this_wordset}')
#
#     return constructed_words


# runs in O(n^2) time at worst case, usually O(n)!
def confabulate(phrase: str, word_to_phoneme) -> str:
    """ given a phrase, return a confabulated list of words that possess the same phonemes """
    words = normalize_quotes(phrase).upper().split(' ')  # split phrase into words
    phoneme_chunks = [(word, g2p(word)) for word in words]  # get phonemes for each word
    all_phonemes = [phoneme for word, phonemes in phoneme_chunks for phoneme in phonemes]  # flatten phoneme chunks to arbitrary phonemes
    print(f'{C.CYAN}Split phonemes: {all_phonemes}{C.END}')

    cmu_dict_list = list(word_to_phoneme.items())
    # shuffle(cmu_dict_list)  # shuffle to randomize the order of the words
    cmu_dict_list.sort(key=lambda x: len(x[1]), reverse=True)  # prefer longer words first
    cmu_dict_list = [(word, phonemes) for word, phonemes in cmu_dict_list if word not in words] + phoneme_chunks  # move the original words to the list of words to search through (prefer new words)
    print(f'{C.CYAN}Running on a sorted CMU Dictionary of {len(cmu_dict_list)} words!{C.END}')

    def find_next_word(found_words: list[str], remaining_phonemes: list[str]) -> list[str] or None:
        print(f'{C.GREEN}Finding: {found_words} + {remaining_phonemes}{C.END}')
        if not remaining_phonemes:  # if there are no remaining phonemes, then we have found a valid solution!
            return found_words
        for word, phonemes in cmu_dict_list:
            if phonemes == remaining_phonemes[:len(phonemes)]:
                # A word was found for the remaining phonemes, recurse!
                solution = find_next_word(found_words + [word], remaining_phonemes[len(phonemes):])
                if solution:  # if a solution was found, return it
                    return solution
                else:  # if the solution was not valid, continue searching
                    continue
        else:
            # No word was found for remaining phonemes
            print(f'{C.RED}Failed: {found_words} + {remaining_phonemes}{C.END}')
            return None

    # this should never return None, as there should always be at least one solution (the original phrase itself)
    found_words = find_next_word([], all_phonemes)
    assert found_words

    # use regex to filter out 'alternate word' notation, i.e. "reap what you sow(1)"re.sub(r'\(\d+\)', '', word)
    return re.sub(r'\(\d+\)', '', ' '.join(found_words).lower())


def get_oddities():
    """ find words that are pronounced the same as each other EXCEPT for 'TH' -> 'DH' """
    word_to_phoneme, phoneme_to_word = get_cmudict()
    for word, pronunciation in word_to_phoneme.items():
        if ('TH' in pronunciation) and (partner := get_partner(word, pronunciation, word_to_phoneme, phoneme_to_word)):
            print(f'{word} -> {partner} ({arpabet_to_ipa(word_to_phoneme[word])} -> {arpabet_to_ipa(word_to_phoneme[partner])})')


def test_confabulation():
    word_to_phoneme, phoneme_to_word = get_cmudict()
    phrase = input('Enter a phrase: ') or "there's nothing to do in this entire college"
    confabulated = confabulate(phrase, word_to_phoneme)
    print(f'{C.CYAN}Confabulated: {confabulated}{C.END}')



def normalize_quotes(inp: str) -> str:
    return inp.replace('’', "'").replace('“', '"').replace('”', '"')


if __name__ == '__main__':
    # get_oddities()
    test_confabulation()
