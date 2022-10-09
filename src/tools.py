# Imports
import os

# System commands
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def await_key_press():
    # Works on Windows only
    if os.name == "nt":
        os.system("pause")
    else:
        input("\nPress Enter to exit.\n")

def title(program_title):
    # Works on Windows only
    if os.name == "nt":
        os.system(f"title {program_title}")

# Formatting functions
def break_line(amount=1):
    print("\n" * amount)

# Inputs
def pursue_int_input(message, minimum, maximum):
    while True:
        user_input = input(f"{message}: ")
        if user_input.isnumeric():
            user_input = int(user_input)
            if user_input < minimum or user_input > maximum:
                print("ERROR: Please enter a valid number.\n")
                continue
            return user_input
        print("ERROR: Please enter a valid number.\n")
