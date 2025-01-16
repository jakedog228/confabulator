"""I wrote this script initially in the python terminal, so it wasn't designed with refactorability in mind"""


with open('cmudict-0.7b', 'r') as f:
    raw = f.read()

uncomment = [x for x in raw.split('\n')[:-1] if not x.startswith(';;;')]
d = {word: pronunciation.split(' ') for word, pronunciation in [x.split('  ') for x in uncomment]}
d_rev = {str(b): a for a, b in d.items()}
for word, pronunciation in d.items():
    if (
            ('TH' in pronunciation) and  # if the word has a 'TH' sound
            (partner := d_rev.get(str(['DH' if syl == 'TH' else syl for syl in pronunciation]), None)) and  # partner TH -> DH exists
            (partner != word)  # partner is not the same word
    ):
        print(f'{word} -> {partner} ({pronunciation} -> {d[partner]})')
