"""THE TOWER OF HANOI, by Al Sweigart al@inventwithpython.com
A puzzle involving moving disks."""

import copy  # To make deep copies of lists
import sys   # To use sys.exit() to quit the program

TOTAL_DISKS = 5  # The more disks, the harder the puzzle
# The initial solved state, all disks on tower A:
SOLVED_TOWER = list(range(TOTAL_DISKS, 0, -1))  # [5, 4, 3, 2, 1]

def main():
    """Plays one game of Tower of Hanoi."""
    # Display the intro text:
    print(
        """THE TOWER OF HANOI, 
        Move the tower of disks, one disk at a time, to another tower. Larger
        disks cannot rest on top of a smaller disk.
        More info at https://en.wikipedia.org/wiki/Tower_of_Hanoi
        """
    )

    # The towers dictionary: A contains the disks, B and C are empty
    towers = {"A": copy.copy(SOLVED_TOWER), "B": [], "C": []}   # A: [5, 4, 3, 2, 1], B: [], C: []

    # The game loop, continues until puzzle is solved
    while True:
        displayTowers(towers)  # Show the current state of the towers
        fromTower, toTower = getPlayerMove(towers)  # Ask player for a valid move
        disk = towers[fromTower].pop()  # Remove the top disk from the fromTower
        towers[toTower].append(disk)  # Place the disk on the toTower

        # Check if the puzzle is solved by looking at tower B or C:
        if SOLVED_TOWER in (towers["B"], towers["C"]):  # If B or C contains [5, 4, 3, 2, 1]
            displayTowers(towers)  # Display the final state of the towers
            print("You have solved the puzzle! Well done!")  # Puzzle solved message
            sys.exit()  # Quit the game

def getPlayerMove(towers):
    """Asks the player for a move. Returns (fromTower, toTower)."""
    while True:  # Loop until a valid move is made
        print('Enter the letters of "from" and "to" towers, or QUIT.')  # Example of valid input format
        print("(e.g., AB to move a disk from tower A to tower B.)")
        response = input("> ").upper().strip()  # Get input, convert to uppercase, and strip spaces

        if response == "QUIT":  # Check if the player wants to quit
            print("Thanks for playing!")  # Exit message
            sys.exit()  # Quit the game

        # Ensure the player entered valid tower letters:
        if response not in ("AB", "AC", "BA", "BC", "CA", "CB"):  # Invalid move check
            print("Enter one of AB, AC, BA, BC, CA, or CB.")  # Valid options reminder
            continue  # Ask again

        fromTower, toTower = response[0], response[1]  # Split response into source and destination towers

        if len(towers[fromTower]) == 0:  # Check if the source tower is empty
            print("You selected a tower with no disks.")  # Error message
            continue  # Ask again
        elif len(towers[toTower]) == 0:  # If destination is empty, move is valid
            return fromTower, toTower  # Valid move (for example "A", "B")
        elif towers[toTower][-1] < towers[fromTower][-1]:  # Can't place a larger disk on a smaller one
            print("Can't put larger disks on top of smaller ones.")  # Error message
            continue  # Ask again
        else:
            return fromTower, toTower  # Return valid move

def displayTowers(towers):
    """Displays the three towers with disks."""
    # Loop from top disk position (TOTAL_DISKS) to bottom (-1):
    for level in range(TOTAL_DISKS, -1, -1):  # Start at TOTAL_DISKS down to 0
        for tower in (towers["A"], towers["B"], towers["C"]):  # For each tower A, B, C:
            if level >= len(tower):  # If there's no disk at this level:
                displayDisk(0)  # Display an empty rod segment:      ||         ||         ||
            else:
                displayDisk(tower[level])  # Display the disk at this level. for disk 4: @@@@_4_@@@@, for 3: @@@_3_@@@.
        print()  # Move to the next line after displaying one level

    # Show tower labels after all levels are printed:
    emptySpace = " " * TOTAL_DISKS  # Empty space padding for tower alignment
    print(f"{emptySpace}A{emptySpace}{emptySpace}B{emptySpace}{emptySpace}C\n")  # Print A, B, C labels

def displayDisk(width):
    """Displays a disk of the given width. Width 0 means no disk."""
    emptySpace = " " * (TOTAL_DISKS - width)  # Create space around the disk
    if width == 0:
        # Display an empty rod segment if no disk:
        print(f"{emptySpace}||{emptySpace}", end="")  # e.g., '   ||   '
    else:
        # Display the disk, e.g., '@@1@@', where '1' is the size:
        disk = "@" * width  # Create the disk display with @ symbols
        numLabel = str(width).rjust(2, "_")  # Right-align the disk number with underscore padding:_5 _4
        print(f"{emptySpace}{disk}{numLabel}{disk}{emptySpace}", end="")  # e.g., '  @@@_3@@@  '

# If the program is run (not imported), start the game:
if __name__ == "__main__":
    main()  # Call the main function to start the game
