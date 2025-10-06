# Ukrainian-Syllable-Splitter
This package is designed to easily split **Ukrainian** words into syllables. 

---
# Ukrainian-Syllable-Splitter
This package is designed to easily split **Ukrainian** words into syllables. 
To use run in terminal:
```pip install git+https://github.com/anastasiia-mozg/Ukrainian-Syllable-Splitter.git```


---
## Notes on External Code Used

In the Ukrainian language, some letters represent more than one sound. For instance: *яблуко* = /йаблуко/, *щерба* = /шчерба/.  
Some of them are combinations of consonants (*щ* = *ш* + *ч*), while others are combinations of a consonant and a vowel (*я* = *йа*, *ю* = *йу*, *є* = *йе*, *ї* = *йі*).  
The latter group is particularly tricky. In some words, they represent two separate sounds (*м'ячик* = /мйачик/), while in others, they represent only one (*няня* = /н’ан’а/).  

These peculiarities of Ukrainian orthography were taken into account in our implementation; otherwise, errors would inevitably occur.

To split a word into syllables correctly, we first need its *phonemic transcription* — that is, we need the **sounds** that make up the word rather than its written letters.  
Such functionality is provided by [this GitHub repository](https://github.com/rbak2/ukrainian_g2p) and is used in our package.

---
## Notes on Syllable Splitting Rules

The rules for syllable division were formulated by Ukrainian phoneticians and are available at this [link](https://ctan.math.utah.edu/ctan/tex-archive/language/ukrainian/ukrhyph/rules_ph.pdf).  
Academic citation:  
**Тоцька Н. І.** *Сучасна українська літературна мова. Фонетика, орфоепія, графіка, орфографія.* — К., 1981. — С. 134–135.

---
## Common Misunderstandings: Syllable Splitting vs. Morphemic Splitting

Although the syllable-splitting rules are strictly defined in the cited source, many people tend to confuse **syllable splitting** with **morphemic splitting** — the process of dividing words into **morphemes** rather than syllables.  

This difference becomes evident, for example, when small children read words syllable by syllable — a process guided by phonetics, not morphology.

In ```test.ipynb```, the test text is [a famous poem by a Ukrainian author](https://onlyart.org.ua/ukrainian-poets/virshi-semenko-myhajlya/semenko-myhajl-vagonovod). The reference syllable splitting was done by a Ukrainian artist who illustrated words with colors, visually marking syllables according to their own interpretation.  
The artist’s splitting rules differed slightly: only about **85%** of the words matched the program’s syllable segmentation.
