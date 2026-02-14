import random
import time
import sys
import pyfiglet

## all key signature accidentals
all_major_keys = {
    "C":  [],
    "G":  ["F#"],
    "D":  ["F#", "C#"],
    "A":  ["F#", "C#", "G#"],
    "E":  ["F#", "C#", "G#", "D#"],
    "B":  ["F#", "C#", "G#", "D#", "A#"],
    "F#": ["F#", "C#", "G#", "D#", "A#", "E#"],
    "C#": ["F#", "C#", "G#", "D#", "A#", "E#", "B#"],
    "F":  ["Bb"],
    "Bb": ["Bb", "Eb"],
    "Eb": ["Bb", "Eb", "Ab"],
    "Ab": ["Bb", "Eb", "Ab", "Db"]
}

#make sure user doesn't get answers wrong for incorrect capitalization
def normalize_input(input):
    return input.strip().capitalize()

## prints text with a typerwrite effect
def typewriter_effect(text, delay=0.05):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)

print(pyfiglet.figlet_format("Major Key Trainer"))
typewriter_effect("Step 1: Enter number of accidentals. \n")
typewriter_effect("Step 2: Enter the accidentals. \n")
typewriter_effect("Type 'quit' anytime to exit.\n")
print()

while True:
    keys = list(all_major_keys.keys())
    random.shuffle(keys)

    for key in keys:
        correct = set(all_major_keys[key])
        num_correct = len(correct)

        print("\n---------------------------")
        print(f"How many accidentals are in {key} major?")

        user_input = input("Number: ")

        if user_input.lower() == "quit":
            print("BYEEEE")
            exit()

        if not user_input.isdigit():
            print("Invalid input. Moving to next key.")
            continue

        if int(user_input) != num_correct:
            print(f"❌ Incorrect. {key} major has {num_correct} accidentals.")
            continue

        print("✅ Correct! Now name them.")

        # If no accidentals (C major)
        if num_correct == 0:
            input("Press Enter to continue.")
            print("✅ C major complete!")
            continue

        entered = set()

        while entered != correct:
            note_input = input("Accidental: ")

            if note_input.lower() == "quit":
                print("BYEEE")
                exit()

            note = normalize_input(note_input)

            if note in correct:
                if note in entered:
                    print("Already entered.")
                else:
                    print("Correct!")
                    entered.add(note)
            else:
                print("Not in this key signature.")

        print(f"Good! {key} major complete!")

    print("\n You completed all 12 keys! Reshuffling...\n")
