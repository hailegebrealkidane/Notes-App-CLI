import json
import os

FILE_NAME = "notes.json"


def load_notes():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_notes(notes):
    with open(FILE_NAME, "w") as f:
        json.dump(notes, f, indent=4)
