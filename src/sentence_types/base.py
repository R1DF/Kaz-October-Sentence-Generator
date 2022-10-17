# Imports
from tenses.present import PresentTense
from tenses.continuous import ContinuousTense
from tenses.future_motivative import FutureMotivativeTense
from tenses.future_potential import FuturePotentialTense
from tenses.past_obvious import PastObviousTense
from tenses.past_uncertain import PastUncertainTense
from tenses.past_continuous import PastContinuousTense
from tenses.past_simple import PastSimpleTense
from readers import PRONOUNS

# Base Sentence class
class BaseSentence:
    def __init__(self, pronoun_number, verb, tense_number):
        self.pronoun_number = pronoun_number
        self.held_verb = verb
        self.tense = tense_number
        self.special_verb = None,
        self.held_verb_altered = None
        self.conjugations = []
        self.sentences = []

    def get_conjugations(self):
        for negation in [False, True]:
            # Getting the tense
            match self.tense:
                case 1:
                    self.tense_object = ContinuousTense(self.pronoun_number, negation)
                case 2:
                    self.tense_object = PresentTense(self.pronoun_number, negation, "complex")
                case 3:
                    self.tense_object = PastSimpleTense(self.pronoun_number, negation)
                case 4:
                    self.tense_object = FutureMotivativeTense(self.pronoun_number, negation)
                case 5:
                    self.tense_object = FuturePotentialTense(self.pronoun_number, negation)
                case 6:
                    self.tense_object = PastObviousTense(self.pronoun_number, negation)
                case 7:
                    self.tense_object = PastUncertainTense(self.pronoun_number, negation)
                case 8:
                    self.tense_object = PastContinuousTense(self.pronoun_number, negation)

            # Manually setting the infinitive and making sure negation applies appropriately
            self.tense_object.set_infinitive(self.special_verb)
            self.tense_object.conjugate()

            # Conjugations and configuring
            conjugated = self.tense_object.conjugated
            if type(conjugated) is str:
                self.conjugations.append(conjugated)
            else:
                for conjugated in conjugated:
                    self.conjugations.append(conjugated)

    def make_sentences(self):
        for conjugation in self.conjugations:
            beginning = f"{PRONOUNS[self.pronoun_number - 1].capitalize()} {self.held_verb_altered}"
            self.sentences.append(f"{beginning} {conjugation}.")

    def print_sentences(self):
        for sentence in self.sentences:
            print(sentence)
