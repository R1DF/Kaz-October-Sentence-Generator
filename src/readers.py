# Imports
import os
import json

# Parameters
PRONOUNS_FILE = json.load(open(os.getcwd() + "\\json_data\\pronouns.json", "r", encoding="utf-8"))
PRONOUNS, PRONOUN_DESCRIPTIONS = PRONOUNS_FILE["pronouns"], PRONOUNS_FILE["descriptions"]

SENTENCE_TYPES_FILE = json.load(open(os.getcwd() + "\\json_data\\sentence_types.json", "r", encoding="utf-8"))
SENTENCE_TYPES, SENTENCE_TYPES_DESCRIPTIONS = SENTENCE_TYPES_FILE["sentence_types"], SENTENCE_TYPES_FILE["descriptions"]

TENSES_FILE = json.load(open(os.getcwd() + "\\json_data\\tenses.json", "r", encoding="utf-8"))
TENSES, TENSES_DESCRIPTIONS = TENSES_FILE["tenses"], TENSES_FILE["descriptions"]

VERBS = json.load(open(os.getcwd() + "\\json_data\\verbs.json", "r", encoding="utf-8"))
