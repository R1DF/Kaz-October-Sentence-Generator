# Imports
from readers import PRONOUNS

# Sentence class
class Sentence:
    def __init__(self, pronoun_number, type_number, tense_number, verb):
        # Values upon initialization
        self.pronoun_number = pronoun_number
        self.type_number = type_number
        self.tense_number = tense_number
        self.verb = verb
        self.is_constructed = False
        self.sentences = []

        # Getting correct words
        self.pronoun = PRONOUNS[self.pronoun_number - 1]

    def construct(self):
        if self.type_number == 4:
            pass
        else:
            pass

    def print_sentence(self):
        if self.is_constructed:
            for sentence_index in range(len(self.sentences)):
                # Prints out every possible sentence whilst following grammar rules in terms of writing
                print(f"{sentence_index + 1}. {self.pronoun.captalize()} {' '.join(self.sentences[sentence_index])}")
