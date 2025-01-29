from util.ipa import arpabet_to_ipa
from util.common import C, get_cmudict, remove_word_version, remove_phoneme_stress, normalize_quotes
from g2p_en import G2p


CREATIVITY = 0.3  # amount of phonetic fuzziness the program uses to find alternate words (0 = no change, 1 = 1 change, ...)
FORCE_NOVELTY = True  # whether it searches all other words before using the original words


g2p = G2p()  # g2p directly intelligently words to ARPABET phonemes (not a lookup table)

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

from difflib import SequenceMatcher  # very creative!

def smart_phonetic_match(word_phonemes: list[str], remaining_phonemes: list[str], errors: int = 1) -> bool:
    """ use phonetic similarity to check if the word's phonemes match the first phonemes in the list """
    if len(word_phonemes) > len(
        remaining_phonemes): return False  # if the word is longer than the remaining phonemes, it can't match
    word_ipa = arpabet_to_ipa(word_phonemes)
    comparison_ipa = arpabet_to_ipa(remaining_phonemes[:len(word_phonemes)])

    slips = 0  # 4 * abs(len(word_ipa) - len(comparison_ipa))
    differences = {}
    for i in range(min(len(word_ipa), len(comparison_ipa))):  # iterate over phonemes
        difference = set(word_ipa[i].descriptors) ^ set(
            comparison_ipa[i].descriptors)  # difference between phonemes
        if difference:
            differences[i] = difference

        slips += len(difference) / 2  # add the number of differences to the slip count

    if slips > errors:
        return False
    else:
        print(f'{C.GREEN}Matched: {comparison_ipa} -> {word_ipa} | {differences} {C.END}')
        return True

def fuzzy_phonetic_match(word_phonemes: list[str], remaining_phonemes: list[str], creativity: float = 0.1) -> bool:
    """ check if the word's phonemes match the first phonemes in the list """
    return SequenceMatcher(None, word_phonemes, remaining_phonemes[:len(word_phonemes)]).ratio() >= 1 - creativity

def strict_phonetic_match(word_phonemes: list[str], remaining_phonemes: list[str]) -> bool:
    """ check if the word's phonemes match the first phonemes in the list """
    return word_phonemes == remaining_phonemes[:len(word_phonemes)]

# runs in O(n^2) time at worst case, usually O(n)!
def confabulate(phrase: str, word_to_phoneme) -> str:
    """ given a phrase, return a confabulated list of words that possess the same phonemes """
    words = normalize_quotes(phrase).upper().split(' ')  # split phrase into words
    phoneme_chunks = [(word, remove_phoneme_stress(g2p(word))) for word in
                      words]  # get phonemes for each word, remove stresses
    all_phonemes = [phoneme for word, phonemes in phoneme_chunks for phoneme in
                    phonemes]  # flatten phoneme chunks to arbitrary phonemes
    print(f'{C.CYAN}Split phonemes: {all_phonemes}{C.END}')

    cmu_dict_list = list(word_to_phoneme.items())
    # shuffle(cmu_dict_list)  # shuffle to randomize the order of the words
    cmu_dict_list.sort(key=lambda x: len(x[1]), reverse=True)  # prefer longer words first
    cmu_dict_list = [(word, remove_phoneme_stress(phonemes)) for word, phonemes in cmu_dict_list if not any(
        starting_word in word for starting_word in
        words)] + phoneme_chunks  # move the original words to the list of words to search through (prefer new words)
    print(f'{C.CYAN}Running on a sorted CMU Dictionary of {len(cmu_dict_list)} words!{C.END}')

    def find_next_word(found_words: list[str], remaining_phonemes: list[str]) -> list[str] or None:
        print(f'{C.GREEN}Finding: {found_words} + {remaining_phonemes}{C.END}')
        if not remaining_phonemes:  # if there are no remaining phonemes, then we have found a valid solution!
            return found_words
        for word, phonemes in cmu_dict_list:
            if strict_phonetic_match(phonemes, remaining_phonemes):  # if the phonemes don't match, skip
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
    return remove_word_version(' '.join(found_words).lower())

def test_confabulation():
    word_to_phoneme, phoneme_to_word = get_cmudict()
    phrase = input('Enter a phrase: ') or "the internal revenue service is the greatest agency of all"  # "there's nothing to do in this entire college"
    confabulated = confabulate(phrase, word_to_phoneme)
    print(f'{C.CYAN}Confabulated: {confabulated}{C.END}')