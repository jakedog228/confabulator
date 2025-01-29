from util.ipa import arpabet_to_ipa
from util.common import C, get_cmudict


def get_partner(word, pronunciation, d, d_rev):
    partner = d_rev.get(str(['DH' if syl == 'TH' else syl for syl in pronunciation]), None)
    if partner and partner != word:
        return partner
    return None


def get_oddities():
    """ find words that are pronounced the same as each other EXCEPT for 'TH' -> 'DH' """
    word_to_phoneme, phoneme_to_word = get_cmudict()
    for word, pronunciation in word_to_phoneme.items():
        if ('TH' in pronunciation) and (partner := get_partner(word, pronunciation, word_to_phoneme, phoneme_to_word)):
            print(f'{word} -> {partner} ({arpabet_to_ipa(word_to_phoneme[word])} -> {arpabet_to_ipa(word_to_phoneme[partner])})')



if __name__ == '__main__':
    get_oddities()
