# Imports
from .base import *
from detectors import letter_is_vowel, word_vowel_type
from readers import PRONOUNS

# Able type class
class AbleSentence(BaseSentence):
    def __init__(self, pronoun_number, verb, tense):
        BaseSentence.__init__(self, pronoun_number, verb, tense)
        self.special_verb = "алу"

    def make_form(self):
        # Modifying the held verb
        if letter_is_vowel(self.held_verb[-2]):
            self.held_verb_altered = self.held_verb[:-1] + "й"
        else:
            if word_vowel_type(self.held_verb) == "soft":
                self.held_verb_altered = self.held_verb[:-1] + "е"
            else:
                self.held_verb_altered = self.held_verb[:-1] + "а"


        # Getting the sentence
        self.get_conjugations()

