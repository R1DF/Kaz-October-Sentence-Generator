# Imports
from .base import *
from readers import PRONOUNS

# Neutral Sentence class
class NeutralSentence(BaseSentence):
    def __init__(self, pronoun_number, verb, tense):
        BaseSentence.__init__(self, pronoun_number, verb, tense)
        self.special_verb = verb

    def make_form(self):
        # Getting the sentence
        self.get_conjugations()

    def make_sentences(self):
        for conjugation in self.conjugations:
            beginning = f"{PRONOUNS[self.pronoun_number - 1].capitalize()}"
            self.sentences.append(f"{beginning} {conjugation}.")

