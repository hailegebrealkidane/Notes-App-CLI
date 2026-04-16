from notes import NotesApp


def main():
    app = NotesApp()

    while True:
        print("\nNotes App")
        print("1. View Notes")
        print("2. Add Note")
        print("3. Search Notes")
        print("4. Delete Note")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            app.view_notes()
        elif choice == "2":
            content = input("Enter note: ")
            app.add_note(content)
        elif choice == "3":
            keyword = input("Enter keyword: ")
            app.search_notes(keyword)
        elif choice == "4":
            index = int(input("Enter note number to delete: "))
            app.delete_note(index - 1)
        elif choice == "5":
            break
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()
