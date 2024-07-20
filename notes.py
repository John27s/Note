def display_menu():
    print("\nNote-Taking Application")
    print("===============")
    print("1. View notes")
    print("2. Add a new note")
    print("3. Search for a note by title")
    print("4. Delete a note")
    print("5. Exit")

def view_notes(notes):
    if not notes:
        print("\nNo notes available.")
    else:
        print("\nNotes:")
        for title, content in notes.items():
            print(f"Title: {title}\nContent: {content}\n")

def add_note(notes):
    title = input("\nEnter the title of the note: ")
    content = input("Enter the content of the note: ")
    notes[title] = content
    print("Note added successfully.")

def search_note(notes):
    title = input("\nEnter the title of the note you want to search: ")
    if title in notes:
        print(f"Content: {notes[title]}")
    else:
        print("Note not found.")

def delete_note(notes):
    title = input("\nEnter the title of the note you want to delete: ")
    if title in notes:
        del notes[title]
        print("Note deleted successfully.")
    else:
        print("Note not found.")

def main():
    notes = {}
    while True:
        display_menu()
        choice = input("\nChoose an option: ")
        
        if choice == '1':
            view_notes(notes)
        elif choice == '2':
            add_note(notes)
        elif choice == '3':
            search_note(notes)
        elif choice == '4':
            delete_note(notes)
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()