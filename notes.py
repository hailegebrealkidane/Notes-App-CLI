from storage import load_notes, save_notes


class NotesApp:
    def __init__(self):
        self.notes = load_notes()

    def view_notes(self):
        if not self.notes:
            print("No notes found.")
            return

        for i, note in enumerate(self.notes):
            print(f"{i+1}. {note}")

    def add_note(self, content):
        self.notes.append(content)
        save_notes(self.notes)
        print("Note added!")

    def search_notes(self, keyword):
        results = [n for n in self.notes if keyword.lower() in n.lower()]
        if not results:
            print("No matching notes.")
            return

        for i, note in enumerate(results):
            print(f"{i+1}. {note}")

    def delete_note(self, index):
        if 0 <= index < len(self.notes):
            self.notes.pop(index)
            save_notes(self.notes)
            print("Note deleted!")
        else:
            print("Invalid note number")
