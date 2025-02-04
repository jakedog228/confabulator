from util.ipa import arpabet_to_ipa
from util.common import get_cmudict, remove_word_version, remove_phoneme_stress, normalize_quotes
from util.common import Color as C
from g2p_en import G2p
from difflib import SequenceMatcher


g2p = G2p()  # intelligent g2p using ML (words -> ARPABET phonemes)


def smart_phonetic_match(word_phonemes: list[str], remaining_phonemes: list[str], errors: int = 1) -> bool:
    """ use phonetic similarity to check if the word's phonemes match the first phonemes in the list """
    # if the word is longer than the remaining phonemes, it can't match
    if len(word_phonemes) > len(remaining_phonemes):
        return False

    # convert ARPABET phonemes to IPA phonemes
    word_ipa = arpabet_to_ipa(word_phonemes)
    comparison_ipa = arpabet_to_ipa(remaining_phonemes[:len(word_phonemes)])

    slips = 0  # 4 * abs(len(word_ipa) - len(comparison_ipa))
    differences = {}
    for i in range(min(len(word_ipa), len(comparison_ipa))):  # iterate over phonemes
        difference = set(word_ipa[i].descriptors) ^ set(comparison_ipa[i].descriptors)  # difference between phonemes
        if difference:
            differences[i] = difference

            # TODO: modify to punish larger differences more, e.g. "gestures":"gestured" is worse than "gestures":"jesters"
            slips += len(difference) / 2  # add the number of differences to the slip count

            # if the number of slips is greater than the number of allowed errors, it's not a match
            if slips > errors:
                return False

    # if it gets through all the phonemes, it's a match!
    print(f'{C.GREEN}+ Matched: {comparison_ipa} -> {word_ipa} | {differences} {C.END}')
    return True

def fuzzy_phonetic_match(word_phonemes: list[str], remaining_phonemes: list[str], creativity: float = 0.1) -> bool:
    """ use basic sequence matching to match the first phonemes in the list """
    return SequenceMatcher(None, word_phonemes, remaining_phonemes[:len(word_phonemes)]).ratio() >= 1 - creativity

def strict_phonetic_match(word_phonemes: list[str], remaining_phonemes: list[str]) -> bool:
    """ check if the word's phonemes exactly match the first phonemes in the list """
    return word_phonemes == remaining_phonemes[:len(word_phonemes)]

# runs in O(n^2) time at worst case, usually O(n)!
def confabulate(phrase: str, word_to_phoneme: dict, match_function) -> str:
    """ given a phrase, return a confabulated list of words that possess the same phonemes """
    words = normalize_quotes(phrase).lower().split(' ')  # split phrase into words
    phoneme_chunks = [(word, remove_phoneme_stress(g2p(word))) for word in words]  # get phonemes for each word, remove stresses
    all_phonemes = [phoneme for word, phonemes in phoneme_chunks for phoneme in phonemes]  # flatten phoneme chunks to arbitrary phonemes
    print(f'{C.CYAN}@@ Split phonemes: {all_phonemes} @@{C.END}')

    # sort the CMU dict to prefer longer words that aren't in the original phrase
    cmu_dict_list = list(word_to_phoneme.items())
    cmu_dict_list.sort(key=lambda x: len(x[1]), reverse=True)  # prefer longer words first
    cmu_dict_list = [(word, remove_phoneme_stress(phonemes)) for word, phonemes in cmu_dict_list if not any(starting_word in word for starting_word in words)] + phoneme_chunks  # move the original words to the list of words to search through (prefer new words)
    print(f'{C.CYAN}@@ Running on a sorted CMU Dictionary of {len(cmu_dict_list)} words! @@{C.END}')

    def find_next_word(found_words: list[str], remaining_phonemes: list[str]) -> list[str] or None:
        """ recursive search for a next word that matches the remaining phonemes """
        print(f'{C.GREEN}+ Finding: {found_words} + {remaining_phonemes}{C.END}')
        if not remaining_phonemes:  # if there are no remaining phonemes, then we have found a valid solution!
            return found_words

        # iterate over the sorted CMU dict to find a word that matches the remaining phonemes
        for word, phonemes in cmu_dict_list:
            if match_function(phonemes, remaining_phonemes):  # if the phonemes don't match, skip
                # A word was found for the remaining phonemes, recurse!
                solution = find_next_word(found_words + [word], remaining_phonemes[len(phonemes):])
                if solution:  # if a solution was found, return it
                    return solution
                else:  # if no solution found (no words fit remaining phonemes), continue searching
                    continue
        else:
            # No word was found for remaining phonemes
            print(f'{C.RED}- Failed: {found_words} + {remaining_phonemes}{C.END}')
            return None

    # this should never return None, as there should always be at least one solution (the original phrase itself)
    found_words = find_next_word([], all_phonemes)
    assert found_words

    # use regex to filter out 'alternate word' notation, i.e. "reap what you sow(1)"re.sub(r'\(\d+\)', '', word)
    return remove_word_version(' '.join(found_words).lower())

if __name__ == '__main__':

    # select a match type
    match_type = input('Enter a match type (smart, fuzzy, strict): ') or 'strict'
    match_func = {'smart': smart_phonetic_match, 'fuzzy': fuzzy_phonetic_match, 'strict': strict_phonetic_match}[match_type]

    # get the phrase to confabulate
    phrase = input('Enter a phrase (or leave empty for a default): ') or "the internal revenue service is the greatest agency of all"
    phrase = phrase.replace(',','').replace('.','').lower()

    # run the confabulator
    print(f'{C.CYAN}@@ Running `{match_type}` on "{phrase}" @@{C.END}')
    word_to_phoneme, phoneme_to_word = get_cmudict()
    confabulated = confabulate(phrase, word_to_phoneme, match_func)
    print(f'{C.CYAN}@@ Confabulated: {confabulated} @@{C.END}')