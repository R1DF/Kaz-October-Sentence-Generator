# Imports
from .base import *
from detectors import letter_is_vowel, get_consonant_type, word_vowel_type
from readers import COMMON_DATA

# Motivative type class
class MotivativeSentence(BaseSentence):
    def __init__(self, pronoun_number, verb, tense):
        BaseSentence.__init__(self, pronoun_number, verb, tense)
        self.special_verb = "келу"

    def make_form(self):
        # Modifying the held verb
        self.pronoun = COMMON_DATA["genitiveCase"]["pronouns"][self.pronoun_number]

        # Altering the held verb: First suffix
        first_suffixes = [
            ["ғы", "гі"],
            ["қі", "кі"]
        ]
        determinant = {"hard": 0, "soft": 1}[word_vowel_type(self.held_verb)]
        if get_consonant_type(self.held_verb[-1]) == "voiceless":
            self.held_verb_altered = self.held_verb + first_suffixes[1][determinant]
        else:
            self.held_verb_altered = self.held_verb + first_suffixes[0][determinant]

        # Adding final suffix
        self.held_verb_altered += COMMON_DATA["genitiveCase"]["motivativeMoodEndings"][self.pronoun_number - 1][determinant]

        # Getting the sentence
        self.get_conjugations()

