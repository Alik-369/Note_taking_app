Simple Note-Taking Program
A command-line note application that allows users to manage text notes stored in a file. The program provides a menu-driven interface with four main functions:

Add Note - Users can enter and save new notes to a text file
View Notes - Displays all saved notes in a numbered list
Clear Notes - Deletes all stored notes
Exit - Closes the program

How It Works:
The program uses a continuous loop that displays a menu and prompts users to select an option (1-4). Notes are stored persistently in a file called note.txt, meaning they remain saved even after the program closes.
Key Features:

File-based storage: Notes are written to and read from note.txt using Python's file handling
Error handling: The program catches exceptions for invalid inputs (non-numeric entries) and file operations (missing files)
User-friendly interface: Simple numbered menu with clear prompts and confirmation messages
Persistent data: Notes remain saved between program sessions

Technical Implementation:
The code is organized into separate functions for each operation (add_note(), view_notes(), clear_notes()) and a main program() function that routes to the appropriate action based on user choice. The main loop handles user input, error catching, and program flow control.
This is a practical beginner-level Python project that demonstrates fundamental programming concepts including functions, file I/O, loops, conditional statements, and exception handling.
