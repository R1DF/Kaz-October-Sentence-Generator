# Imports
from readers import VOWELS, CONSONANTS

def letter_is_vowel(letter):
    return letter.upper() in VOWELS["soft"] + VOWELS["hard"]

def get_vowel_type(letter):
    if letter.upper() in VOWELS["soft"]:
        return "soft"
    elif letter.upper() in VOWELS["hard"]:
        return "hard"

def get_consonant_type(letter):
    if letter.upper() in CONSONANTS["sonorant"]:
        return "sonorant"
    elif letter.upper() in VOWELS["voiced"]:
        return "voiced"
    elif letter.upper() in VOWELS["voiceless"]:
        return "voiceless"

def word_vowel_type(word):
    for letter_index in range(len(word) - 2, -1, -1):
        if letter_is_vowel(word[letter_index]):
            return get_vowel_type(word[letter_index])
