from ipapy.data import UNICODE_TO_IPA
from ipapy.data import load_data_file
from util.IPAString import IPAString
from re import sub


def load_data(data_file_path="arpabet.dat"):
    """
    Load the ARPABET ASCII IPA data from the built-in database.
    Code modified from https://github.com/pettarin/ipapy/blob/master/ipapy/arpabetmapper.py
    Data file ref: https://github.com/pettarin/ipapy/blob/master/ipapy/data/arpabet.dat
    """
    arpabet_to_ipa_chars = dict()
    for line in load_data_file(
            file_path=data_file_path,
            file_path_is_relative=True,
            line_format=u"UA"
    ):
        i_unicode, i_arpabet = line
        if (len(i_unicode) == 0) or (len(i_arpabet) == 0):
            raise ValueError("Data file '%s' contains a bad line: '%s'" % (data_file_path, line))
        i_unicode = i_unicode[0]
        i_arpabet = i_arpabet[0]
        val = tuple([UNICODE_TO_IPA[c] for c in i_unicode])
        arpabet_to_ipa_chars[i_arpabet] = val

    return arpabet_to_ipa_chars  # note: some ARPABET characters may map to multiple IPA characters


arpabet_to_ipa_chars = load_data()
def arpabet_to_ipa(arpabet_chars: list[str]):
    if not arpabet_chars or not all(arpabet_char for arpabet_char in arpabet_chars):
        return IPAString()
    ipa_chars = [ipa_char for arpabet_char in arpabet_chars for ipa_char in arpabet_to_ipa_chars[sub(r'\d+', '', arpabet_char)]]  # flatten list of tuples AND remove numbers (nuances) from ARPABET characters
    ipa_string = IPAString(ipa_chars=ipa_chars)
    return ipa_string


def ipa_to_arpabet(ipa_string: IPAString):
    arpabet_chars = []
    for ipa_char in ipa_string:
        for arpabet_char, ipa_chars in arpabet_to_ipa_chars.items():
            if ipa_char in ipa_chars:
                arpabet_chars.append(arpabet_char)
                break
        else:
            raise ValueError(f"IPA character '{ipa_char}' not found in database!")
    return arpabet_chars


if __name__ == "__main__":
    arpabet_text = "HH AH L OW".split(' ')
    ipa_string = arpabet_to_ipa(arpabet_text)
    print(f'"{arpabet_text}" -> "{ipa_string}"')  # Output: "['HH', 'AH', 'L', 'OW']" -> "hʌloʊ"
    print(f'"{ipa_string}" -> "{ipa_to_arpabet(ipa_string)}"')  # Output: "hʌloʊ" -> "['HH', 'AH', 'L', 'OH', 'UH']"
