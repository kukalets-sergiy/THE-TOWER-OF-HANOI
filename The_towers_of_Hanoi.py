"""THE TOWER OF HANOI, by Al Sweigart al@inventwithpython.com
A puzzle involving moving disks."""
import copy
import sys

TOTAL_DISKS = 5
# The more disks, the harder the puzzle.
# Initially, all disks are on tower A:
SOLVED_TOWER = list(range(TOTAL_DISKS, 0, -1))   # [5, 4, 3, 2, 1]

def main():
    """Plays one game of Tower of Hanoi."""
    print(
        """THE TOWER OF HANOI, by Al Sweigart al@inventwithpython.com
        Move the tower of disks, one disk at a time, to another tower. Larger
        disks cannot rest on top of a smaller disk.
        More info at https://en.wikipedia.org/wiki/Tower_of_Hanoi
        """
    )

    towers = {"A": copy.copy(SOLVED_TOWER), "B": [], "C": []}
    while True:  # One move per iteration.
        # Display towers and disks:
        displayTowers(towers)
        # Ask player for a move:
        fromTower, toTower = getPlayerMove(towers)
        # Move the top disk from fromTower to toTower:
        disk = towers[fromTower].pop()
        towers[toTower].append(disk)
        # Check if the puzzle is solved:
        if SOLVED_TOWER in (towers["B"], towers["C"]):
            displayTowers(towers)  # Display towers one last time.
            print("You have solved the puzzle! Well done!")
            sys.exit()

def getPlayerMove(towers):
    """Asks the player for a move. Returns (fromTower, toTower)."""
    while True:  # Continue until a valid move is entered.
        print('Enter the letters of "from" and "to" towers, or QUIT.')
        print("(e.g., AB to move a disk from tower A to tower B.)")
        response = input("> ").upper().strip()
        if response == "QUIT":
            print("Thanks for playing!")
            sys.exit()
        # Ensure the player entered valid tower letters:
        if response not in ("AB", "AC", "BA", "BC", "CA", "CB"):
            print("Enter one of AB, AC, BA, BC, CA, or CB.")
            continue  # Ask for the move again.

        # Assign meaningful variable names:
        fromTower, toTower = response[0], response[1]
        if len(towers[fromTower]) == 0:
            # The fromTower cannot be empty:
            print("You selected a tower with no disks.")
            continue  # Ask for the move again.
        elif len(towers[toTower]) == 0:
            # You can move any disk to an empty tower:
            return fromTower, toTower
        elif towers[toTower][-1] < towers[fromTower][-1]:
            print("Can't put larger disks on top of smaller ones.")
            continue  # Ask for the move again.
        else:
            # Valid move, return the selected towers:
            return fromTower, toTower

def displayTowers(towers):
    """Displays the three towers with disks."""
    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (towers["A"], towers["B"], towers["C"]):
            if level >= len(tower):
                displayDisk(0)  # Display an empty rod segment.
            else:
                displayDisk(tower[level])  # Display the disk.
        print()
    # Display tower labels A, B, and C:
    emptySpace = " " * TOTAL_DISKS
    print(f"{emptySpace}A{emptySpace}{emptySpace}B{emptySpace}{emptySpace}C\n")

def displayDisk(width):
    """Displays a disk of the given width. Width 0 means no disk."""
    emptySpace = " " * (TOTAL_DISKS - width)
    if width == 0:
        # Display a rod segment without a disk:
        print(f"{emptySpace}||{emptySpace}", end="")
    else:
        # Display the disk:
        disk = "@" * width
        numLabel = str(width).rjust(2, "_")
        print(f"{emptySpace}{disk}{numLabel}{disk}{emptySpace}", end="")

# If the program was run (not imported), start the game:
if __name__ == "__main__":
    main()
