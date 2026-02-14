import random

chromatic = ["C", "C#", "D", "D#", "E", "F",
             "F#", "G", "G#", "A", "A#", "B"]

# Enharmonic equivalents
enharmonics = {
    "DB": "C#",
    "EB": "D#",
    "GB": "F#",
    "AB": "G#",
    "BB": "A#"
}

chord_formulas = {
    "maj7": [0, 4, 7, 11],
    "min7": [0, 3, 7, 10],
    "7":    [0, 4, 7, 10]
}

def build_chord(root, formula):
    root_index = chromatic.index(root)
    return [
        chromatic[(root_index + interval) % 12]
        for interval in formula
    ]

def normalize(note):
    note = note.strip().upper()
    if note in enharmonics:
        return enharmonics[note]
    return note

print("🎶 1-3-5-7 Chord Trainer (Enharmonic Friendly)")
print("Type notes one at a time.")
print("Type 'quit' anytime to exit.\n")

roots = chromatic.copy()
chord_types = list(chord_formulas.keys())

while True:
    full_cycle = [(r, ct) for r in roots for ct in chord_types]
    random.shuffle(full_cycle)

    for root, chord_type in full_cycle:
        formula = chord_formulas[chord_type]
        correct_notes = set(build_chord(root, formula))
        entered = set()

        print("\n---------------------------")
        print(f"What are the 1 3 5 7 of {root}{chord_type}?")

        while entered != correct_notes:
            user_input = input("Note: ")

            if user_input.lower() == "quit":
                print("Good practice session 🎹")
                exit()

            note = normalize(user_input)

            if note in correct_notes:
                if note in entered:
                    print("Already entered.")
                else:
                    print("Correct!")
                    entered.add(note)
            else:
                print("Not in this chord.")

        print(f"🔥 Correct! {root}{chord_type} complete!")

    print("\n🎉 You completed all chords! Reshuffling...\n")

