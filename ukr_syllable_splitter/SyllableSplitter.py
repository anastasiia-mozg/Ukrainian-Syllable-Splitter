import re, copy
from .Transcriptor import Transcriptor, split_to_phonemes
from .phoneme_subst_dict import phoneme_to_code_dict


class SyllableSplitter:
    def __init__(self, word):
        self.word = word.lower()
        self.__word_validation_pattern = re.compile('''[-вмлнрйьяюєїбдзжгґпфтсцшщяюєїчкхіуаоие'`]+''')
        self.__validate_word()
        self.__syllable_patterns = ['(?P<Rule1>V([SDG]|[DG]S|GG|DD|DDS|GGS)V)', '(?P<Rule2>V(D[GS]+|SS)V)', '(?P<Rule3>VS{1,}[GDS]+)V']
        self.__patterns = re.compile('|'.join(self.__syllable_patterns))
        
        self.phoneme_transcription = Transcriptor(self.word).transcribe('g2p') # we need it as in Ukrainian there are some letters that stand for two different sounds
        self.phonemes = split_to_phonemes(self.phoneme_transcription).pop()
        self.phoneme_code = self.__get_phoneme_code()
        self.syllables_num = len(self.phoneme_code) - len(self.phoneme_code.replace('V', ''))

    # if we don't check the word, we don't get right answer or even get errors
    def __validate_word(self) -> None:
        if not isinstance(self.word, str):
            raise TypeError("Word must be a string")

        if not self.word:
            raise ValueError("Word cannot be empty")

        match = re.fullmatch(self.__word_validation_pattern, self.word)
        if not match:
            raise ValueError("You can only use Ukrainian letters")

    # the primary reason to encode a word is to make patterns of the syllable splitting more readable and easy for debugging.
    # also the patterns of syllable splitting are written using those codes.
    def __get_phoneme_code(self) -> str:
        code = copy.deepcopy(''.join(self.phonemes))
        for key, value in phoneme_to_code_dict.items():
            pattern = re.compile(key)
            code = re.sub(pattern, value, code)
        return code


    def __get_rule(self, match) -> str:
        rule = str()
        if match:
            groups = match.groupdict()
            rule = next(name for name, value in groups.items() if value)
        return rule

   
    def __get_border_index(self, match, rule_name:str, code:str) -> int:
        if rule_name == 'Rule1':
            return match.start() + 1
        elif rule_name == 'Rule2':
            return match.start() + 2
        elif rule_name == 'Rule3': # in this one the index of the border of syllable depends on the last sonorous sound
            target = re.search(r'S(?=[GD]+)', code)
            return target.end()
        else:
            return len(code)


    def get_syllable_spans(self) -> list:
        spans = list()   
        left_border = 0
        while True:
            if self.syllables_num < 1: # if we have one or zero vowels we have only one syllable
                right_border = len(self.phoneme_code)
                spans.append([left_border, right_border])
                break
            chunk = copy.deepcopy(self.phoneme_code)
            for _ in range(self.syllables_num): # the number of syllables = number of vowels
                match = re.search(self.__patterns, chunk)
                rule = self.__get_rule(match)
                right_border = self.__get_border_index(match, rule, chunk)
                span = (left_border, right_border)
                spans.append(span)
                chunk = self.phoneme_transcription[:right_border] + chunk[right_border:] # we do this to save right indexation
                left_border = right_border
            break
        return spans

    #keep_phoneme_transcription is used as user might not want to get syllables in graphic writting. 
    #Also it can help with debugging as program uses Transcriptor to get phonematic transcription.
    def get_syllables(self, keep_phoneme_transcription:bool=False) -> list:
        syllables = [''.join(self.phonemes[left:right]) for left, right in self.get_syllable_spans()]
        if keep_phoneme_transcription:
            return syllables
        else:
            return [Transcriptor(syllable).p2g() for syllable in syllables]
