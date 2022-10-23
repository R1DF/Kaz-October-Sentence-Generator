"""
Kazakh October Sentence Generator (KSG Oct. version)
"""

# Imports
from tools import *
from readers import *
from sentence_types.able_type import AbleSentence
from sentence_types.motivative_type import MotivativeSentence
from sentence_types.obligative_type import ObligativeSentence
from sentence_types.potential_type import PotentialSentence
from sentence_types.neutral_type import NeutralSentence
import random

# Main code
def main():
    title("Kazakh Sentence Generator (October 2022 instalment)") # Titling
    # LOGIC ERROR WITH PAST SIMPLE, INDEXES + ADD MORE ERROR CHECKING (3-4-5)
    # Introduction
    clear()
    print("Kazakh Sentence Generator (October '22)")
    print("Please enter your desired combination of the sentence to generate one. (Hit Ctrl+C to quit.)")

    # Pronoun selection
    break_line()
    print("Stage I. Pronoun")
    for pronoun_number in range(len(PRONOUNS)):
        print(f"{pronoun_number + 1}. {PRONOUNS[pronoun_number]} / {PRONOUN_DESCRIPTIONS[pronoun_number]}")
    break_line()
    pronoun_number = pursue_int_input("Enter select pronoun by number", 1, 8)

    # Sentence type selection
    break_line()
    print("Stage II. Mood / Type")
    for sentence_type_number in range(len(SENTENCE_TYPES)):
        print(f"{sentence_type_number + 1}. {SENTENCE_TYPES[sentence_type_number]} / {SENTENCE_TYPES_DESCRIPTIONS[sentence_type_number]}")
    break_line()
    sentence_type_number = pursue_int_input("Enter sentence type by number", 1, 5)

    # Tense selection
    break_line()
    print("Stage III. Tense")
    for tense_number in range(len(TENSES)):
        print(
            f"{tense_number + 1}. {TENSES[tense_number]} / {TENSES_DESCRIPTIONS[tense_number]}")
    break_line()
    tense_number = pursue_int_input("Enter tense by number", 1, 8)

    # Verb selection
    break_line()
    print("Stage IV. Verb")
    random_verb = random.choice(VERBS)
    print("Selected verb:", random_verb)
    await_key_press()

    # Recap
    clear()
    print("Your sentence structure:")
    print("Pronoun:", PRONOUNS[pronoun_number - 1])
    print("Mood / Type:", SENTENCE_TYPES[sentence_type_number - 1])
    print("Tense:", TENSES[tense_number - 1])
    print("Verb:", random_verb)
    break_line(2)

    await_key_press()

    # Making the sentence type object
    match sentence_type_number:
        case 1:
            sentence = AbleSentence(pronoun_number, random_verb, tense_number)
        case 2:
            sentence = MotivativeSentence(pronoun_number, random_verb, tense_number)
        case 3:
            sentence = ObligativeSentence(pronoun_number, random_verb, tense_number)
        case 4:
            sentence = PotentialSentence(pronoun_number, random_verb, tense_number)
        case 5:
            sentence = NeutralSentence(pronoun_number, random_verb, tense_number)
    sentence.make_form()
    if sentence_type_number != 3:
        sentence.make_sentences()  # obligative form is simple and doesn't need this
    sentence.print_sentences()

# Running the function
try:
    main()
except KeyboardInterrupt:
    clear()
    quit()
