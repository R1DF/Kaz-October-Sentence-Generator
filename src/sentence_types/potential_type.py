# Imports
from .base import *
from detectors import letter_is_vowel, word_vowel_type

# Potential type class
class PotentialSentence(BaseSentence):
    def __init__(self, pronoun_number, verb, tense):
        BaseSentence.__init__(self, pronoun_number, verb, tense)
        self.special_verb = "тырысу"

    def make_form(self):
        # Modifying the held verb
        if word_vowel_type(self.held_verb) == "hard":
            self.held_verb_altered = self.held_verb + "ға"
        else:
            self.held_verb_altered += self.held_verb + "ге"


        # Getting the sentence
        self.get_conjugations()

