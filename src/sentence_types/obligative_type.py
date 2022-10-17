# Imports
from .base import *
from detectors import letter_is_vowel, word_vowel_type
from readers import COMMON_DATA

# Obligative type class
class ObligativeSentence(BaseSentence):
    def __init__(self, pronoun_number, verb, tense):
        BaseSentence.__init__(self, pronoun_number, verb, tense)

    def make_form(self):
        # There's 2 way to make this kind of sentence with "керек"
        self.sentences.append(f"{COMMON_DATA['dativeCase'][self.pronoun_number].capitalize()} {self.held_verb} керек.")

        # Second way is a bit more complicated
        self.held_verb_altered = self.held_verb + COMMON_DATA["genitiveCase"]['caseEndings'][self.pronoun_number][{"hard": 0, "soft": 1}[word_vowel_type(self.held_verb)]]
        self.sentences.append(f"{COMMON_DATA['genitiveCase']['pronouns'][self.pronoun_number].capitalize()} {self.held_verb_altered} керек.")

