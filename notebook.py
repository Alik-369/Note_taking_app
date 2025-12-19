print(f"1.Enter a note\n2.View notes\n3.Clear all notes\n4.Exit")


def add_note():
    note = input("Enter your note:")
    with open("note.txt", "a") as file:
        file.write(note + "\n")
    print("Note added successfully.")
def view_notes():
    print("Your notes:")
    with open("note.txt", "r") as file:
        note = file.readlines()
        for idx, note in enumerate(note,start=1):
            print(f"{idx}. {note.strip()}")
def clear_notes():
    open("note.txt", "w").close()
    print("All notes cleared.")   
def program():
    
    if choice ==1:
        add_note()
    elif choice ==2:
        view_notes()
    elif choice ==3:
        clear_notes()
    elif choice ==4:
        print("Exiting the program.")
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
while True:
    choice = int(input("Enter your choice(1-4):"))
    
    try:
        program()
    except Exception as e:
        print(f"An error occurred: {e}")
    
    if choice == 4:
        break


