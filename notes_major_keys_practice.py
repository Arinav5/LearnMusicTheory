import random

# Key signatures (only accidentals)
key_signatures = {
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

def normalize(note):
    return note.strip().capitalize()

print("🎼 Key Signature Trainer (Level 2)")
print("Step 1: Enter number of accidentals.")
print("Step 2: Enter the accidentals.")
print("Type 'quit' anytime to exit.\n")

while True:
    keys = list(key_signatures.keys())
    random.shuffle(keys)

    for key in keys:
        correct = set(key_signatures[key])
        num_correct = len(correct)

        print("\n---------------------------")
        print(f"How many accidentals are in {key} major?")

        user_input = input("Number: ")

        if user_input.lower() == "quit":
            print("Good practice session 🎹")
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
                print("Good practice session 🎹")
                exit()

            note = normalize(note_input)

            if note in correct:
                if note in entered:
                    print("Already entered.")
                else:
                    print("Correct!")
                    entered.add(note)
            else:
                print("Not in this key signature.")

        print(f"🔥 Good! {key} major complete!")

    print("\n🎉 You completed all 12 keys! Reshuffling...\n")

