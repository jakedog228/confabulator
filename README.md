## Confabulator

This is us il e scrip twitch takes uh frey's und confounds it's foe nemes.

### Strict Matching
```diff
Enter a match type (smart, fuzzy, strict): strict
Enter a phrase (or leave empty for a default): this is a silly script which takes a phrase and confounds its phonemes
@@ Running `strict` on "this is a silly script which takes a phrase and confounds its phonemes" @@
! Loading CMU Dictionary...
! CMU Dictionary loaded!
@@ Split phonemes: ['DH', 'IH', 'S', 'IH', 'Z', 'AH', 'S', 'IH', 'L', 'IY', 'S', 'K', 'R', 'IH', 'P', 'T', 'W', 'IH', 'CH', 'T', 'EY', 'K', 'S', 'AH', 'F', 'R', 'EY', 'Z', 'AH', 'N', 'D', 'K', 'AH', 'N', 'F', 'AW', 'N', 'D', 'Z', 'IH', 'T', 'S', 'F', 'OW', 'N', 'IY', 'M', 'Z'] @@
@@ Running on a sorted CMU Dictionary of 55700 words! @@
+ Finding: [] + ['DH', 'IH', 'S', 'IH', 'Z', 'AH', 'S', 'IH', 'L', 'IY', 'S', 'K', 'R', 'IH', 'P', 'T', 'W', 'IH', 'CH', 'T', 'EY', 'K', 'S', 'AH', 'F', 'R', 'EY', 'Z', 'AH', 'N', 'D', 'K', 'AH', 'N', 'F', 'AW', 'N', 'D', 'Z', 'IH', 'T', 'S', 'F', 'OW', 'N', 'IY', 'M', 'Z']
+ Finding: ['this'] + ['IH', 'Z', 'AH', 'S', 'IH', 'L', 'IY', 'S', 'K', 'R', 'IH', 'P', 'T', 'W', 'IH', 'CH', 'T', 'EY', 'K', 'S', 'AH', 'F', 'R', 'EY', 'Z', 'AH', 'N', 'D', 'K', 'AH', 'N', 'F', 'AW', 'N', 'D', 'Z', 'IH', 'T', 'S', 'F', 'OW', 'N', 'IY', 'M', 'Z']
+ Finding: ['this', 'is'] + ['AH', 'S', 'IH', 'L', 'IY', 'S', 'K', 'R', 'IH', 'P', 'T', 'W', 'IH', 'CH', 'T', 'EY', 'K', 'S', 'AH', 'F', 'R', 'EY', 'Z', 'AH', 'N', 'D', 'K', 'AH', 'N', 'F', 'AW', 'N', 'D', 'Z', 'IH', 'T', 'S', 'F', 'OW', 'N', 'IY', 'M', 'Z']
+ Finding: ['this', 'is', 'us'] + ['IH', 'L', 'IY', 'S', 'K', 'R', 'IH', 'P', 'T', 'W', 'IH', 'CH', 'T', 'EY', 'K', 'S', 'AH', 'F', 'R', 'EY', 'Z', 'AH', 'N', 'D', 'K', 'AH', 'N', 'F', 'AW', 'N', 'D', 'Z', 'IH', 'T', 'S', 'F', 'OW', 'N', 'IY', 'M', 'Z']
+ Finding: ['this', 'is', 'us', 'il'] + ['IY', 'S', 'K', 'R', 'IH', 'P', 'T', 'W', 'IH', 'CH', 'T', 'EY', 'K', 'S', 'AH', 'F', 'R', 'EY', 'Z', 'AH', 'N', 'D', 'K', 'AH', 'N', 'F', 'AW', 'N', 'D', 'Z', 'IH', 'T', 'S', 'F', 'OW', 'N', 'IY', 'M', 'Z']
+ Finding: ['this', 'is', 'us', 'il', 'e'] + ['S', 'K', 'R', 'IH', 'P', 'T', 'W', 'IH', 'CH', 'T', 'EY', 'K', 'S', 'AH', 'F', 'R', 'EY', 'Z', 'AH', 'N', 'D', 'K', 'AH', 'N', 'F', 'AW', 'N', 'D', 'Z', 'IH', 'T', 'S', 'F', 'OW', 'N', 'IY', 'M', 'Z']
+ Finding: ['this', 'is', 'us', 'il', 'e', 'scrip'] + ['T', 'W', 'IH', 'CH', 'T', 'EY', 'K', 'S', 'AH', 'F', 'R', 'EY', 'Z', 'AH', 'N', 'D', 'K', 'AH', 'N', 'F', 'AW', 'N', 'D', 'Z', 'IH', 'T', 'S', 'F', 'OW', 'N', 'IY', 'M', 'Z']
+ Finding: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitched'] + ['EY', 'K', 'S', 'AH', 'F', 'R', 'EY', 'Z', 'AH', 'N', 'D', 'K', 'AH', 'N', 'F', 'AW', 'N', 'D', 'Z', 'IH', 'T', 'S', 'F', 'OW', 'N', 'IY', 'M', 'Z']
- Failed: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitched'] + ['EY', 'K', 'S', 'AH', 'F', 'R', 'EY', 'Z', 'AH', 'N', 'D', 'K', 'AH', 'N', 'F', 'AW', 'N', 'D', 'Z', 'IH', 'T', 'S', 'F', 'OW', 'N', 'IY', 'M', 'Z']
+ Finding: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch'] + ['T', 'EY', 'K', 'S', 'AH', 'F', 'R', 'EY', 'Z', 'AH', 'N', 'D', 'K', 'AH', 'N', 'F', 'AW', 'N', 'D', 'Z', 'IH', 'T', 'S', 'F', 'OW', 'N', 'IY', 'M', 'Z']
+ Finding: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes'] + ['AH', 'F', 'R', 'EY', 'Z', 'AH', 'N', 'D', 'K', 'AH', 'N', 'F', 'AW', 'N', 'D', 'Z', 'IH', 'T', 'S', 'F', 'OW', 'N', 'IY', 'M', 'Z']
+ Finding: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh'] + ['F', 'R', 'EY', 'Z', 'AH', 'N', 'D', 'K', 'AH', 'N', 'F', 'AW', 'N', 'D', 'Z', 'IH', 'T', 'S', 'F', 'OW', 'N', 'IY', 'M', 'Z']
+ Finding: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh', "frey's"] + ['AH', 'N', 'D', 'K', 'AH', 'N', 'F', 'AW', 'N', 'D', 'Z', 'IH', 'T', 'S', 'F', 'OW', 'N', 'IY', 'M', 'Z']
+ Finding: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh', "frey's", 'und'] + ['K', 'AH', 'N', 'F', 'AW', 'N', 'D', 'Z', 'IH', 'T', 'S', 'F', 'OW', 'N', 'IY', 'M', 'Z']
+ Finding: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh', "frey's", 'und', 'kuhne'] + ['F', 'AW', 'N', 'D', 'Z', 'IH', 'T', 'S', 'F', 'OW', 'N', 'IY', 'M', 'Z']
+ Finding: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh', "frey's", 'und', 'kuhne', 'found'] + ['Z', 'IH', 'T', 'S', 'F', 'OW', 'N', 'IY', 'M', 'Z']
- Failed: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh', "frey's", 'und', 'kuhne', 'found'] + ['Z', 'IH', 'T', 'S', 'F', 'OW', 'N', 'IY', 'M', 'Z']
- Failed: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh', "frey's", 'und', 'kuhne'] + ['F', 'AW', 'N', 'D', 'Z', 'IH', 'T', 'S', 'F', 'OW', 'N', 'IY', 'M', 'Z']
+ Finding: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh', "frey's", 'und', 'kun'] + ['F', 'AW', 'N', 'D', 'Z', 'IH', 'T', 'S', 'F', 'OW', 'N', 'IY', 'M', 'Z']
+ Finding: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh', "frey's", 'und', 'kun', 'found'] + ['Z', 'IH', 'T', 'S', 'F', 'OW', 'N', 'IY', 'M', 'Z']
- Failed: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh', "frey's", 'und', 'kun', 'found'] + ['Z', 'IH', 'T', 'S', 'F', 'OW', 'N', 'IY', 'M', 'Z']
- Failed: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh', "frey's", 'und', 'kun'] + ['F', 'AW', 'N', 'D', 'Z', 'IH', 'T', 'S', 'F', 'OW', 'N', 'IY', 'M', 'Z']
+ Finding: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh', "frey's", 'und', 'confounds'] + ['IH', 'T', 'S', 'F', 'OW', 'N', 'IY', 'M', 'Z']
+ Finding: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh', "frey's", 'und', 'confounds', "it's"] + ['F', 'OW', 'N', 'IY', 'M', 'Z']
+ Finding: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh', "frey's", 'und', 'confounds', "it's", 'phoneme'] + ['Z']
- Failed: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh', "frey's", 'und', 'confounds', "it's", 'phoneme'] + ['Z']
+ Finding: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh', "frey's", 'und', 'confounds', "it's", 'phoney'] + ['M', 'Z']
- Failed: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh', "frey's", 'und', 'confounds', "it's", 'phoney'] + ['M', 'Z']
+ Finding: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh', "frey's", 'und', 'confounds', "it's", 'phony'] + ['M', 'Z']
- Failed: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh', "frey's", 'und', 'confounds', "it's", 'phony'] + ['M', 'Z']
+ Finding: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh', "frey's", 'und', 'confounds', "it's", 'fone'] + ['IY', 'M', 'Z']
+ Finding: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh', "frey's", 'und', 'confounds', "it's", 'fone', 'e'] + ['M', 'Z']
- Failed: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh', "frey's", 'und', 'confounds', "it's", 'fone', 'e'] + ['M', 'Z']
+ Finding: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh', "frey's", 'und', 'confounds', "it's", 'fone', 'e.'] + ['M', 'Z']
- Failed: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh', "frey's", 'und', 'confounds', "it's", 'fone', 'e.'] + ['M', 'Z']
+ Finding: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh', "frey's", 'und', 'confounds', "it's", 'fone', 'ee'] + ['M', 'Z']
- Failed: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh', "frey's", 'und', 'confounds', "it's", 'fone', 'ee'] + ['M', 'Z']
- Failed: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh', "frey's", 'und', 'confounds', "it's", 'fone'] + ['IY', 'M', 'Z']
+ Finding: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh', "frey's", 'und', 'confounds', "it's", 'phone'] + ['IY', 'M', 'Z']
+ Finding: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh', "frey's", 'und', 'confounds', "it's", 'phone', 'e'] + ['M', 'Z']
- Failed: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh', "frey's", 'und', 'confounds', "it's", 'phone', 'e'] + ['M', 'Z']
+ Finding: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh', "frey's", 'und', 'confounds', "it's", 'phone', 'e.'] + ['M', 'Z']
- Failed: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh', "frey's", 'und', 'confounds', "it's", 'phone', 'e.'] + ['M', 'Z']
+ Finding: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh', "frey's", 'und', 'confounds', "it's", 'phone', 'ee'] + ['M', 'Z']
- Failed: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh', "frey's", 'und', 'confounds', "it's", 'phone', 'ee'] + ['M', 'Z']
- Failed: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh', "frey's", 'und', 'confounds', "it's", 'phone'] + ['IY', 'M', 'Z']
+ Finding: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh', "frey's", 'und', 'confounds', "it's", 'foe'] + ['N', 'IY', 'M', 'Z']
+ Finding: ['this', 'is', 'us', 'il', 'e', 'scrip', 'twitch', 'takes', 'uh', "frey's", 'und', 'confounds', "it's", 'foe', 'nemes'] + []
@@ Confabulated: this is us il e scrip twitch takes uh frey's und confounds it's foe nemes @@
```

### "Smart" Matching
A WIP Attempt to use a more flexible matching algorithm to find more creative matches.

"the intern ulrey vienneau searfoss as thug latest agent ia faul"
```diff
Enter a match type (smart, fuzzy, strict): smart
Enter a phrase (or leave empty for a default): the internal revenue service is the greatest agency of all
@@ Running `smart` on "the internal revenue service is the greatest agency of all" @@
! Loading CMU Dictionary...
! CMU Dictionary loaded!
@@ Split phonemes: ['DH', 'AH', 'IH', 'N', 'T', 'ER', 'N', 'AH', 'L', 'R', 'EH', 'V', 'AH', 'N', 'UW', 'S', 'ER', 'V', 'AH', 'S', 'IH', 'Z', 'DH', 'AH', 'G', 'R', 'EY', 'T', 'AH', 'S', 'T', 'EY', 'JH', 'AH', 'N', 'S', 'IY', 'AH', 'V', 'AO', 'L'] @@
@@ Running on a sorted CMU Dictionary of 114033 words! @@
+ Finding: [] + ['DH', 'AH', 'IH', 'N', 'T', 'ER', 'N', 'AH', 'L', 'R', 'EH', 'V', 'AH', 'N', 'UW', 'S', 'ER', 'V', 'AH', 'S', 'IH', 'Z', 'DH', 'AH', 'G', 'R', 'EY', 'T', 'AH', 'S', 'T', 'EY', 'JH', 'AH', 'N', 'S', 'IY', 'AH', 'V', 'AO', 'L']
+ Matched: ðʌ -> ðʌ | {} 
+ Finding: ['the'] + ['IH', 'N', 'T', 'ER', 'N', 'AH', 'L', 'R', 'EH', 'V', 'AH', 'N', 'UW', 'S', 'ER', 'V', 'AH', 'S', 'IH', 'Z', 'DH', 'AH', 'G', 'R', 'EY', 'T', 'AH', 'S', 'T', 'EY', 'JH', 'AH', 'N', 'S', 'IY', 'AH', 'V', 'AO', 'L']
+ Matched: intɝn -> intɝn | {} 
+ Finding: ['the', 'intern'] + ['AH', 'L', 'R', 'EH', 'V', 'AH', 'N', 'UW', 'S', 'ER', 'V', 'AH', 'S', 'IH', 'Z', 'DH', 'AH', 'G', 'R', 'EY', 'T', 'AH', 'S', 'T', 'EY', 'JH', 'AH', 'N', 'S', 'IY', 'AH', 'V', 'AO', 'L']
+ Matched: ʌlɹe -> ʌlɹi | {3: {'close', 'close-mid'}} 
+ Finding: ['the', 'intern', 'ulrey'] + ['V', 'AH', 'N', 'UW', 'S', 'ER', 'V', 'AH', 'S', 'IH', 'Z', 'DH', 'AH', 'G', 'R', 'EY', 'T', 'AH', 'S', 'T', 'EY', 'JH', 'AH', 'N', 'S', 'IY', 'AH', 'V', 'AO', 'L']
+ Matched: vʌnu -> vʌnoʊ | {3: {'close', 'close-mid'}} 
+ Finding: ['the', 'intern', 'ulrey', 'vienneau'] + ['S', 'ER', 'V', 'AH', 'S', 'IH', 'Z', 'DH', 'AH', 'G', 'R', 'EY', 'T', 'AH', 'S', 'T', 'EY', 'JH', 'AH', 'N', 'S', 'IY', 'AH', 'V', 'AO', 'L']
+ Matched: sɝvʌs -> sɝfʌs | {2: {'voiced', 'voiceless'}} 
+ Finding: ['the', 'intern', 'ulrey', 'vienneau', 'searfoss'] + ['IH', 'Z', 'DH', 'AH', 'G', 'R', 'EY', 'T', 'AH', 'S', 'T', 'EY', 'JH', 'AH', 'N', 'S', 'IY', 'AH', 'V', 'AO', 'L']
+ Matched: iz -> az | {0: {'close', 'open'}} 
+ Finding: ['the', 'intern', 'ulrey', 'vienneau', 'searfoss', 'as'] + ['DH', 'AH', 'G', 'R', 'EY', 'T', 'AH', 'S', 'T', 'EY', 'JH', 'AH', 'N', 'S', 'IY', 'AH', 'V', 'AO', 'L']
+ Matched: ðʌɡ -> θʌɡ | {0: {'voiceless', 'voiced'}} 
+ Finding: ['the', 'intern', 'ulrey', 'vienneau', 'searfoss', 'as', 'thug'] + ['R', 'EY', 'T', 'AH', 'S', 'T', 'EY', 'JH', 'AH', 'N', 'S', 'IY', 'AH', 'V', 'AO', 'L']
+ Matched: ɹɘɪtʌst -> lɘɪtʌst | {0: {'lateral-approximant', 'approximant'}} 
+ Finding: ['the', 'intern', 'ulrey', 'vienneau', 'searfoss', 'as', 'thug', 'latest'] + ['EY', 'JH', 'AH', 'N', 'S', 'IY', 'AH', 'V', 'AO', 'L']
+ Matched: ɘɪd͡ʒʌns -> ɘɪd͡ʒʌnt | {5: {'plosive', 'sibilant-fricative'}} 
+ Finding: ['the', 'intern', 'ulrey', 'vienneau', 'searfoss', 'as', 'thug', 'latest', 'agent'] + ['IY', 'AH', 'V', 'AO', 'L']
+ Matched: iʌ -> iʌ | {} 
+ Finding: ['the', 'intern', 'ulrey', 'vienneau', 'searfoss', 'as', 'thug', 'latest', 'agent', 'ia'] + ['V', 'AO', 'L']
+ Matched: vɔl -> fɔl | {0: {'voiced', 'voiceless'}} 
+ Finding: ['the', 'intern', 'ulrey', 'vienneau', 'searfoss', 'as', 'thug', 'latest', 'agent', 'ia', 'faul'] + []
@@ Confabulated: the intern ulrey vienneau searfoss as thug latest agent ia faul @@
```

### Disclaimer
This code is for educational purposes only. Please do not use this code for awesome subliminal attacks on targeted individuals. They'd never even notice. 

