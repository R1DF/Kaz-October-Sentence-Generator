"""
Kazakh October Sentence Generator (KSG Oct. version)
"""

# Imports
from tools import *
from readers import *
import random

# Main code
def main():
    title("Kazakh Sentence Generator (October 2022 instalment)") # Titling

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
    pronoun_number = pursue_int_input("Enter select pronoun by number", 1, 8) - 1

    # Sentence type selection
    break_line()
    print("Stage II. Mood / Type")
    for sentence_type_number in range(len(SENTENCE_TYPES)):
        print(f"{sentence_type_number + 1}. {SENTENCE_TYPES[sentence_type_number]} / {SENTENCE_TYPES_DESCRIPTIONS[sentence_type_number]}")
    break_line()
    sentence_type_number = pursue_int_input("Enter sentence type by number", 1, 5) - 1

    # Tense selection
    break_line()
    print("Stage III. Tense")
    for tense_number in range(len(TENSES)):
        print(
            f"{tense_number + 1}. {TENSES[tense_number]} / {TENSES_DESCRIPTIONS[tense_number]}")
    break_line()
    tense_number = pursue_int_input("Enter tense by number", 1, 8) - 1

    # Verb selection
    break_line()
    print("Stage IV. Verb")
    random_verb = random.choice(VERBS)
    print("Selected verb:", random_verb)
    await_key_press()

    # Recap
    clear()
    print("Your sentence structure:")
    print("Pronoun:", PRONOUNS[pronoun_number])
    print("Mood / Type:", SENTENCE_TYPES[sentence_type_number])
    print("Tense:", TENSES[tense_number])
    print("Verb:", random_verb)
    break_line(2)

    await_key_press()
    clear()

# Running the function
try:
    main()
except KeyboardInterrupt:
    clear()
    quit()
